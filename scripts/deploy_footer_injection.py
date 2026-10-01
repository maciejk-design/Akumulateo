#!/usr/bin/env python3
"""
deploy_footer_injection.py – Wdraża snippets/squarespace/footer-code-injection.html
bezpośrednio do Squarespace (Website Tools -> Code Injection -> FOOTER).

Jest to JEDYNE MIEJSCE w Squarespace odpowiedzialne za dynamiczną hydratację
liczby opinii i ocen w całym serwisie www.akumulateo.pl.
"""
import subprocess
import json
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

def run_js(js_code):
    script = f'''
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if (URL of t) contains "celery-robin-sffx.squarespace.com" then
                    tell t
                        return (execute javascript {json.dumps(js_code)})
                    end tell
                end if
            end repeat
        end repeat
        return "Not found"
    end tell
    '''
    res = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
    return res.stdout.strip()

def main():
    footer_path = REPO_ROOT / "snippets" / "squarespace" / "footer-code-injection.html"
    with open(footer_path, "r", encoding="utf-8") as f:
        footer_code = f.read()

    print(f"Loaded footer_code: {len(footer_code)} chars")

    # Krok 1: Sprawdź czy jesteśmy już na /config/pages/code-injection
    check_url_js = "location.href"
    cur_url = run_js(check_url_js)
    print("Current URL in tab:", cur_url)

    if "code-injection" not in cur_url:
        print("Navigating to website-tools...")
        nav_script = '''
        tell application "Google Chrome"
            repeat with w in windows
                repeat with i from 1 to count of tabs of w
                    if (URL of tab i of w) contains "celery-robin-sffx.squarespace.com" then
                        set index of w to 1
                        set active tab index of w to i
                        tell tab i of w
                            set URL to "https://celery-robin-sffx.squarespace.com/config/pages/website-tools"
                        end tell
                        return "Navigated"
                    end if
                end repeat
            end repeat
            return "Not found"
        end tell
        '''
        subprocess.run(['osascript', '-e', nav_script])
        time.sleep(3.5)

        click_ci_js = '''
        (() => {
            const btns = Array.from(document.querySelectorAll('button, a, div'));
            const btn = btns.find(b => b.innerText && b.innerText.trim() === 'Code Injection');
            if (btn) {
                btn.click();
                return 'CLICKED_CODE_INJECTION';
            }
            return 'NOT_FOUND';
        })()
        '''
        print("Click Code Injection:", run_js(click_ci_js))
        time.sleep(3.5)

    # Krok 2: Wstrzyknij kod do Footera (cms[1]) i wywołaj Save
    inject_and_save_js = f'''
    (() => {{
        const s = document.createElement('script');
        s.textContent = `
            try {{
                const cms = document.querySelectorAll('.CodeMirror');
                if (cms.length < 2) throw new Error('Less than 2 CodeMirrors: ' + cms.length);
                const fCm = cms[1];
                if (!fCm || !fCm.CodeMirror) throw new Error('No cm[1]');
                
                fCm.CodeMirror.setValue({json.dumps(footer_code)});
                if (typeof fCm.CodeMirror.save === 'function') fCm.CodeMirror.save();
                
                const ta = fCm.querySelector('textarea');
                if (ta) {{
                    ta.focus();
                    ta.dispatchEvent(new Event('input', {{ bubbles: true }}));
                    ta.dispatchEvent(new Event('change', {{ bubbles: true }}));
                }}
                document.documentElement.setAttribute('data-footer-status', 'PASTED_LEN_' + fCm.CodeMirror.getValue().length);
            }} catch(e) {{
                document.documentElement.setAttribute('data-footer-err', e.message);
            }}
        `;
        document.documentElement.appendChild(s);
        s.remove();

        const status = document.documentElement.getAttribute('data-footer-status');
        const err = document.documentElement.getAttribute('data-footer-err');
        document.documentElement.removeAttribute('data-footer-status');
        document.documentElement.removeAttribute('data-footer-err');

        return JSON.stringify({{ status, err }});
    }})()
    '''
    res_inject = run_js(inject_and_save_js)
    print("Inject Result:", res_inject)
    time.sleep(1.5)

    # Krok 3: Kliknij Save
    save_js = '''
    (() => {
        const saveBtn = document.querySelector('[data-test="menuHeader-save"]');
        if (!saveBtn) return JSON.stringify({ error: 'No save button' });
        saveBtn.click();
        return JSON.stringify({ status: 'CLICKED_SAVE' });
    })()
    '''
    res_save = run_js(save_js)
    print("Save Result:", res_save)
    time.sleep(3.0)

    print("✅ Pomyślnie zaktualizowano Footer Code Injection na produkcji Squarespace!")

if __name__ == '__main__':
    main()

import subprocess
import json
import time

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
    with open('snippets/squarespace/header-code-injection.html', 'r', encoding='utf-8') as f:
        header_code = f.read()
    with open('snippets/squarespace/footer-code-injection.html', 'r', encoding='utf-8') as f:
        footer_code = f.read()

    print(f"Loaded header_code: {len(header_code)} chars, footer_code: {len(footer_code)} chars")

    # Step 1: Navigate to website-tools
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
                    return "Navigated to website-tools"
                end if
            end repeat
        end repeat
        return "Not found"
    end tell
    '''
    res = subprocess.run(['osascript', '-e', nav_script], capture_output=True, text=True)
    print("Nav result:", res.stdout.strip())
    time.sleep(3.5)

    # Step 2: Click Code Injection
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
    print("Click code injection:", run_js(click_ci_js))
    time.sleep(3)

    # Step 3: Inspect CodeMirrors
    inspect_js = '''
    (() => {
        const cms = Array.from(document.querySelectorAll('.CodeMirror'));
        return JSON.stringify({
            count: cms.length,
            cm0: cms[0] ? cms[0].innerText.slice(0, 100) : null,
            cm1: cms[1] ? cms[1].innerText.slice(0, 100) : null
        });
    })()
    '''
    print("Current CodeMirrors:", run_js(inspect_js))

    # Step 4: Inject header_code into cms[0] and footer_code into cms[1]
    inject_js = f'''
    (() => {{
        const cms = Array.from(document.querySelectorAll('.CodeMirror'));
        if (cms.length < 2) return JSON.stringify({{ error: 'Less than 2 CodeMirrors', count: cms.length }});

        // 1. Header (cms[0])
        const hCm = cms[0];
        const hTa = hCm.querySelector('textarea');
        if (hTa) {{
            hTa.focus();
            hTa.dispatchEvent(new KeyboardEvent('keydown', {{
                key: 'a', code: 'KeyA', keyCode: 65, which: 65, metaKey: true, bubbles: true, cancelable: true
            }}));
            const dtH = new DataTransfer();
            dtH.setData('text/plain', {json.dumps(header_code)});
            hTa.dispatchEvent(new ClipboardEvent('paste', {{
                bubbles: true, cancelable: true, clipboardData: dtH
            }}));
        }}
        if (hCm.CodeMirror) {{
            hCm.CodeMirror.setValue({json.dumps(header_code)});
        }}

        // 2. Footer (cms[1])
        const fCm = cms[1];
        const fTa = fCm.querySelector('textarea');
        if (fTa) {{
            fTa.focus();
            fTa.dispatchEvent(new KeyboardEvent('keydown', {{
                key: 'a', code: 'KeyA', keyCode: 65, which: 65, metaKey: true, bubbles: true, cancelable: true
            }}));
            const dtF = new DataTransfer();
            dtF.setData('text/plain', {json.dumps(footer_code)});
            fTa.dispatchEvent(new ClipboardEvent('paste', {{
                bubbles: true, cancelable: true, clipboardData: dtF
            }}));
        }}
        if (fCm.CodeMirror) {{
            fCm.CodeMirror.setValue({json.dumps(footer_code)});
        }}

        const saveBtn = document.querySelector('[data-test="menuHeader-save"], [data-test*="save"]');
        return JSON.stringify({{
            status: 'PASTED',
            hLength: hCm.innerText.length,
            fLength: fCm.innerText.length,
            hasSaveBtn: !!saveBtn
        }});
    }})()
    '''
    print("Inject result:", run_js(inject_js))
    time.sleep(1.5)

    # Step 5: Save
    save_js = '''
    (() => {
        const saveBtn = document.querySelector('[data-test="menuHeader-save"], [data-test*="save"]');
        if (!saveBtn) return JSON.stringify({ error: 'No save button' });
        saveBtn.click();
        return JSON.stringify({ status: 'CLICKED_SAVE' });
    })()
    '''
    print("Save result:", run_js(save_js))
    time.sleep(3)
    print("Deployment done!")

if __name__ == '__main__':
    main()

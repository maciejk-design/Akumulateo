#!/usr/bin/env python3
"""
Automates deployment of snippets/squarespace/home-page-header-injection.html
into Squarespace 7.1: Pages -> Home (Settings) -> Advanced -> Page Header Code Injection.
Uses DOM text container chunking + main-world CodeMirror API execution
to avoid AppleScript argument length limits and cross-world isolation barriers.
"""
import subprocess
import json
import time

def run_js(js_code):
    escaped = json.dumps(js_code)
    script = f'''
tell application "Google Chrome"
    repeat with w in windows
        repeat with t in tabs of w
            if (URL of t) contains "celery-robin-sffx.squarespace.com" then
                tell t
                    return (execute javascript {escaped})
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
    with open('snippets/squarespace/home-page-header-injection.html', 'r', encoding='utf-8') as f:
        injection_code = f.read()

    total_len = len(injection_code)
    print(f"Loaded home injection code: {total_len} chars")

    # Step 0: Ensure tab on /config/pages
    nav_script = '''
    tell application "Google Chrome"
        repeat with w in windows
            repeat with i from 1 to count of tabs of w
                if (URL of tab i of w) contains "celery-robin-sffx.squarespace.com" then
                    set index of w to 1
                    set active tab index of w to i
                    tell tab i of w
                        if not ((URL of tab i of w) is "https://celery-robin-sffx.squarespace.com/config/pages") then
                            set URL to "https://celery-robin-sffx.squarespace.com/config/pages"
                        end if
                    end tell
                    return "Navigated"
                end if
            end repeat
        end repeat
        return "Not found"
    end tell
    '''
    subprocess.run(['osascript', '-e', nav_script])
    time.sleep(2.5)

    # Step 1: Open dialog if not already open
    open_js = '''
    (() => {
        let dialog = document.querySelector('[role=dialog]');
        if (dialog) return 'DIALOG_ALREADY_OPEN';
        const btn = document.querySelector('button[aria-label="Page settings Home"]');
        if (btn) {
            btn.click();
            return 'CLICKED_HOME_SETTINGS_BTN';
        }
        return 'NO_DIALOG_NO_BTN';
    })()
    '''
    open_res = run_js(open_js)
    print("Open dialog:", open_res)
    time.sleep(2)

    # Step 2: Click Advanced tab
    adv_js = '''
    (() => {
        const dialog = document.querySelector('[role=dialog]');
        if (!dialog) return JSON.stringify({ error: 'No dialog' });
        const items = Array.from(dialog.querySelectorAll('a, button, p, span'));
        const adv = items.find(el => el.innerText && el.innerText.trim() === 'Advanced');
        if (!adv) return JSON.stringify({ error: 'No Advanced tab' });
        const clickable = adv.closest('a') || adv.closest('button') || adv;
        clickable.click();
        return 'CLICKED_ADVANCED';
    })()
    '''
    adv_res = run_js(adv_js)
    print("Click advanced:", adv_res)
    time.sleep(2)

    # Step 3: Setup DOM container for code chunks
    setup_js = """
    (() => {
        let el = document.getElementById('__INJECTION_CODE_CONTAINER__');
        if (!el) {
            el = document.createElement('script');
            el.type = 'text/plain';
            el.id = '__INJECTION_CODE_CONTAINER__';
            document.body.appendChild(el);
        }
        el.textContent = '';
        return 'CONTAINER_READY';
    })()
    """
    run_js(setup_js)

    # Step 4: Append chunks to container textContent
    chunk_size = 5000
    num_chunks = (total_len + chunk_size - 1) // chunk_size

    for i in range(num_chunks):
        chunk = injection_code[i * chunk_size : (i + 1) * chunk_size]
        chunk_json = json.dumps(chunk)
        js = f"document.getElementById('__INJECTION_CODE_CONTAINER__').textContent += {chunk_json}; document.getElementById('__INJECTION_CODE_CONTAINER__').textContent.length"
        run_js(js)

    # Step 5: Inject main-world script to set cm.CodeMirror.setValue
    apply_js = """
    (() => {
        const s = document.createElement('script');
        s.textContent = `
            try {
                const container = document.getElementById('__INJECTION_CODE_CONTAINER__');
                if (!container) throw new Error('No container found');
                const fullCode = container.textContent;
                
                const cm = document.querySelector('.CodeMirror');
                if (!cm) throw new Error('No .CodeMirror element');
                if (!cm.CodeMirror) throw new Error('No cm.CodeMirror instance');
                
                cm.CodeMirror.setValue(fullCode);
                if (typeof cm.CodeMirror.save === 'function') {
                    cm.CodeMirror.save();
                }
                
                document.querySelectorAll('textarea').forEach(ta => {
                    ta.dispatchEvent(new Event('input', { bubbles: true }));
                    ta.dispatchEvent(new Event('change', { bubbles: true }));
                });
                
                document.documentElement.setAttribute('data-apply-success', 'SAVED_LEN_' + cm.CodeMirror.getValue().length);
            } catch(e) {
                document.documentElement.setAttribute('data-apply-err', e.message);
            }
        `;
        document.documentElement.appendChild(s);
        s.remove();
        
        const success = document.documentElement.getAttribute('data-apply-success');
        const err = document.documentElement.getAttribute('data-apply-err');
        document.documentElement.removeAttribute('data-apply-success');
        document.documentElement.removeAttribute('data-apply-err');
        
        return JSON.stringify({ success, err });
    })()
    """
    apply_res = run_js(apply_js)
    print("Apply result:", apply_res)
    time.sleep(2)

    # Step 6: Click Save button and clean up container
    save_js = '''
    (() => {
        const dialog = document.querySelector('[role=dialog]');
        if (!dialog) return 'NO_DIALOG';
        const saveBtn = dialog.querySelector('[data-test="nav-modal-left-button"]');
        if (!saveBtn) return 'NO_SAVE_BUTTON';
        saveBtn.click();
        
        const container = document.getElementById('__INJECTION_CODE_CONTAINER__');
        if (container) container.remove();
        
        return 'CLICKED_SAVE';
    })()
    '''
    save_res = run_js(save_js)
    print("Save result:", save_res)
    time.sleep(3.5)

    check_dialog_js = '''
    (() => {
        const dialog = document.querySelector('[role=dialog]');
        return dialog ? 'DIALOG_STILL_OPEN' : 'DIALOG_CLOSED_SAVED';
    })()
    '''
    status = run_js(check_dialog_js)
    print("Final status:", status)

if __name__ == '__main__':
    main()

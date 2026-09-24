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
    with open('snippets/squarespace/home-page-header-injection.html', 'r', encoding='utf-8') as f:
        injection_code = f.read()

    print(f"Loaded injection code: {len(injection_code)} chars")

    # Step 0: Ensure we are on /config/pages
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
    print("Ensured tab on /config/pages")
    time.sleep(3)

    # Step 1: Ensure dialog is open or click button[aria-label="Page settings Home"]
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
    print("Open dialog:", run_js(open_js))
    time.sleep(2)

    # Step 2: Click Advanced tab
    adv_js = '''
    (() => {
        const dialog = document.querySelector('[role=dialog]');
        if (!dialog) return JSON.stringify({ error: 'No dialog' });
        const items = Array.from(dialog.querySelectorAll('a, button, p, span'));
        const adv = items.find(el => el.innerText && el.innerText.trim() === 'Advanced');
        if (!adv) return JSON.stringify({ error: 'No Advanced text' });
        const clickable = adv.closest('a') || adv.closest('button') || adv;
        clickable.click();
        return 'CLICKED_ADVANCED';
    })()
    '''
    print("Click advanced:", run_js(adv_js))
    time.sleep(2)

    # Step 3: Paste into CodeMirror
    paste_js = f'''
    (() => {{
        const dialog = document.querySelector('[role=dialog]');
        if (!dialog) return JSON.stringify({{ error: 'No dialog' }});
        
        const cm = dialog.querySelector('.CodeMirror');
        if (!cm) return JSON.stringify({{ error: 'No CodeMirror' }});
        
        const ta = cm.querySelector('textarea');
        if (!ta) return JSON.stringify({{ error: 'No textarea' }});
        
        ta.focus();
        ta.dispatchEvent(new KeyboardEvent('keydown', {{
            key: 'a', code: 'KeyA', keyCode: 65, which: 65, metaKey: true, bubbles: true, cancelable: true
        }}));

        const dt = new DataTransfer();
        dt.setData('text/plain', {json.dumps(injection_code)});
        ta.dispatchEvent(new ClipboardEvent('paste', {{
            bubbles: true, cancelable: true, clipboardData: dt
        }}));

        if (cm.CodeMirror) {{
            cm.CodeMirror.setValue({json.dumps(injection_code)});
        }}

        const saveBtn = dialog.querySelector('[data-test="nav-modal-left-button"]');
        return JSON.stringify({{
            status: 'PASTED',
            cmLength: cm.innerText.length,
            hasSaveBtn: !!saveBtn
        }});
    }})()
    '''
    paste_res = run_js(paste_js)
    print("Paste result:", paste_res)
    time.sleep(1.5)

    # Step 4: Click Save
    save_js = '''
    (() => {
        const dialog = document.querySelector('[role=dialog]');
        if (!dialog) return JSON.stringify({ error: 'No dialog' });
        const saveBtn = dialog.querySelector('[data-test="nav-modal-left-button"]');
        if (!saveBtn) return JSON.stringify({ error: 'No save button' });
        saveBtn.click();
        return JSON.stringify({ status: 'CLICKED_SAVE' });
    })()
    '''
    save_res = run_js(save_js)
    print("Save result:", save_res)
    time.sleep(3)
    print("Deployment of home-page-header-injection.html SUCCESSFUL!")

if __name__ == '__main__':
    main()

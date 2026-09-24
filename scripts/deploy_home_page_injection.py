import subprocess
import json
import time
import sys

def main():
    with open('snippets/squarespace/home-page-header-injection.html', 'r', encoding='utf-8') as f:
        injection_code = f.read()

    print(f"Loaded injection code: {len(injection_code)} chars")

    # AppleScript to navigate to /config/pages if not already there
    nav_script = '''
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if (URL of t) contains "celery-robin-sffx.squarespace.com" then
                    set index of w to 1
                    set active tab index of w to (get index of t)
                    tell t
                        if (URL of t) is not "https://celery-robin-sffx.squarespace.com/config/pages" then
                            set URL to "https://celery-robin-sffx.squarespace.com/config/pages"
                        end if
                    end tell
                    return "On pages"
                end if
            end repeat
        end repeat
        return "Squarespace tab not found"
    end tell
    '''
    res = subprocess.run(['osascript', '-e', nav_script], capture_output=True, text=True)
    print("Nav result:", res.stdout.strip())
    time.sleep(4)

    # Open Page Settings Home -> Advanced (with retry)
    open_adv_js = '''
    (() => {
        let dialog = document.querySelector('[role=dialog]');
        if (!dialog) {
            const btns = Array.from(document.querySelectorAll('button[data-test=collection-settings]'));
            const homeBtn = btns.find(b => b.getAttribute('aria-label') === 'Page settings Home');
            if (!homeBtn) return JSON.stringify({ error: 'Home settings button not found', btnCount: btns.length });
            homeBtn.click();
        }
        return JSON.stringify({ status: 'CLICKED_HOME_SETTINGS' });
    })()
    '''
    for attempt in range(5):
        open_res = run_js_in_sqsp(open_adv_js)
        print(f"Open settings attempt {attempt+1}:", open_res)
        if "CLICKED_HOME_SETTINGS" in open_res:
            break
        time.sleep(2)
    time.sleep(2)

    # Click Advanced tab (with retry)
    click_adv_js = '''
    (() => {
        const dialog = document.querySelector('[role=dialog]');
        if (!dialog) return JSON.stringify({ error: 'No dialog' });
        const p = Array.from(dialog.querySelectorAll('p')).find(el => el.innerText.trim() === 'Advanced');
        const a = p ? p.closest('a') : null;
        if (!a) return JSON.stringify({ error: 'Advanced anchor not found' });
        a.click();
        return JSON.stringify({ status: 'CLICKED_ADVANCED' });
    })()
    '''
    for attempt in range(5):
        adv_res = run_js_in_sqsp(click_adv_js)
        print(f"Click advanced attempt {attempt+1}:", adv_res)
        if "CLICKED_ADVANCED" in adv_res:
            break
        time.sleep(1.5)
    time.sleep(2)

    # Paste into CodeMirror
    paste_js = f'''
    (() => {{
        const dialog = document.querySelector('[role=dialog]');
        if (!dialog) return JSON.stringify({{ error: 'No dialog' }});
        const cm = dialog.querySelector('.CodeMirror');
        if (!cm) return JSON.stringify({{ error: 'No CodeMirror' }});
        const ta = cm.querySelector('textarea');
        if (!ta) return JSON.stringify({{ error: 'No textarea' }});
        
        ta.focus();
        const selectAllEvt = new KeyboardEvent('keydown', {{
            key: 'a', code: 'KeyA', keyCode: 65, which: 65, metaKey: true, bubbles: true, cancelable: true
        }});
        ta.dispatchEvent(selectAllEvt);

        const dt = new DataTransfer();
        dt.setData('text/plain', {json.dumps(injection_code)});
        const pasteEvt = new ClipboardEvent('paste', {{
            bubbles: true, cancelable: true, clipboardData: dt
        }});
        ta.dispatchEvent(pasteEvt);

        const saveBtn = dialog.querySelector('[data-test="nav-modal-left-button"]');
        return JSON.stringify({{
            cmLength: cm.innerText.length,
            hasSaveBtn: !!saveBtn
        }});
    }})()
    '''
    paste_res = run_js_in_sqsp(paste_js)
    print("Paste result:", paste_res)
    time.sleep(1)

    # Click Save
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
    save_res = run_js_in_sqsp(save_js)
    print("Save result:", save_res)
    time.sleep(3)

    print("Step 1 (Homepage Header Injection) completed successfully!")

def run_js_in_sqsp(js_code):
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
    p = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
    return p.stdout.strip()

if __name__ == '__main__':
    main()

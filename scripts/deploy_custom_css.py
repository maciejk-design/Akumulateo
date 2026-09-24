import subprocess
import json
import time

def main():
    with open('snippets/squarespace/custom-css.css', 'r', encoding='utf-8') as f:
        custom_css = f.read()

    print(f"Loaded custom CSS: {len(custom_css)} chars")

    # Navigate to custom-css
    nav_script = '''
    tell application "Google Chrome"
        set w to front window
        repeat with t in tabs of w
            if (URL of t) contains "celery-robin-sffx.squarespace.com" then
                set active tab index of w to (get index of t)
                tell t
                    set URL to "https://celery-robin-sffx.squarespace.com/config/pages/custom-css"
                end tell
                return "Navigated to custom-css"
            end if
        end repeat
        return "Squarespace tab not found"
    end tell
    '''
    res = subprocess.run(['osascript', '-e', nav_script], capture_output=True, text=True)
    print("Nav result:", res.stdout.strip())
    time.sleep(3)

    # Paste into CodeMirror
    paste_js = f'''
    (() => {{
        const cm = document.querySelector('.CodeMirror');
        if (!cm) return JSON.stringify({{ error: 'No CodeMirror' }});
        const ta = cm.querySelector('textarea');
        if (!ta) return JSON.stringify({{ error: 'No textarea' }});
        
        ta.focus();
        const selectAllEvt = new KeyboardEvent('keydown', {{
            key: 'a', code: 'KeyA', keyCode: 65, which: 65, metaKey: true, bubbles: true, cancelable: true
        }});
        ta.dispatchEvent(selectAllEvt);

        const dt = new DataTransfer();
        dt.setData('text/plain', {json.dumps(custom_css)});
        const pasteEvt = new ClipboardEvent('paste', {{
            bubbles: true, cancelable: true, clipboardData: dt
        }});
        ta.dispatchEvent(pasteEvt);

        const saveBtn = document.querySelector('[data-test="menuHeader-save"]');
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
        const saveBtn = document.querySelector('[data-test="menuHeader-save"]');
        if (!saveBtn) return JSON.stringify({ error: 'No save button' });
        saveBtn.click();
        return JSON.stringify({ status: 'CLICKED_SAVE' });
    })()
    '''
    save_res = run_js_in_sqsp(save_js)
    print("Save result:", save_res)
    time.sleep(2)
    print("Custom CSS updated successfully!")

def run_js_in_sqsp(js_code):
    script = f'''
    tell application "Google Chrome"
        set w to front window
        repeat with t in tabs of w
            if (URL of t) contains "celery-robin-sffx.squarespace.com" then
                tell t
                    return (execute javascript {json.dumps(js_code)})
                end tell
            end if
        end repeat
        return "Not found"
    end tell
    '''
    p = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
    return p.stdout.strip()

if __name__ == '__main__':
    main()

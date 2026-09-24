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
    with open('snippets/squarespace/custom-css.css', 'r', encoding='utf-8') as f:
        custom_css = f.read()

    print(f"Loaded custom CSS: {len(custom_css)} chars")

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

    # Step 2: Click Custom CSS
    click_css_js = '''
    (() => {
        const btns = Array.from(document.querySelectorAll('button, a, div'));
        const btn = btns.find(b => b.innerText && b.innerText.trim() === 'Custom CSS');
        if (btn) {
            btn.click();
            return 'CLICKED_CUSTOM_CSS';
        }
        return 'NOT_FOUND';
    })()
    '''
    print("Click custom css:", run_js(click_css_js))
    time.sleep(3)

    # Step 3: Paste into CodeMirror
    paste_js = f'''
    (() => {{
        const cm = document.querySelector('.CodeMirror');
        if (!cm) return JSON.stringify({{ error: 'No CodeMirror' }});
        
        if (cm.CodeMirror) {{
            cm.CodeMirror.setValue({json.dumps(custom_css)});
        }} else {{
            const ta = cm.querySelector('textarea');
            if (!ta) return JSON.stringify({{ error: 'No textarea' }});
            ta.focus();
            const dt = new DataTransfer();
            dt.setData('text/plain', {json.dumps(custom_css)});
            ta.dispatchEvent(new ClipboardEvent('paste', {{
                bubbles: true, cancelable: true, clipboardData: dt
            }}));
        }}

        const saveBtn = document.querySelector('[data-test="menuHeader-save"], [data-test="nav-modal-left-button"]') || Array.from(document.querySelectorAll('button')).find(b => b.innerText && b.innerText.trim() === 'Save');
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
        const saveBtn = document.querySelector('[data-test="menuHeader-save"], [data-test="nav-modal-left-button"]') || Array.from(document.querySelectorAll('button')).find(b => b.innerText && b.innerText.trim() === 'Save');
        if (!saveBtn) return JSON.stringify({ error: 'No save button' });
        saveBtn.click();
        return JSON.stringify({ status: 'CLICKED_SAVE' });
    })()
    '''
    save_res = run_js(save_js)
    print("Save result:", save_res)
    time.sleep(3)
    print("Custom CSS updated successfully!")

if __name__ == '__main__':
    main()

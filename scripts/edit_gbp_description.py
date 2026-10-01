import subprocess
import time

def run_js(tab_id, js_code):
    escaped_js = js_code.replace('\\', '\\\\').replace('"', '\\"')
    apple_script = f'''
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if (id of t as text) is "{tab_id}" then
                    tell t
                        return execute javascript "{escaped_js}"
                    end tell
                end if
            end repeat
        end repeat
    end tell
    '''
    res = subprocess.run(["osascript", "-e", apple_script], capture_output=True, text=True)
    return res.stdout.strip()

tab_id = "1964394538"

click_save = '''
(function() {
    const btn = document.querySelector("button#fjaSBb") || document.querySelector("button[jsname='x8hlje']");
    if (!btn) return "NO_SAVE_BUTTON";
    
    // Check if enabled
    const disabled = btn.hasAttribute('disabled') || btn.getAttribute('aria-disabled') === 'true';
    if (disabled) return "BUTTON_DISABLED";
    
    btn.click();
    return "CLICKED_SAVE";
})()
'''

print("Click save:", run_js(tab_id, click_save))
time.sleep(3)

verify_js = '''
(function() {
    const sec = document.querySelector("section[data-row-id='13']");
    return JSON.stringify({
        hasTextarea: !!document.querySelector("textarea"),
        secText: sec ? sec.innerText.slice(0, 300) : "NO_SEC"
    });
})()
'''
print("Verification:", run_js(tab_id, verify_js))

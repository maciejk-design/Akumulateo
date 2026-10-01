import subprocess
import json

def run_chrome_js(tab_id, js_code):
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

tab_id = "1964394678"

inspect_all_btns = '''
(function() {
    const btns = Array.from(document.querySelectorAll("button[aria-label*='Page settings']")).map(b => b.getAttribute('aria-label'));
    return JSON.stringify(btns);
})()
'''

print(run_chrome_js(tab_id, inspect_all_btns))

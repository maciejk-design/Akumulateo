import subprocess
import json
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
time.sleep(2)

check_iframe = '''
(function() {
    const iframes = Array.from(document.querySelectorAll("iframe")).map(f => f.src);
    const inputs = Array.from(document.querySelectorAll("input, textarea, [contenteditable='true']")).map(i => ({
        tag: i.tagName,
        type: i.type,
        val: i.value,
        aria: i.getAttribute('aria-label')
    }));
    return JSON.stringify({
        iframes: iframes,
        inputs: inputs,
        bodyLen: document.body.innerText.length,
        bodySample: document.body.innerText.slice(0, 400)
    });
})()
'''
print(run_js(tab_id, check_iframe))

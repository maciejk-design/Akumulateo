import os
import sys
import json
import time
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNIPPET_PATH = os.path.join(BASE_DIR, "snippets", "squarespace", "obszar-dzialania-page-header-injection.html")

with open(SNIPPET_PATH, "r", encoding="utf-8") as f:
    injection_code = f.read()

print(f"Loaded injection for Obszar działania: {len(injection_code)} chars")

# Step 1: Create the JS payload file that will run in Chrome to set CodeMirror
code_json = json.dumps(injection_code)
escaped_code_expr = json.dumps(code_json)

payload_js = f"""
(function() {{
    var script = document.createElement('script');
    script.id = 'cm-injector-script';
    
    script.textContent = '(function() {{' +
        'try {{' +
        '    var cmEl = document.querySelector(\\'[role="dialog"] .CodeMirror\\');' +
        '    if (!cmEl || !cmEl.CodeMirror) {{' +
        '        document.documentElement.setAttribute(\\'data-deploy-result\\', JSON.stringify({{success: false, error: "no CodeMirror"}}));' +
        '        return;' +
        '    }}' +
        '    var cm = cmEl.CodeMirror;' +
        '    var code = ' + {escaped_code_expr} + ';' +
        '    cm.setValue(code);' +
        '    if (cm.save) cm.save();' +
        '    var ta = cmEl.querySelector("textarea");' +
        '    if (ta) {{' +
        '        ta.dispatchEvent(new Event("input", {{ bubbles: true }}));' +
        '        ta.dispatchEvent(new Event("change", {{ bubbles: true }}));' +
        '    }}' +
        '    document.documentElement.setAttribute(\\'data-deploy-result\\', JSON.stringify({{' +
        '        success: true,' +
        '        valueLength: cm.getValue().length,' +
        '        hasSaveBtn: !!document.querySelector(\\'[data-test="nav-modal-left-button"]\\')' +
        '    }}));' +
        '}} catch(e) {{' +
        '    document.documentElement.setAttribute(\\'data-deploy-result\\', JSON.stringify({{success: false, error: e.toString()}}));' +
        '}}' +
    '}})();';
    
    document.head.appendChild(script);
    script.remove();
    return document.documentElement.getAttribute('data-deploy-result');
}})();
"""

tmp_js_path = "/tmp/deploy_obszar.js"
with open(tmp_js_path, "w", encoding="utf-8") as f:
    f.write(payload_js)

# Step 2: Execute JS via AppleScript
as_code = f"""
set f to POSIX file "{tmp_js_path}"
set jsCode to read f as «class utf8»
tell application "Google Chrome"
    tell tab 7 of window 1
        set res to execute javascript jsCode
        return res
    end tell
end tell
"""

proc = subprocess.run(["osascript", "-e", as_code], capture_output=True, text=True)
print("Injection execution result:", proc.stdout.strip())
if proc.stderr:
    print("Error:", proc.stderr.strip())

res = json.loads(proc.stdout.strip())
if not res.get("success"):
    print("❌ Failed to set CodeMirror:", res)
    sys.exit(1)

print(f"✅ CodeMirror updated with {res['valueLength']} characters! Save button present: {res['hasSaveBtn']}")

# Step 3: Click Save
click_save_as = """
tell application "Google Chrome"
    tell tab 7 of window 1
        execute javascript "
        (function() {
            var saveBtn = document.querySelector('[data-test=\"nav-modal-left-button\"]');
            if (saveBtn) {
                saveBtn.click();
                return 'Clicked SAVE';
            }
            return 'No SAVE button found';
        })()
        "
    end tell
end tell
"""
proc_save = subprocess.run(["osascript", "-e", click_save_as], capture_output=True, text=True)
print("Save click result:", proc_save.stdout.strip())

# Step 4: Wait for save and verify
time.sleep(3)
check_as = """
tell application "Google Chrome"
    tell tab 7 of window 1
        execute javascript "
        (function() {
            var dialog = document.querySelector('[role=\"dialog\"]');
            var saveBtn = document.querySelector('[data-test=\"nav-modal-left-button\"]');
            return JSON.stringify({
                hasDialog: !!dialog,
                hasSaveBtn: !!saveBtn
            });
        })()
        "
    end tell
end tell
"""
proc_check = subprocess.run(["osascript", "-e", check_as], capture_output=True, text=True)
print("Dialog state after 3s:", proc_check.stdout.strip())

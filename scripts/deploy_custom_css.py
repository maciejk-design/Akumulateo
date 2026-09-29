import os
import sys
import json
import time
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSS_PATH = os.path.join(BASE_DIR, "snippets", "squarespace", "custom-css.css")

with open(CSS_PATH, "r", encoding="utf-8") as f:
    css_content = f.read()

print(f"Loaded Custom CSS: {len(css_content)} chars")

# Step 0: Ensure tab is on custom-css
nav_as = """
tell application "Google Chrome"
    tell tab 7 of window 1
        set URL to "https://celery-robin-sffx.squarespace.com/config/pages/custom-css"
    end tell
end tell
"""
subprocess.run(["osascript", "-e", nav_as])
time.sleep(3.5)

code_json = json.dumps(css_content)
escaped_code_expr = json.dumps(code_json)

payload_js = f"""
(function() {{
    var script = document.createElement("script");
    script.id = "cm-css-setter";
    
    script.textContent = "(function() {{" +
        "try {{" +
        "    var cmEl = document.querySelector(\x27.CodeMirror\x27);" +
        "    if (!cmEl || !cmEl.CodeMirror) {{" +
        "        document.documentElement.setAttribute(\x27data-deploy-result\x27, JSON.stringify({{success: false, error: \\"no CodeMirror\\" }}));" +
        "        return;" +
        "    }}" +
        "    var cm = cmEl.CodeMirror;" +
        "    var code = " + {escaped_code_expr} + ";" +
        "    cm.setValue(code);" +
        "    if (cm.save) cm.save();" +
        "    var ta = cmEl.querySelector(\\"textarea\\");" +
        "    if (ta) {{" +
        "        ta.dispatchEvent(new Event(\\"input\\", {{ bubbles: true }}));" +
        "        ta.dispatchEvent(new Event(\\"change\\", {{ bubbles: true }}));" +
        "    }}" +
        "    var saveBtn = Array.from(document.querySelectorAll(\\"button\\")).find(b => (b.innerText || \\"\\").trim().toUpperCase() === \\"SAVE\\");" +
        "    document.documentElement.setAttribute(\x27data-deploy-result\x27, JSON.stringify({{" +
        "        success: true," +
        "        valueLength: cm.getValue().length," +
        "        hasSaveBtn: !!saveBtn" +
        "    }}));" +
        "}} catch(e) {{" +
        "    document.documentElement.setAttribute(\x27data-deploy-result\x27, JSON.stringify({{success: false, error: e.toString() }}));" +
        "}}" +
    "}})();";
    
    document.head.appendChild(script);
    script.remove();
    return document.documentElement.getAttribute("data-deploy-result");
}})();
"""

tmp_js = "/tmp/inject_custom_css.js"
with open(tmp_js, "w", encoding="utf-8") as f:
    f.write(payload_js)

as_code = f"""
set f to POSIX file "{tmp_js}"
set jsCode to read f as «class utf8»
tell application "Google Chrome"
    tell tab 7 of window 1
        set res to execute javascript jsCode
        return res
    end tell
end tell
"""
proc = subprocess.run(["osascript", "-e", as_code], capture_output=True, text=True)
print("Inject result:", proc.stdout.strip())
res = json.loads(proc.stdout.strip())
if not res.get("success"):
    print("❌ Failed to set CSS in CodeMirror:", res)
    sys.exit(1)

time.sleep(1)

# Click Save
save_js = """(function() {
    var btn = Array.from(document.querySelectorAll("button")).find(b => (b.innerText || "").trim().toUpperCase() === "SAVE");
    if (!btn) return "NO_SAVE_BTN";
    var propsKey = Object.keys(btn).find(k => k.startsWith("__reactProps"));
    if (propsKey && btn[propsKey] && typeof btn[propsKey].onClick === "function") {
        btn[propsKey].onClick({ 
            preventDefault: function() {}, 
            stopPropagation: function() {},
            target: btn,
            currentTarget: btn
        });
        return "CLICKED_SAVE_REACT";
    }
    btn.click();
    return "FALLBACK_CLICKED_SAVE";
})();"""

with open("/tmp/save_custom_css.js", "w") as f:
    f.write(save_js)

as_save = """
set f to POSIX file "/tmp/save_custom_css.js"
set jsCode to read f as «class utf8»
tell application "Google Chrome"
    tell tab 7 of window 1
        set res to execute javascript jsCode
        return res
    end tell
end tell
"""
proc_save = subprocess.run(["osascript", "-e", as_save], capture_output=True, text=True)
print("Save click result:", proc_save.stdout.strip())

time.sleep(3)

# Check save button state (it disappears or disables when saved)
check_as = """
tell application "Google Chrome"
    tell tab 7 of window 1
        execute javascript "
        (function() {
            var saveBtn = Array.from(document.querySelectorAll('button')).find(b => (b.innerText || '').trim().toUpperCase() === 'SAVE');
            return JSON.stringify({
                hasSaveBtn: !!saveBtn
            });
        })()
        "
    end tell
end tell
"""
proc_check = subprocess.run(["osascript", "-e", check_as], capture_output=True, text=True)
print("Save button still present?:", proc_check.stdout.strip())
print("✅ Custom CSS deployed successfully!")

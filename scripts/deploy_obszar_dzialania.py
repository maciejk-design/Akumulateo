import os
import sys
import json
import time
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNIPPET_PATH = os.path.join(BASE_DIR, "snippets", "squarespace", "obszar-dzialania-page-header-injection.html")

with open(SNIPPET_PATH, "r", encoding="utf-8") as f:
    injection_code = f.read()

print(f"Loaded Obszar Działania injection: {len(injection_code)} chars")

# Step 1: Open Page Settings for Obszar działania (select the real page, index 1)
open_js = """(function() {
    var btns = Array.from(document.querySelectorAll('button')).filter(b => b.getAttribute('aria-label') === 'Page settings Obszar działania');
    if (btns.length >= 2) {
        btns[1].click();
        return 'CLICKED_PAGE_SETTINGS_INDEX_1';
    } else if (btns.length === 1) {
        btns[0].click();
        return 'CLICKED_PAGE_SETTINGS_INDEX_0';
    }
    return 'NOT_FOUND';
})();"""

with open("/tmp/open_obszar.js", "w") as f:
    f.write(open_js)

as_open = """
set f to POSIX file "/tmp/open_obszar.js"
set jsCode to read f as «class utf8»
tell application "Google Chrome"
    tell tab 7 of window 1
        set res to execute javascript jsCode
        return res
    end tell
end tell
"""
proc = subprocess.run(["osascript", "-e", as_open], capture_output=True, text=True)
print("Step 1 (Open Settings):", proc.stdout.strip())
time.sleep(2)

# Step 2: Click "Advanced" tab
click_adv_js = """(function() {
    var dialog = document.querySelector('[role="dialog"]');
    if (!dialog) return 'NO_DIALOG';
    var a = Array.from(dialog.querySelectorAll('a')).find(function(el) {
        return el.innerText && el.innerText.trim() === 'Advanced';
    });
    if (a) {
        a.click();
        return 'CLICKED_ADVANCED';
    }
    return 'ADVANCED_NOT_FOUND';
})();"""

with open("/tmp/click_adv_obszar.js", "w") as f:
    f.write(click_adv_js)

as_adv = """
set f to POSIX file "/tmp/click_adv_obszar.js"
set jsCode to read f as «class utf8»
tell application "Google Chrome"
    tell tab 7 of window 1
        set res to execute javascript jsCode
        return res
    end tell
end tell
"""
proc = subprocess.run(["osascript", "-e", as_adv], capture_output=True, text=True)
print("Step 2 (Click Advanced):", proc.stdout.strip())
time.sleep(2)

# Step 3: Inject code into CodeMirror
code_json = json.dumps(injection_code)
escaped_code_expr = json.dumps(code_json)

payload_js = f"""
(function() {{
    var script = document.createElement("script");
    script.id = "cm-obszar-script";
    
    script.textContent = "(function() {{" +
        "try {{" +
        "    var cmEl = document.querySelector(\x27[role=\\"dialog\\"] .CodeMirror\x27);" +
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
        "    document.documentElement.setAttribute(\x27data-deploy-result\x27, JSON.stringify({{" +
        "        success: true," +
        "        valueLength: cm.getValue().length," +
        "        hasSaveBtn: !!document.querySelector(\x27[data-test=\\"nav-modal-left-button\\"]\x27)" +
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

tmp_js = "/tmp/inject_obszar.js"
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
print("Step 3 (Inject to CodeMirror):", proc.stdout.strip())
res = json.loads(proc.stdout.strip())
if not res.get("success"):
    print("❌ Failed to inject code into Obszar działania:", res)
    sys.exit(1)

time.sleep(1)

# Step 4: Click Save via React onClick
save_js = """(function() {
    var btn = document.querySelector(\x27[data-test="nav-modal-left-button"]\x27);
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

with open("/tmp/save_obszar.js", "w") as f:
    f.write(save_js)

as_save = """
set f to POSIX file "/tmp/save_obszar.js"
set jsCode to read f as «class utf8»
tell application "Google Chrome"
    tell tab 7 of window 1
        set res to execute javascript jsCode
        return res
    end tell
end tell
"""
proc_save = subprocess.run(["osascript", "-e", as_save], capture_output=True, text=True)
print("Step 4 (Click Save):", proc_save.stdout.strip())

time.sleep(3)

# Step 5: Verify modal closed
proc_check = subprocess.run(["osascript", "-e", """
tell application "Google Chrome"
    tell tab 7 of window 1
        execute javascript "document.querySelector(\x27[role=dialog]\x27) !== null;"
    end tell
end tell
"""], capture_output=True, text=True)
print("Step 5 (Dialog still open?):", proc_check.stdout.strip())
print("✅ Obszar działania deployed successfully!")

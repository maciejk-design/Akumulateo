import os
import sys
import json
import time
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNIPPET_PATH = os.path.join(BASE_DIR, "snippets", "squarespace", "mokotow-page-header-injection.html")

with open(SNIPPET_PATH, "r", encoding="utf-8") as f:
    injection_code = f.read()

print(f"Loaded Mokotow injection: {len(injection_code)} chars")

# Step 1: Open Page Settings for Mokotow
open_as = """
tell application "Google Chrome"
    tell tab 7 of window 1
        execute javascript "
        (function() {
            var btn = document.querySelector('button[aria-label*=\"Page settings Wymiana akumulatora z dojazdem Warszawa Mokotów\"]');
            if (btn) {
                btn.click();
                return 'Clicked Mokotow Settings';
            }
            return 'Mokotow Settings button not found';
        })()
        "
    end tell
end tell
"""
proc = subprocess.run(["osascript", "-e", open_as], capture_output=True, text=True)
print("Step 1 (Open Settings):", proc.stdout.strip())
time.sleep(2)

# Step 2: Click "Advanced" tab
click_adv_as = """
tell application "Google Chrome"
    tell tab 7 of window 1
        execute javascript "
        (function() {
            var dialog = document.querySelector('[role=\"dialog\"]');
            if (!dialog) return 'No dialog';
            var a = Array.from(dialog.querySelectorAll('a')).find(function(el) {
                return el.innerText && el.innerText.trim() === 'Advanced';
            });
            if (a) {
                a.click();
                return 'Clicked Advanced';
            }
            return 'Advanced link not found';
        })()
        "
    end tell
end tell
"""
proc = subprocess.run(["osascript", "-e", click_adv_as], capture_output=True, text=True)
print("Step 2 (Click Advanced):", proc.stdout.strip())
time.sleep(2)

# Step 3: Inject code into CodeMirror
code_json = json.dumps(injection_code)
escaped_code_expr = json.dumps(code_json)

payload_js = f"""
(function() {{
    var script = document.createElement('script');
    script.id = 'cm-mokotow-script';
    
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

tmp_js_path = "/tmp/deploy_mokotow.js"
with open(tmp_js_path, "w", encoding="utf-8") as f:
    f.write(payload_js)

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
print("Step 3 (Inject to CodeMirror):", proc.stdout.strip())
res = json.loads(proc.stdout.strip())
if not res.get("success"):
    print("❌ Failed to inject code into Mokotow:", res)
    sys.exit(1)

time.sleep(1)

# Step 4: Click Save via React onClick
save_as = """
tell application "Google Chrome"
    tell tab 7 of window 1
        execute javascript "
        (function() {
            var s = document.createElement('script');
            s.textContent = `
                (function() {
                    try {
                        var btn = document.querySelector('[data-test=\"nav-modal-left-button\"]');
                        if (!btn) {
                            document.documentElement.setAttribute('data-save-res', 'no btn');
                            return;
                        }
                        var propsKey = Object.keys(btn).find(k => k.startsWith('__reactProps'));
                        if (propsKey && btn[propsKey] && typeof btn[propsKey].onClick === 'function') {
                            btn[propsKey].onClick({ 
                                preventDefault: function() {}, 
                                stopPropagation: function() {},
                                target: btn,
                                currentTarget: btn
                            });
                            document.documentElement.setAttribute('data-save-res', 'CALLED_ONCLICK');
                        } else {
                            btn.click();
                            document.documentElement.setAttribute('data-save-res', 'FALLBACK_CLICK');
                        }
                    } catch(e) {
                        document.documentElement.setAttribute('data-save-res', 'ERROR: ' + e.toString());
                    }
                })();
            `;
            document.head.appendChild(s);
            s.remove();
            return document.documentElement.getAttribute('data-save-res');
        })()
        "
    end tell
end tell
"""
proc = subprocess.run(["osascript", "-e", save_as], capture_output=True, text=True)
print("Step 4 (Click Save):", proc.stdout.strip())

# Step 5: Verify modal closed
time.sleep(3)
check_as = """
tell application "Google Chrome"
    tell tab 7 of window 1
        execute javascript "
        (function() {
            var dialog = document.querySelector('[role=\"dialog\"]');
            return JSON.stringify({
                hasDialog: !!dialog
            });
        })()
        "
    end tell
end tell
"""
proc = subprocess.run(["osascript", "-e", check_as], capture_output=True, text=True)
print("Step 5 (Check modal closed):", proc.stdout.strip())
print("✅ Mokotow deployed successfully!")

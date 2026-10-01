import subprocess
import time
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNIPPET_PATH = os.path.join(BASE_DIR, "snippets", "squarespace", "car-battery-replacement-warsaw-page-header-injection.html")

with open(SNIPPET_PATH, "r", encoding="utf-8") as f:
    injection_code = f.read()

win_idx, tab_idx = 1, 9

def run_js(code):
    tmp_path = "/tmp/run_sqs.js"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(code)
    as_code = f"""
set f to POSIX file "{tmp_path}"
set jsCode to read f as «class utf8»
tell application "Google Chrome"
    tell tab {tab_idx} of window {win_idx}
        return (execute javascript jsCode)
    end tell
end tell
"""
    res = subprocess.run(["osascript", "-e", as_code], capture_output=True, text=True)
    return res.stdout.strip()

print("1. Opening settings for Mobile Car Battery Replacement Warsaw 24/7...")
open_js = """(function() {
    var btns = Array.from(document.querySelectorAll("button[aria-label*='Page settings']"));
    var target = btns.find(b => b.getAttribute("aria-label").includes("Mobile Car Battery Replacement Warsaw 24/7"));
    if (target) {
        target.click();
        return "CLICKED_TARGET: " + target.getAttribute("aria-label");
    }
    return "TARGET_NOT_FOUND";
})();"""
print(run_js(open_js))
time.sleep(2.5)

print("2. Setting URL slug to 'car-battery-replacement-warsaw'...")
slug_js = """(function() {
    var res = {};
    var slugInput = document.querySelector('input[aria-label="URL Slug"]') || document.querySelector('input[name="urlId"]');
    if (slugInput) {
        var nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
        nativeSetter.call(slugInput, "car-battery-replacement-warsaw");
        slugInput.dispatchEvent(new Event("input", { bubbles: true }));
        slugInput.dispatchEvent(new Event("change", { bubbles: true }));
        res.slug = "UPDATED: " + slugInput.value;
    } else {
        res.slug = "NO_SLUG_INPUT";
    }
    return JSON.stringify(res);
})();"""
print(run_js(slug_js))
time.sleep(1.5)

print("3. Navigating to Advanced tab...")
adv_js = """(function() {
    var dialog = document.querySelector("[role=dialog]");
    if (!dialog) return "NO_DIALOG";
    var a = Array.from(dialog.querySelectorAll("a")).find(el => el.innerText && el.innerText.trim() === "Advanced");
    if (a) {
        a.click();
        return "CLICKED_ADVANCED";
    }
    return "ADV_NOT_FOUND";
})();"""
print(run_js(adv_js))
time.sleep(2)

print("4. Injecting code into CodeMirror...")
escaped_code = json.dumps(json.dumps(injection_code))
payload_js = f"""
(function() {{
    var script = document.createElement("script");
    script.id = "cm-district-script";
    script.textContent = "(function() {{" +
        "try {{" +
        "    var cmEl = document.querySelector(\\'[role=\\"dialog\\"] .CodeMirror\\');" +
        "    if (!cmEl || !cmEl.CodeMirror) {{" +
        "        document.documentElement.setAttribute(\\'data-deploy-result\\', JSON.stringify({{success: false, error: \\"no CodeMirror\\" }}));" +
        "        return;" +
        "    }}" +
        "    var cm = cmEl.CodeMirror;" +
        "    var code = " + {escaped_code} + ";" +
        "    cm.setValue(code);" +
        "    if (cm.save) cm.save();" +
        "    var ta = cmEl.querySelector(\\"textarea\\");" +
        "    if (ta) {{" +
        "        ta.dispatchEvent(new Event(\\"input\\", {{ bubbles: true }}));" +
        "        ta.dispatchEvent(new Event(\\"change\\", {{ bubbles: true }}));" +
        "    }}" +
        "    document.documentElement.setAttribute(\\'data-deploy-result\\', JSON.stringify({{" +
        "        success: true," +
        "        valueLength: cm.getValue().length," +
        "        hasSaveBtn: !!document.querySelector(\\'[data-test=\\"nav-modal-left-button\\"]\\')" +
        "    }}));" +
        "}} catch(e) {{" +
        "    document.documentElement.setAttribute(\\'data-deploy-result\\', JSON.stringify({{success: false, error: e.toString() }}));" +
        "}}" +
        "}})();";
    document.head.appendChild(script);
    script.remove();
    return document.documentElement.getAttribute("data-deploy-result");
}})();
"""
tmp_inject = "/tmp/inject_en.js"
with open(tmp_inject, "w", encoding="utf-8") as f:
    f.write(payload_js)

as_inject = f"""
set f to POSIX file "{tmp_inject}"
set jsCode to read f as «class utf8»
tell application "Google Chrome"
    tell tab {tab_idx} of window {win_idx}
        return (execute javascript jsCode)
    end tell
end tell
"""
res_inject = subprocess.run(["osascript", "-e", as_inject], capture_output=True, text=True).stdout.strip()
print("   Injection result:", res_inject)
time.sleep(1.5)

print("5. Clicking SAVE...")
save_js = """(function() {
    var btn = document.querySelector('[data-test="nav-modal-left-button"]');
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
print(run_js(save_js))
time.sleep(4)

print("6. Verifying dialog status...")
check_js = """(function() {
    var dialog = document.querySelector("[role=dialog]");
    return dialog ? "DIALOG_STILL_OPEN" : "DIALOG_CLOSED_SAVED";
})();"""
status = run_js(check_js)
print("   Status:", status)
if status == "DIALOG_STILL_OPEN":
    print("   Retrying save...")
    run_js(save_js)
    time.sleep(3)

print("7. Testing live URL via curl...")
live_url = "https://www.akumulateo.pl/car-battery-replacement-warsaw"
for attempt in range(8):
    proc = subprocess.run(["/usr/bin/curl", "-s", "-I", live_url], capture_output=True, text=True)
    first_line = proc.stdout.splitlines()[0] if proc.stdout else "No response"
    print(f"   Attempt {attempt+1}/8: {first_line}")
    if "200" in first_line:
        print("🎉 SUCCESS! https://www.akumulateo.pl/car-battery-replacement-warsaw is LIVE and returns HTTP 200!")
        break
    time.sleep(3)

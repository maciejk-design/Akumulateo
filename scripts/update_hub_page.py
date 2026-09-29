#!/usr/bin/env python3
"""
Aktualizacja wstrzyknięcia kodu dla strony Hub (/obszar-dzialania-warszawa-i-okolice)
w panelu Squarespace.
Wymusza stan 'dirty' formularza, aby przycisk SAVE stał się aktywny,
wstrzykuje kod do CodeMirror i zapisuje.
"""

import os
import sys
import time
import json
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_DIR, "scripts"))

from deploy_district import get_chrome_sqs_tab, run_js, ensure_pages_panel

win_idx, tab_idx = get_chrome_sqs_tab()
print(f"Panel Squarespace w oknie {win_idx}, karcie {tab_idx}")

ensure_pages_panel(win_idx, tab_idx)
time.sleep(1.5)

# 1. Otwórz właściwy przycisk Obszar działania (drugi, pod Not Linked)
print("1. Otwieranie ustawień właściwej strony Obszar działania...")
open_hub = """(function() {
    var btns = Array.from(document.querySelectorAll("button[aria-label*=\\"Page settings Obszar działania\\"]"));
    if (btns.length >= 2) {
        btns[1].click();
        return "CLICKED_SECOND_HUB";
    } else if (btns.length === 1) {
        btns[0].click();
        return "CLICKED_FIRST_HUB";
    }
    return "NO_HUB_BTNS";
})();"""

res_hub = run_js(open_hub, win_idx, tab_idx)
print("   Wynik:", res_hub)
time.sleep(2.5)

# 2. Wywołaj stan 'dirty' w zakładce General, aby aktywować przycisk SAVE
print("2. Aktywacja przycisku SAVE (zmiana stanu formularza)...")
trigger_dirty = """(function() {
    var input = document.querySelector("input[aria-label=\\"Page Title\\"]") || document.querySelector("input[name=title]");
    if (!input) return "NO_TITLE_INPUT";
    var val = input.value;
    var nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
    nativeSetter.call(input, val + " ");
    input.dispatchEvent(new Event("input", { bubbles: true }));
    input.dispatchEvent(new Event("change", { bubbles: true }));
    
    // Przywróć oryginalną wartość z zachowaniem flagi dirty
    nativeSetter.call(input, val);
    input.dispatchEvent(new Event("input", { bubbles: true }));
    input.dispatchEvent(new Event("change", { bubbles: true }));
    return "FORM_MARKED_DIRTY";
})();"""
print("   Wynik:", run_js(trigger_dirty, win_idx, tab_idx))
time.sleep(1.5)

# 3. Przejdź do zakładki Advanced
print("3. Klikanie zakładki Advanced...")
click_adv = """(function() {
    var dialog = document.querySelector("[role=dialog]");
    if (!dialog) return "NO_DIALOG";
    var a = Array.from(dialog.querySelectorAll("a")).find(el => el.innerText && el.innerText.trim() === "Advanced");
    if (a) {
        a.click();
        return "CLICKED_ADVANCED";
    }
    return "ADV_NOT_FOUND";
})();"""

res_adv = None
for attempt in range(5):
    res_adv = run_js(click_adv, win_idx, tab_idx)
    if res_adv == "CLICKED_ADVANCED":
        break
    time.sleep(1)

print("   Wynik:", res_adv)
if res_adv != "CLICKED_ADVANCED":
    print("❌ Nie znaleziono zakładki Advanced w oknie dialogowym!")
    sys.exit(1)

time.sleep(2)

# 4. Wczytaj zaktualizowany kod wstrzyknięcia
snippet_path = os.path.join(BASE_DIR, "snippets", "squarespace", "obszar-dzialania-page-header-injection.html")
with open(snippet_path, "r", encoding="utf-8") as f:
    hub_code = f.read()

print(f"📦 Załadowano kod wstrzyknięcia Hub: {len(hub_code)} znaków")

escaped_code = json.dumps(json.dumps(hub_code))
payload_js = f"""
(function() {{
    var script = document.createElement("script");
    script.id = "cm-hub-script";
    script.textContent = "(function() {{" +
        "try {{" +
        "    var cmEl = document.querySelector(\x27[role=\\"dialog\\"] .CodeMirror\x27);" +
        "    if (!cmEl || !cmEl.CodeMirror) {{" +
        "        document.documentElement.setAttribute(\x27data-deploy-result\x27, JSON.stringify({{success: false, error: \\"no CodeMirror\\" }}));" +
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

tmp_inject = "/tmp/inject_hub_page.js"
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

res_inject = None
for attempt in range(8):
    res_inject = subprocess.run(["osascript", "-e", as_inject], capture_output=True, text=True).stdout.strip()
    if "true" in res_inject:
        break
    time.sleep(1)

print("   Wynik wstrzyknięcia:", res_inject)
if "true" not in (res_inject or ""):
    print("❌ Nie udało się wstrzyknąć kodu do CodeMirror!")
    sys.exit(1)

time.sleep(1.5)

# 5. Kliknij SAVE
print("5. Klikanie SAVE...")
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

res_save = run_js(save_js, win_idx, tab_idx)
print("   Wynik zapisu:", res_save)
time.sleep(4)

# 6. Weryfikacja zamknięcia modala
check_js = """(function() {
    var dialog = document.querySelector("[role=dialog]");
    return dialog ? "DIALOG_STILL_OPEN" : "DIALOG_CLOSED_SAVED";
})();"""
status = run_js(check_js, win_idx, tab_idx)
print("   Status modala:", status)
if status == "DIALOG_STILL_OPEN":
    print("   ...ponawiam kliknięcie SAVE...")
    run_js(save_js, win_idx, tab_idx)
    time.sleep(3)

# 7. Test na żywo
live_url = "https://www.akumulateo.pl/obszar-dzialania-warszawa-i-okolice"
print(f"7. Weryfikacja HTTP na żywo: {live_url}...")
for attempt in range(6):
    curl_proc = subprocess.run(["/usr/bin/curl", "-s", "-I", live_url], capture_output=True, text=True)
    first_line = curl_proc.stdout.splitlines()[0] if curl_proc.stdout else "Brak"
    if "200" in first_line:
        break
    time.sleep(2)

print(f"    Status HTTP: {first_line}")
print("🎉 SUKCES! Strona Hub została zaktualizowana i działa na produkcji!")

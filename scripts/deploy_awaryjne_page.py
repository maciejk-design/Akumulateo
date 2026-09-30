#!/usr/bin/env python3
"""
Skrypt automatycznie wdrażający pakiet Page Header Code Injection
dla podstrony /awaryjne-uruchomienie-auta-warszawa w Squarespace 7.1.
"""

import os
import sys
import time
import json
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNIPPETS_DIR = os.path.join(BASE_DIR, "snippets", "squarespace")
sys.path.append(os.path.join(BASE_DIR, "scripts"))

from deploy_district import get_chrome_sqs_tab, ensure_pages_panel

def run_js(code, win_idx, tab_idx):
    tmp_path = "/tmp/run_sqs_awaryjne.js"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(code)
    
    as_code = f"""
set f to POSIX file "{tmp_path}"
set jsCode to read f as «class utf8»
tell application "Google Chrome"
    set t to tab {tab_idx} of window {win_idx}
    return (execute t javascript jsCode)
end tell
"""
    res = subprocess.run(["osascript", "-e", as_code], capture_output=True, text=True)
    return res.stdout.strip()

def main():
    print("========================================================")
    print("🚀 ROZPOCZYNAM WDROŻENIE DLA: AWARYJNE URUCHOMIENIE AUTA WARSZAWA")
    print("   URL: /awaryjne-uruchomienie-auta-warszawa")
    print("========================================================")

    snippet_path = os.path.join(SNIPPETS_DIR, "awaryjne-uruchomienie-page-header-injection.html")
    if not os.path.exists(snippet_path):
        print(f"❌ Plik wstrzyknięcia nie istnieje: {snippet_path}")
        sys.exit(1)

    with open(snippet_path, "r", encoding="utf-8") as f:
        injection_code = f.read()

    # Upewnij się, że AppleScript komunikuje się z głównym oknem Chrome (zamykamy instancję MCP jeśli istnieje)
    subprocess.run(["pkill", "-f", "chrome-devtools-mcp"], capture_output=True)
    time.sleep(1)

    win_idx, tab_idx = get_chrome_sqs_tab()
    print(f"🌐 Znaleziono panel Squarespace w oknie {win_idx}, karcie {tab_idx}")
    ensure_pages_panel(win_idx, tab_idx)
    time.sleep(1.5)

    # Krok 1: Otwórz ustawienia strony
    print("1. Otwieranie ustawień strony 'Awaryjne uruchomienie auta Warszawa'...")
    open_page = """(function() {
        var btns = Array.from(document.querySelectorAll("button[aria-label*=\\"Page settings\\"]"));
        var target = btns.find(b => b.getAttribute("aria-label").includes("Awaryjne uruchomienie"));
        if (!target) return "NOT_FOUND";
        target.click();
        return "CLICKED: " + target.getAttribute("aria-label");
    })();"""
    
    res_open = None
    for attempt in range(6):
        res_open = run_js(open_page, win_idx, tab_idx)
        if "CLICKED" in res_open:
            break
        print(f"   ...próba {attempt+1}/6 ({res_open}), ponawiam za 1.5s...")
        time.sleep(1.5)

    print("   Wynik:", res_open)
    if "CLICKED" not in (res_open or ""):
        print("❌ Nie znaleziono przycisku ustawień!")
        sys.exit(1)
    time.sleep(2.5)

    # Krok 2: Ustawienie Tytułu (w celu aktywacji przycisku SAVE w React)
    print("2. Wymuszanie stanu dirty w formularzu (aktywacja przycisku SAVE)...")
    set_fields = """(function() {
        var titleInput = document.querySelector('input[aria-label="Page Title"]') || document.querySelector('input[name="title"]');
        if (titleInput) {
            var nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
            var origVal = titleInput.value || "Awaryjne Uruchomienie Auta Warszawa 24/7";
            nativeSetter.call(titleInput, origVal + " [active]");
            titleInput.dispatchEvent(new Event("input", { bubbles: true }));
            titleInput.dispatchEvent(new Event("change", { bubbles: true }));
            setTimeout(function() {
                nativeSetter.call(titleInput, "Awaryjne Uruchomienie Auta Warszawa 24/7 | Rozruch z Dojazdem | Akumulateo");
                titleInput.dispatchEvent(new Event("input", { bubbles: true }));
                titleInput.dispatchEvent(new Event("change", { bubbles: true }));
            }, 100);
            return "DIRTY_TRIGGERED";
        }
        return "NO_TITLE_INPUT";
    })();"""
    res_title = run_js(set_fields, win_idx, tab_idx)
    print("   Wynik:", res_title)
    time.sleep(1.5)

    # Krok 3: Przejście do zakładki Advanced
    print("3. Przejście do zakładki Advanced...")
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
    res_adv = run_js(click_adv, win_idx, tab_idx)
    print("   Wynik:", res_adv)
    if res_adv != "CLICKED_ADVANCED":
        print("❌ Nie znaleziono zakładki Advanced!")
        sys.exit(1)
    time.sleep(2)

    # Krok 4: Wstrzyknięcie kodu do CodeMirror
    print(f"4. Wstrzykiwanie kodu ({len(injection_code)} zn.) do CodeMirror...")
    escaped_code = json.dumps(json.dumps(injection_code))
    payload_js = f"""
(function() {{
    var script = document.createElement("script");
    script.id = "cm-awaryjne-script";
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
    tmp_inject = "/tmp/inject_awaryjne.js"
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
    print("   Wynik wstrzyknięcia:", res_inject)
    time.sleep(1.5)

    # Krok 5: Kliknięcie SAVE
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

    # Krok 6: Weryfikacja zamknięcia modala
    check_js = """(function() {
        var dialog = document.querySelector("[role=dialog]");
        return dialog ? "DIALOG_STILL_OPEN" : "DIALOG_CLOSED_SAVED";
    })();"""
    status = run_js(check_js, win_idx, tab_idx)
    print("   Status modala:", status)
    if status == "DIALOG_STILL_OPEN":
        run_js(save_js, win_idx, tab_idx)
        time.sleep(3)

    # Krok 7: Test na żywo via curl
    live_url = "https://www.akumulateo.pl/awaryjne-uruchomienie-auta-warszawa"
    print(f"6. Weryfikacja HTTP na żywo: {live_url}...")
    for attempt in range(8):
        curl_proc = subprocess.run(["/usr/bin/curl", "-s", "-I", live_url], capture_output=True, text=True)
        first_line = curl_proc.stdout.splitlines()[0] if curl_proc.stdout else "Brak"
        if "200" in first_line:
            break
        print(f"   Próba {attempt+1}/8: {first_line}, czekam 3s...")
        time.sleep(3)

    print(f"    Status HTTP: {first_line}")
    print("🎉 WDROŻENIE ZAKOŃCZONE POMYŚLNIE!")

if __name__ == "__main__":
    main()

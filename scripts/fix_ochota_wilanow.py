#!/usr/bin/env python3
"""
Konfiguruje dwie istniejące zduplikowane strony w Squarespace na:
1. Ochota (wymiana-akumulatora-warszawa-ochota)
2. Wilanów (wymiana-akumulatora-warszawa-wilanow)
"""

import os
import sys
import time
import json
import subprocess

from deploy_district import get_chrome_sqs_tab, run_js, ensure_pages_panel

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNIPPETS_DIR = os.path.join(BASE_DIR, "snippets", "squarespace")

def configure_copy_page(target_name, title, slug, snippet_path):
    print(f"\n========================================================")
    print(f"🔧 KONFIGURACJA STRONY DLA: {target_name.upper()}")
    print(f"   Slug: /{slug}")
    print(f"========================================================")
    
    win_idx, tab_idx = get_chrome_sqs_tab()
    ensure_pages_panel(win_idx, tab_idx)
    time.sleep(1.5)
    
    with open(snippet_path, "r", encoding="utf-8") as f:
        injection_code = f.read()

    # Krok 1: Kliknij pierwszy dostępny przycisk z (Copy)
    print("1. Otwieranie ustawień zduplikowanej strony (Copy)...")
    open_copy = """(function() {
        var copyBtns = Array.from(document.querySelectorAll("button[aria-label*=\\"Page settings\\"]")).filter(b => b.getAttribute("aria-label").includes("Copy") || b.getAttribute("aria-label").includes("Kopia"));
        if (!copyBtns.length) return "NO_COPY_BTNS";
        copyBtns[0].click();
        return "CLICKED_COPY: " + copyBtns[0].getAttribute("aria-label");
    })();"""
    
    res_open = run_js(open_copy, win_idx, tab_idx)
    print("   Wynik:", res_open)
    if "CLICKED_COPY" not in res_open:
        print("❌ Nie znaleziono przycisku z (Copy)!")
        return False
    time.sleep(2.5)

    # Krok 2: Ustaw Page Title, Navigation Title i URL Slug
    print(f"2. Aktualizacja tytułów i URL Slug na: '{slug}'...")
    escaped_title = json.dumps(title)
    escaped_slug = json.dumps(slug)
    set_fields = f"""(function() {{
        var res = {{}};
        var titleInput = document.querySelector('input[aria-label="Page Title"]') || document.querySelector('input[name="title"]');
        if (titleInput) {{
            var nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
            nativeSetter.call(titleInput, {escaped_title});
            titleInput.dispatchEvent(new Event("input", {{ bubbles: true }}));
            titleInput.dispatchEvent(new Event("change", {{ bubbles: true }}));
            res.title = "UPDATED";
        }}
        var navTitleInput = document.querySelector('input[aria-label="Navigation Title"]') || document.querySelector('input[name="navigationTitle"]');
        if (navTitleInput) {{
            var nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
            nativeSetter.call(navTitleInput, {escaped_title});
            navTitleInput.dispatchEvent(new Event("input", {{ bubbles: true }}));
            navTitleInput.dispatchEvent(new Event("change", {{ bubbles: true }}));
            res.navTitle = "UPDATED";
        }}
        var slugInput = document.querySelector('input[aria-label="URL Slug"]') || document.querySelector('input[name="urlId"]');
        if (slugInput) {{
            var nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
            nativeSetter.call(slugInput, {escaped_slug});
            slugInput.dispatchEvent(new Event("input", {{ bubbles: true }}));
            slugInput.dispatchEvent(new Event("change", {{ bubbles: true }}));
            res.slug = "UPDATED: " + slugInput.value;
        }} else {{
            res.slug = "NO_SLUG_INPUT";
        }}
        return JSON.stringify(res);
    }})();"""
    res_fields = run_js(set_fields, win_idx, tab_idx)
    print("   Wynik:", res_fields)
    time.sleep(1.5)

    # Krok 3: Kliknij zakładkę Advanced
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
    time.sleep(2)

    # Krok 4: Wstrzyknij kod do CodeMirror
    print("4. Wstrzykiwanie kodu do CodeMirror...")
    escaped_code = json.dumps(json.dumps(injection_code))
    payload_js = f"""
(function() {{
    var script = document.createElement("script");
    script.id = "cm-fix-script";
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
    tmp_inject = f"/tmp/inject_fix_{slug}.js"
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

    # Krok 5: Kliknij SAVE
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

    # Krok 6: Sprawdź zamknięcie okna
    check_js = """(function() {
        var dialog = document.querySelector("[role=dialog]");
        return dialog ? "DIALOG_STILL_OPEN" : "DIALOG_CLOSED_SAVED";
    })();"""
    status = run_js(check_js, win_idx, tab_idx)
    print("   Status modala:", status)
    if status == "DIALOG_STILL_OPEN":
        run_js(save_js, win_idx, tab_idx)
        time.sleep(3)

    # Krok 7: Test na żywo
    live_url = f"https://www.akumulateo.pl/{slug}"
    print(f"6. Weryfikacja HTTP na żywo: {live_url}...")
    for attempt in range(8):
        curl_proc = subprocess.run(["/usr/bin/curl", "-s", "-I", live_url], capture_output=True, text=True)
        first_line = curl_proc.stdout.splitlines()[0] if curl_proc.stdout else "Brak"
        if "200" in first_line:
            break
        print(f"   Próba {attempt+1}/8: {first_line}, czekam 3s...")
        time.sleep(3)

    print(f"    Status HTTP końcowy: {first_line}")
    return "200" in first_line

def main():
    # 1. Ochota
    ochota_snippet = os.path.join(SNIPPETS_DIR, "ochota-page-header-injection.html")
    configure_copy_page(
        "Ochota",
        "Wymiana Akumulatora z Dojazdem Warszawa Ochota 24/7 | Akumulateo",
        "wymiana-akumulatora-warszawa-ochota",
        ochota_snippet
    )
    time.sleep(3)

    # 2. Wilanów
    wilanow_snippet = os.path.join(SNIPPETS_DIR, "wilanow-page-header-injection.html")
    configure_copy_page(
        "Wilanów",
        "Wymiana Akumulatora Miasteczko Wilanów 24/7 | Kodowanie BMS AGM",
        "wymiana-akumulatora-warszawa-wilanow",
        wilanow_snippet
    )

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Konfiguruje podstrony Marki i Wołomin w Squarespace.
"""

import os
import sys
import time
import json
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SNIPPETS_DIR = os.path.join(BASE_DIR, "snippets", "squarespace")
sys.path.append(os.path.join(BASE_DIR, "scripts"))

from deploy_district import get_chrome_sqs_tab, run_js, ensure_pages_panel

def configure_page_by_label(search_label, slug, snippet_path):
    print(f"\n========================================================")
    print(f"🔧 KONFIGURACJA STRONY: {search_label.upper()}")
    print(f"   Slug: /{slug}")
    print(f"========================================================")
    
    win_idx, tab_idx = get_chrome_sqs_tab()
    ensure_pages_panel(win_idx, tab_idx)
    time.sleep(1.5)
    
    with open(snippet_path, "r", encoding="utf-8") as f:
        injection_code = f.read()

    # Krok 1: Kliknij przycisk ustawień danej strony
    print(f"1. Otwieranie ustawień strony ({search_label})...")
    escaped_label = json.dumps(search_label)
    open_page = f"""(function() {{
        var btns = Array.from(document.querySelectorAll("button[aria-label*=\\"Page settings\\"]"));
        var target = btns.find(b => b.getAttribute("aria-label").includes({escaped_label}));
        if (!target) return "NOT_FOUND";
        target.click();
        return "CLICKED: " + target.getAttribute("aria-label");
    }})();"""
    
    res_open = run_js(open_page, win_idx, tab_idx)
    print("   Wynik:", res_open)
    if "CLICKED" not in res_open:
        print("❌ Nie znaleziono przycisku ustawień!")
        return False
    time.sleep(2.5)

    # Krok 2: Ustaw URL Slug
    print(f"2. Aktualizacja URL Slug na: '{slug}'...")
    escaped_slug = json.dumps(slug)
    set_fields = f"""(function() {{
        var res = {{}};
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
    # 1. Marki
    marki_snippet = os.path.join(SNIPPETS_DIR, "marki-page-header-injection.html")
    configure_page_by_label("Marki", "wymiana-akumulatora-marki", marki_snippet)
    time.sleep(3)

    # 2. Wołomin
    wolomin_snippet = os.path.join(SNIPPETS_DIR, "wolomin-page-header-injection.html")
    configure_page_by_label("Wołomin", "wymiana-akumulatora-wolomin", wolomin_snippet)

if __name__ == "__main__":
    main()

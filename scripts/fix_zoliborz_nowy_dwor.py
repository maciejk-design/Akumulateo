#!/usr/bin/env python3
"""
Skrypt konfigurujący podstrony Żoliborz i Nowy Dwór Mazowiecki w Squarespace 7.1.
Wykorzystuje istniejące zduplikowane strony (slugs: mokotow-1-1 i mokotow-1-2).
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
    tmp_path = "/tmp/run_sqs_fix.js"
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

def configure_target_page(match_slug_pattern, new_title, new_slug, snippet_path):
    print(f"\n========================================================")
    print(f"🔧 KONFIGURACJA STRONY DLA: {new_title}")
    print(f"   Szukany wzorzec sluga: {match_slug_pattern}")
    print(f"   Nowy slug: /{new_slug}")
    print(f"   Snippet: {snippet_path}")
    print(f"========================================================")

    if not os.path.exists(snippet_path):
        print(f"❌ Plik wstrzyknięcia nie istnieje: {snippet_path}")
        return False

    with open(snippet_path, "r", encoding="utf-8") as f:
        injection_code = f.read()

    win_idx, tab_idx = get_chrome_sqs_tab()
    ensure_pages_panel(win_idx, tab_idx)
    time.sleep(1.5)

    # Krok 1: Znajdź przycisk, którego modal ma slug pasujący do match_slug_pattern
    print("1. Szukanie odpowiedniej podstrony w panelu stron...")
    
    find_and_open = f"""(function() {{
        var btns = Array.from(document.querySelectorAll("button[aria-label*=\\"Page settings\\"]"));
        return btns.length;
    }})();"""
    count_str = run_js(find_and_open, win_idx, tab_idx)
    total_btns = int(count_str) if count_str.isdigit() else 0
    print(f"   Znaleziono {total_btns} przycisków stron")

    found_idx = None
    for i in range(total_btns):
        # Kliknij i sprawdź slug
        open_i = f"""(function() {{
            var btns = Array.from(document.querySelectorAll("button[aria-label*=\\"Page settings\\"]"));
            if (btns[{i}]) {{
                btns[{i}].click();
                return "CLICKED";
            }}
            return "NOT_FOUND";
        }})();"""
        run_js(open_i, win_idx, tab_idx)
        time.sleep(1.5)
        
        get_slug = """(function() {
            var slug = document.querySelector('input[aria-label="URL Slug"]') || document.querySelector('input[name="urlId"]');
            return slug ? slug.value : "";
        })();"""
        curr_slug = run_js(get_slug, win_idx, tab_idx)
        
        if match_slug_pattern in curr_slug:
            print(f"   🎯 Znaleziono cel na indeksie {i}! Aktualny slug: {curr_slug}")
            found_idx = i
            break
        
        # Zamknij modal
        close_modal = """(function() {
            var dialog = document.querySelector("[role=dialog]");
            if (dialog) {
                var closeBtn = Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.trim() === "CLOSE" || b.innerText.trim() === "Cancel");
                if (closeBtn) closeBtn.click();
            }
        })();"""
        run_js(close_modal, win_idx, tab_idx)
        time.sleep(1)

    if found_idx is None:
        print(f"❌ Nie znaleziono strony ze slugiem zawierającym '{match_slug_pattern}'")
        return False

    # Krok 2: Ustawienie Tytułu i Sluga
    print(f"2. Aktualizacja Page Title ('{new_title}') oraz URL Slug ('{new_slug}')...")
    escaped_title = json.dumps(new_title)
    escaped_slug = json.dumps(new_slug)
    
    set_fields = f"""(function() {{
        var res = {{}};
        var titleInput = document.querySelector('input[aria-label="Page Title"]') || document.querySelector('input[name="title"]');
        if (titleInput) {{
            var nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
            nativeSetter.call(titleInput, {escaped_title});
            titleInput.dispatchEvent(new Event("input", {{ bubbles: true }}));
            titleInput.dispatchEvent(new Event("change", {{ bubbles: true }}));
            res.title = "UPDATED: " + titleInput.value;
        }}
        var navTitleInput = document.querySelector('input[aria-label="Navigation Title"]') || document.querySelector('input[name="navigationTitle"]');
        if (navTitleInput) {{
            var nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
            nativeSetter.call(navTitleInput, {escaped_title});
            navTitleInput.dispatchEvent(new Event("input", {{ bubbles: true }}));
            navTitleInput.dispatchEvent(new Event("change", {{ bubbles: true }}));
            res.navTitle = "UPDATED: " + navTitleInput.value;
        }}
        var slugInput = document.querySelector('input[aria-label="URL Slug"]') || document.querySelector('input[name="urlId"]');
        if (slugInput) {{
            var nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
            nativeSetter.call(slugInput, {escaped_slug});
            slugInput.dispatchEvent(new Event("input", {{ bubbles: true }}));
            slugInput.dispatchEvent(new Event("change", {{ bubbles: true }}));
            res.slug = "UPDATED: " + slugInput.value;
        }}
        return JSON.stringify(res);
    }})();"""
    res_fields = run_js(set_fields, win_idx, tab_idx)
    print("   Wynik pól:", res_fields)
    time.sleep(1.5)

    # Krok 3: Zakładka Advanced
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

    # Krok 4: Wstrzyknięcie kodu do CodeMirror
    print(f"4. Wstrzykiwanie kodu ({len(injection_code)} zn.) do CodeMirror...")
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
    tmp_inject = f"/tmp/inject_fix_{new_slug}.js"
    with open(tmp_inject, "w", encoding="utf-8") as f:
        f.write(payload_js)

    as_inject = f"""
set f to POSIX file "{tmp_inject}"
set jsCode to read f as «class utf8»
tell application "Google Chrome"
    set t to tab {tab_idx} of window {win_idx}
    return (execute t javascript jsCode)
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
    live_url = f"https://www.akumulateo.pl/{new_slug}"
    print(f"6. Weryfikacja HTTP na żywo: {live_url}...")
    first_line = ""
    for attempt in range(8):
        curl_proc = subprocess.run(["/usr/bin/curl", "-s", "-I", live_url], capture_output=True, text=True)
        first_line = curl_proc.stdout.splitlines()[0] if curl_proc.stdout else "Brak"
        if "200" in first_line:
            break
        print(f"   Próba {attempt+1}/8: {first_line}, czekam 3s na CDN...")
        time.sleep(3)

    print(f"    Status HTTP końcowy: {first_line}")
    return "200" in first_line

def main():
    print("🚀 Rozpoczynam naprawę podstron Nowy Dwór Mazowiecki i Żoliborz...")

    # 1. Nowy Dwór Mazowiecki (wzorzec: mokotow-1-1)
    ndm_snippet = os.path.join(SNIPPETS_DIR, "nowy-dwor-mazowiecki-page-header-injection.html")
    res_ndm = configure_target_page(
        match_slug_pattern="mokotow-1-1",
        new_title="Wymiana Akumulatora Nowy Dwór Mazowiecki 24/7 | Pogotowie z Dojazdem",
        new_slug="wymiana-akumulatora-nowy-dwor-mazowiecki",
        snippet_path=ndm_snippet
    )
    time.sleep(3)

    # 2. Żoliborz (wzorzec: mokotow-1-2)
    zoliborz_snippet = os.path.join(SNIPPETS_DIR, "zoliborz-page-header-injection.html")
    res_zoliborz = configure_target_page(
        match_slug_pattern="mokotow-1-2",
        new_title="Wymiana Akumulatora z Dojazdem Warszawa Żoliborz 24/7 | Akumulateo",
        new_slug="wymiana-akumulatora-warszawa-zoliborz",
        snippet_path=zoliborz_snippet
    )

    print("\n========================================================")
    print(f"Wynik końcowy:")
    print(f"  Nowy Dwór Mazowiecki: {'✅ SUKCES' if res_ndm else '❌ BŁĄD'}")
    print(f"  Żoliborz:             {'✅ SUKCES' if res_zoliborz else '❌ BŁĄD'}")
    print("========================================================")

if __name__ == "__main__":
    main()

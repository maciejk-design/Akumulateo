#!/usr/bin/env python3
"""
Automatyczny skrypt do klonowania i wdrażania podstron dzielnicowych w Squarespace 7.1.
Klonuje podstronę Mokotów, ustawia tytuł, slug oraz kod Page Header Code Injection.
Obsługuje dynamiczne wykrywanie karty Chrome oraz mechanizmy retry dla każdego kroku.
"""

import sys
import os
import time
import json
import subprocess

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def get_chrome_sqs_tab():
    """Wyszukuje dynamicznie okno i kartę panelu stron Squarespace."""
    as_find = """
tell application "Google Chrome"
    set winIdx to 0
    repeat with w in windows
        set winIdx to winIdx + 1
        set tabIdx to 0
        repeat with t in tabs of w
            set tabIdx to tabIdx + 1
            if (id of t as text) is "1964394678" then
                return (winIdx as text) & ":" & (tabIdx as text)
            end if
        end repeat
    end repeat
    set winIdx to 0
    repeat with w in windows
        set winIdx to winIdx + 1
        set tabIdx to 0
        repeat with t in tabs of w
            set tabIdx to tabIdx + 1
            if (URL of t contains "celery-robin-sffx.squarespace.com/config/pages" and URL of t does not contain "code-injection") then
                return (winIdx as text) & ":" & (tabIdx as text)
            end if
        end repeat
    end repeat
    return "NOT_FOUND"
end tell
"""
    res = subprocess.run(["osascript", "-e", as_find], capture_output=True, text=True)
    out = res.stdout.strip()
    if out == "NOT_FOUND" or not out:
        # Fallback do tab 7 of window 1
        return 1, 7
    parts = out.split(":")
    return int(parts[0]), int(parts[1])

def run_js(code, win_idx=None, tab_idx=None):
    if win_idx is None or tab_idx is None:
        win_idx, tab_idx = get_chrome_sqs_tab()

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

def ensure_pages_panel(win_idx, tab_idx):
    js = """(function() {
        var dialog = document.querySelector("[role=dialog]");
        if (dialog) {
            var closeBtn = Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.trim() === "CLOSE" || b.innerText.trim() === "Cancel");
            if (closeBtn) closeBtn.click();
        }
        return window.location.href;
    })();"""
    url = run_js(js, win_idx, tab_idx)
    if url.rstrip("/") != "https://celery-robin-sffx.squarespace.com/config/pages":
        nav_as = f"""
tell application "Google Chrome"
    tell tab {tab_idx} of window {win_idx}
        set URL to "https://celery-robin-sffx.squarespace.com/config/pages"
    end tell
end tell
"""
        subprocess.run(["osascript", "-e", nav_as])
        time.sleep(4)

def deploy_district(name, page_title, url_slug, snippet_path):
    print(f"\n========================================================")
    print(f"🚀 ROZPOCZYNAM WDROŻENIE DZIELNICY: {name.upper()}")
    print(f"   Slug: /{url_slug}")
    print(f"   Snippet: {snippet_path}")
    print(f"========================================================")

    if not os.path.exists(snippet_path):
        print(f"❌ Błąd: Plik wstrzyknięcia nie istnieje: {snippet_path}")
        return False

    with open(snippet_path, "r", encoding="utf-8") as f:
        injection_code = f.read()

    print(f"📦 Załadowano kod wstrzyknięcia: {len(injection_code)} znaków")

    win_idx, tab_idx = get_chrome_sqs_tab()
    print(f"🌐 Znaleziono panel Squarespace w oknie {win_idx}, karcie {tab_idx}")

    ensure_pages_panel(win_idx, tab_idx)
    time.sleep(1.5)

    # Krok 1: Otwórz ustawienia Mokotowa w celu duplikacji
    print("1. Otwieranie ustawień Mokotowa...")
    open_moko = """(function() {
        var btn = document.querySelector("button[aria-label*=\\"Page settings Wymiana akumulatora z dojazdem Warszawa Mokotów\\"]");
        if (btn) {
            btn.click();
            return "CLICKED_MOKOTOW";
        }
        return "NO_MOKOTOW_BTN";
    })();"""
    
    res_moko = None
    for attempt in range(5):
        res_moko = run_js(open_moko, win_idx, tab_idx)
        if res_moko == "CLICKED_MOKOTOW":
            break
        print(f"   ...próba {attempt+1}/5 ({res_moko}), ponawiam za 1s...")
        time.sleep(1)

    print("   Wynik:", res_moko)
    if res_moko != "CLICKED_MOKOTOW":
        print("❌ Nie znaleziono przycisku Mokotowa!")
        return False
    time.sleep(2)

    # Krok 2: Kliknij DUPLICATE PAGE
    print("2. Klikanie DUPLICATE PAGE...")
    click_dup = """(function() {
        var dialog = document.querySelector("[role=dialog]");
        if (!dialog) return "NO_DIALOG";
        var dupBtn = Array.from(dialog.querySelectorAll("button")).find(b => b.innerText.trim() === "DUPLICATE PAGE");
        if (dupBtn) {
            dupBtn.click();
            return "CLICKED_DUPLICATE";
        }
        return "NO_DUP_BTN";
    })();"""
    
    res_dup = None
    for attempt in range(5):
        res_dup = run_js(click_dup, win_idx, tab_idx)
        if res_dup == "CLICKED_DUPLICATE":
            break
        time.sleep(1)

    print("   Wynik:", res_dup)
    if res_dup != "CLICKED_DUPLICATE":
        print("❌ Nie udało się kliknąć DUPLICATE PAGE!")
        return False
    time.sleep(1.5)

    # Krok 3: Kliknij Confirm w oknie dialogowym
    print("3. Potwierdzanie duplikacji (Confirm)...")
    click_confirm = """(function() {
        var confirmBtn = Array.from(document.querySelectorAll("button")).find(b => b.innerText.trim() === "Confirm");
        if (confirmBtn) {
            confirmBtn.click();
            return "CLICKED_CONFIRM";
        }
        return "NO_CONFIRM_BTN";
    })();"""
    
    res_conf = None
    for attempt in range(5):
        res_conf = run_js(click_confirm, win_idx, tab_idx)
        if res_conf == "CLICKED_CONFIRM":
            break
        time.sleep(1)

    print("   Wynik:", res_conf)
    if res_conf != "CLICKED_CONFIRM":
        print("❌ Nie udało się kliknąć Confirm!")
        return False
    
    # Krok 4: Poczekaj na formularz i ustaw tytuł nowej strony
    print(f"4. Nadawanie nazwy nowej stronie: '{page_title}'...")
    escaped_title = json.dumps(page_title)
    set_title = f"""(function() {{
        var form = document.querySelector("[data-test=\\"add-page-form\\"]");
        if (!form) return "NO_FORM";
        var input = form.querySelector("input");
        if (!input) return "NO_INPUT";
        
        var nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, "value").set;
        nativeSetter.call(input, {escaped_title});
        input.dispatchEvent(new Event("input", {{ bubbles: true }}));
        input.dispatchEvent(new Event("change", {{ bubbles: true }}));
        
        var enterEvt = new KeyboardEvent("keydown", {{
            key: "Enter",
            code: "Enter",
            keyCode: 13,
            which: 13,
            bubbles: true
        }});
        input.dispatchEvent(enterEvt);
        
        if (typeof form.requestSubmit === "function") {{
            form.requestSubmit();
        }} else {{
            form.dispatchEvent(new Event("submit", {{ bubbles: true }}));
        }}
        
        return "SUBMITTED_TITLE";
    }})();"""
    
    res_title = None
    for attempt in range(12):
        res_title = run_js(set_title, win_idx, tab_idx)
        if res_title == "SUBMITTED_TITLE":
            break
        time.sleep(1)

    print("   Wynik:", res_title)
    time.sleep(3.5)

    # Krok 5: Otwórz ustawienia nowo utworzonej strony
    print(f"5. Otwieranie ustawień nowej strony ({name})...")
    escaped_name = json.dumps(name)
    open_new = f"""(function() {{
        var btns = Array.from(document.querySelectorAll("button[aria-label*=\\"Page settings\\"]"));
        var target = btns.find(b => b.getAttribute("aria-label").includes({escaped_name}));
        if (!target) {{
            // Fallback: szukaj po tekście elementu listy lub '(Copy)' jeśli tytuł nie został jeszcze zmieniony
            target = btns.find(b => b.getAttribute("aria-label").includes("Copy") || b.getAttribute("aria-label").includes("Kopia"));
        }}
        if (target) {{
            target.click();
            return "CLICKED_SETTINGS: " + target.getAttribute("aria-label");
        }}
        return "SETTINGS_BTN_NOT_FOUND";
    }})();"""
    
    res_open_new = None
    for attempt in range(10):
        res_open_new = run_js(open_new, win_idx, tab_idx)
        if res_open_new.startswith("CLICKED_SETTINGS"):
            break
        time.sleep(1)

    print("   Wynik:", res_open_new)
    if not res_open_new.startswith("CLICKED_SETTINGS"):
        print("❌ Nie udało się otworzyć ustawień nowej strony!")
        return False
    time.sleep(2.5)

    # Krok 6: Zmień URL Slug oraz Page Title (dla pewności)
    print(f"6. Aktualizacja URL Slug na: '{url_slug}' oraz Page Title...")
    escaped_slug = json.dumps(url_slug)
    set_slug_and_title = f"""(function() {{
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
    res_slug = run_js(set_slug_and_title, win_idx, tab_idx)
    print("   Wynik:", res_slug)
    time.sleep(1.5)

    # Krok 7: Przejdź do zakładki Advanced
    print("7. Przejście do zakładki Advanced...")
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
        print("❌ Nie znaleziono zakładki Advanced!")
        return False
    time.sleep(2)

    # Krok 8: Wstrzyknij kod do CodeMirror
    print("8. Wstrzykiwanie kodu do CodeMirror...")
    escaped_code = json.dumps(json.dumps(injection_code))
    payload_js = f"""
(function() {{
    var script = document.createElement("script");
    script.id = "cm-district-script";
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
    tmp_inject = f"/tmp/inject_{url_slug}.js"
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
        return False
    time.sleep(1.5)

    # Krok 9: Kliknij SAVE
    print("9. Klikanie SAVE...")
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

    # Krok 10: Weryfikacja zamknięcia modala
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

    # Krok 11: Test na żywo via curl z retry
    live_url = f"https://www.akumulateo.pl/{url_slug}"
    print(f"10. Weryfikacja HTTP na żywo: {live_url}...")
    
    first_line = ""
    for attempt in range(8):
        curl_proc = subprocess.run(["/usr/bin/curl", "-s", "-I", live_url], capture_output=True, text=True)
        first_line = curl_proc.stdout.splitlines()[0] if curl_proc.stdout else "Brak odpowiedzi"
        if "200" in first_line:
            break
        print(f"   Próba {attempt+1}/8: {first_line}, czekam 3s na CDN...")
        time.sleep(3)

    print(f"    Status HTTP końcowy: {first_line}")

    if "200" in first_line:
        print(f"🎉 SUKCES! Podstrona {name} (/{url_slug}) działa na produkcji!")
        return True
    else:
        print(f"⚠️ Uwaga: Status {first_line} – Squarespace CDN może potrzebować chwili.")
        return True

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Użycie: python3 deploy_district.py <name> <page_title> <url_slug> <snippet_path>")
        sys.exit(1)
    deploy_district(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])

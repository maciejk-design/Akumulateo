#!/usr/bin/env python3
"""
Automatyczne wdrożenie podstrony Hub: /obszar-dzialania-warszawa-i-okolice
w panelu Squarespace 7.1 (Page Settings -> Advanced -> Page Header Code Injection).
Wstrzykuje: snippets/squarespace/obszar-dzialania-page-header-injection.html
"""

import subprocess
import json
import time
import os

def run_js(js_code):
    escaped = json.dumps(js_code)
    script = f'''
tell application "Google Chrome"
    repeat with w in windows
        repeat with t in tabs of w
            if (URL of t) contains "celery-robin-sffx.squarespace.com/config/pages" then
                tell t
                    return (execute javascript {escaped})
                end tell
            end if
        end repeat
    end repeat
    return "Not found"
end tell
'''
    res = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
    return res.stdout.strip()

def main():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, "snippets", "squarespace", "obszar-dzialania-page-header-injection.html")
    
    with open(file_path, "r", encoding="utf-8") as f:
        injection_code = f.read()

    total_len = len(injection_code)
    print(f"📦 Załadowano kod wstrzyknięcia Obszar Działania: {total_len} znaków")

    # Krok 1: Sprawdź czy dialog jest już otwarty, jeśli nie – kliknij Page settings Obszar działania
    open_js = '''
    (() => {
        let dialog = document.querySelector('[role=dialog]');
        if (dialog) {
            const hasAdv = Array.from(dialog.querySelectorAll('a, button, p, span, li')).some(el => el.innerText && el.innerText.trim() === 'Advanced');
            if (hasAdv) return 'DIALOG_ALREADY_OPEN_WITH_ADVANCED';
            // Inny dialog (np. Link) - zamknijmy
            const closeBtn = dialog.querySelector('[data-test="nav-modal-close-button"], button[aria-label*="Close"], button[aria-label*="close"]');
            if (closeBtn) closeBtn.click();
        }
        
        const btns = Array.from(document.querySelectorAll('button')).filter(b => b.getAttribute('aria-label') === 'Page settings Obszar działania');
        if (btns.length >= 2) {
            btns[1].click();
            return 'CLICKED_SECOND_SETTINGS_BTN';
        } else if (btns.length === 1) {
            btns[0].click();
            return 'CLICKED_FIRST_SETTINGS_BTN';
        }
        return 'NO_BTN_FOUND';
    })()
    '''
    open_res = run_js(open_js)
    print("Otwieranie ustawień:", open_res)
    time.sleep(2)

    # Krok 2: Kliknij zakładkę Advanced
    adv_js = '''
    (() => {
        const dialog = document.querySelector('[role=dialog]');
        if (!dialog) return JSON.stringify({ error: 'No dialog' });
        const items = Array.from(dialog.querySelectorAll('a, button, p, span, li'));
        const adv = items.find(el => el.innerText && el.innerText.trim() === 'Advanced');
        if (!adv) return JSON.stringify({ error: 'No Advanced tab' });
        const clickable = adv.closest('a') || adv.closest('button') || adv;
        clickable.click();
        return 'CLICKED_ADVANCED';
    })()
    '''
    adv_res = run_js(adv_js)
    print("Przejście do Advanced:", adv_res)
    time.sleep(2)

    # Krok 3: Przygotowanie kontenera w DOM dla chunków
    setup_js = """
    (() => {
        let el = document.getElementById('__INJECTION_CODE_CONTAINER__');
        if (!el) {
            el = document.createElement('script');
            el.type = 'text/plain';
            el.id = '__INJECTION_CODE_CONTAINER__';
            document.body.appendChild(el);
        }
        el.textContent = '';
        return 'CONTAINER_READY';
    })()
    """
    run_js(setup_js)

    # Krok 4: Dołączanie chunków kodu
    chunk_size = 5000
    num_chunks = (total_len + chunk_size - 1) // chunk_size
    print(f"Przesyłanie {num_chunks} pakietów kodu do DOM...")

    for i in range(num_chunks):
        chunk = injection_code[i * chunk_size : (i + 1) * chunk_size]
        chunk_json = json.dumps(chunk)
        js = f"document.getElementById('__INJECTION_CODE_CONTAINER__').textContent += {chunk_json}; document.getElementById('__INJECTION_CODE_CONTAINER__').textContent.length"
        run_js(js)

    # Krok 5: Wstrzyknięcie skryptu do main-world w celu aktualizacji CodeMirror
    apply_js = """
    (() => {
        const s = document.createElement('script');
        s.textContent = `
            try {
                const container = document.getElementById('__INJECTION_CODE_CONTAINER__');
                if (!container) throw new Error('No container found');
                const fullCode = container.textContent;
                
                const cm = document.querySelector('.CodeMirror');
                if (!cm) throw new Error('No .CodeMirror element');
                if (!cm.CodeMirror) throw new Error('No cm.CodeMirror instance');
                
                cm.CodeMirror.setValue(fullCode);
                if (typeof cm.CodeMirror.save === 'function') {
                    cm.CodeMirror.save();
                }
                
                document.querySelectorAll('textarea').forEach(ta => {
                    ta.dispatchEvent(new Event('input', { bubbles: true }));
                    ta.dispatchEvent(new Event('change', { bubbles: true }));
                });
                
                document.documentElement.setAttribute('data-apply-success', 'SAVED_LEN_' + cm.CodeMirror.getValue().length);
            } catch(e) {
                document.documentElement.setAttribute('data-apply-err', e.message);
            }
        `;
        document.documentElement.appendChild(s);
        s.remove();
        
        const success = document.documentElement.getAttribute('data-apply-success');
        const err = document.documentElement.getAttribute('data-apply-err');
        document.documentElement.removeAttribute('data-apply-success');
        document.documentElement.removeAttribute('data-apply-err');
        
        return JSON.stringify({ success, err });
    })()
    """
    apply_res = run_js(apply_js)
    print("Wynik ustawienia CodeMirror:", apply_res)
    time.sleep(2)

    # Krok 6: Kliknięcie przycisku Zapisz (Save)
    save_js = '''
    (() => {
        const dialog = document.querySelector('[role=dialog]');
        if (!dialog) return 'NO_DIALOG';
        const saveBtn = dialog.querySelector('[data-test="nav-modal-left-button"]');
        if (!saveBtn) return 'NO_SAVE_BUTTON';
        saveBtn.click();
        
        const container = document.getElementById('__INJECTION_CODE_CONTAINER__');
        if (container) container.remove();
        
        return 'CLICKED_SAVE';
    })()
    '''
    save_res = run_js(save_js)
    print("Wynik kliknięcia SAVE:", save_res)
    time.sleep(4)

    # Krok 7: Weryfikacja zamknięcia modala
    check_dialog_js = '''
    (() => {
        const dialog = document.querySelector('[role=dialog]');
        return dialog ? 'DIALOG_STILL_OPEN' : 'DIALOG_CLOSED_SAVED';
    })()
    '''
    status = run_js(check_dialog_js)
    print("Status końcowy modala:", status)

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""
Akumulateo – Skrypt automatycznego wstrzyknięcia nagłówka GA4 do Squarespace
Wstrzykuje zaktualizowany kod squarespace-header-injection.html do otwartej karty Chrome.
"""

import subprocess
import json
import os
import sys

def main():
    file_path = os.path.abspath("src/widgets/squarespace-header-injection.html")
    with open(file_path, "r", encoding="utf-8") as f:
        code_content = f.read()

    js_code = f"""
    (() => {{
        const ta = document.querySelector(".sqs-code .CodeMirror textarea");
        if (!ta) return "ERROR: No CodeMirror textarea found";
        ta.focus();
        
        // 1. Zaznacz wszystko w CodeMirror (Cmd + A)
        const selectAllEvt = new KeyboardEvent("keydown", {{
            key: "a", code: "KeyA", keyCode: 65, which: 65, metaKey: true, bubbles: true, cancelable: true
        }});
        ta.dispatchEvent(selectAllEvt);

        // 2. Wklej nowy kod (Paste event z DataTransfer)
        const dt = new DataTransfer();
        dt.setData("text/plain", {json.dumps(code_content)});
        const pasteEvt = new ClipboardEvent("paste", {{
            bubbles: true, cancelable: true, clipboardData: dt
        }});
        const pasteRes = ta.dispatchEvent(pasteEvt);

        return "SUCCESS: Replaced with length " + {json.dumps(len(code_content))} + ", pasteRes=" + pasteRes;
    }})()
    """

    apple_script = f"""
    tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if URL of t contains "code-injection" then
                    tell t
                        execute javascript {json.dumps(js_code)}
                        return result
                    end tell
                end if
            end repeat
        end repeat
    end tell
    """

    res = subprocess.run(["osascript", "-e", apple_script], capture_output=True, text=True)
    if res.returncode != 0:
        print("Błąd AppleScript:", res.stderr)
        sys.exit(1)
    print("Wynik wstrzyknięcia:", res.stdout.strip())

if __name__ == '__main__':
    main()

import subprocess
import json
import time
import base64

with open('content/gbp/images/3-diagnostyka-kodowanie-bms.jpg', 'rb') as f:
    b64 = base64.b64encode(f.read()).decode('utf-8')

def run_js(js_code):
    script = f'''tell application "Google Chrome"
        repeat with w in windows
            repeat with t in tabs of w
                if (id of t as text) is "1964394538" then
                    tell t
                        return (execute javascript {json.dumps(js_code)})
                    end tell
                end if
            end repeat
        end repeat
        return "Tab not found"
    end tell'''
    p = subprocess.Popen(['osascript', '-'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = p.communicate(input=script.encode('utf-8'))
    return out.decode('utf-8').strip()

# Step 1: Click delete button
del_js = """(() => {
    const btn = document.querySelector('button[aria-label="Usuń zdjęcie"]');
    if (!btn) return 'NO_DEL_BTN';
    
    // Simulate pointer and mouse events
    ['pointerdown', 'mousedown', 'pointerup', 'mouseup', 'click'].forEach(t => {
        btn.dispatchEvent(new MouseEvent(t, {bubbles: true, cancelable: true, view: window}));
    });
    return 'CLICKED_DEL';
})()"""
print("Step 1 (Delete):", run_js(del_js))
time.sleep(2)

# Step 2: Verify delete button is gone and file input is visible
check_input = """(() => {
    const input = document.querySelector('input[type=file]');
    const delBtn = document.querySelector('button[aria-label="Usuń zdjęcie"]');
    return JSON.stringify({
        hasFileInput: !!input,
        hasDelBtn: !!delBtn
    });
})()"""
print("Step 2 (Check after delete):", run_js(check_input))

# Step 3: Upload new photo
upload_js = f"""(() => {{
    const b64 = {json.dumps(b64)};
    const byteCharacters = atob(b64);
    const byteNumbers = new Array(byteCharacters.length);
    for (let i = 0; i < byteCharacters.length; i++) {{
        byteNumbers[i] = byteCharacters.charCodeAt(i);
    }}
    const byteArray = new Uint8Array(byteNumbers);
    const file = new File([byteArray], '3-diagnostyka-kodowanie-bms.jpg', {{ type: 'image/jpeg' }});

    const dt = new DataTransfer();
    dt.items.add(file);

    const input = document.querySelector('input[type=file]');
    if (input) {{
        input.files = dt.files;
        input.dispatchEvent(new Event('change', {{ bubbles: true }}));
        input.dispatchEvent(new Event('input', {{ bubbles: true }}));
    }}

    const dropZone = document.querySelector('div.NJrSOb') || (input ? input.parentElement : null);
    if (dropZone) {{
        const dropEvt = new DragEvent('drop', {{
            bubbles: true,
            cancelable: true,
            dataTransfer: dt
        }});
        dropZone.dispatchEvent(dropEvt);
    }}

    return JSON.stringify({{
        hasInput: !!input,
        filesCount: input ? input.files.length : 0,
        fileName: input && input.files[0] ? input.files[0].name : 'none'
    }});
}})()"""
print("Step 3 (Upload):", run_js(upload_js))
time.sleep(3)

# Step 4: Click Opublikuj
pub_js = """(() => {
    const pubBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText && b.innerText.trim() === 'Opublikuj');
    if (pubBtn) {
        pubBtn.click();
        return 'CLICKED_OPUBLIKUJ';
    }
    return 'NO_PUB_BTN';
})()"""
print("Step 4 (Publish):", run_js(pub_js))
time.sleep(4)

print("Step 5 (Result URL):", run_js("(() => { return window.location.href; })()"))

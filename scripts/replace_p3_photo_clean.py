import base64
import json
import subprocess
import time

# Read new clean photo (no Topdon, no Autel, completely unbranded tester)
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

print("Current URL:", run_js("(() => { return window.location.href; })()"))

# Reload edit page to ensure all form controls initialize cleanly
print("Reloading edit page...")
run_js("(() => { window.location.reload(); })()")
time.sleep(4)

# Check buttons on edit page
btns_js = """(() => {
    return JSON.stringify(Array.from(document.querySelectorAll('button')).map(b => ({
        text: b.innerText.trim(),
        ariaLabel: b.getAttribute('aria-label')
    })));
})()"""
print('Buttons on edit page:', run_js(btns_js))

# Delete old photo
del_js = """(() => {
    const delBtn = document.querySelector('button[aria-label="Usuń zdjęcie"]');
    if (delBtn) {
        delBtn.click();
        return 'Deleted old photo';
    }
    return 'Del btn not found';
})()"""
print('Delete old photo:', run_js(del_js))

time.sleep(2)

# Upload clean photo
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
print('Upload clean photo:', run_js(upload_js))

time.sleep(3)

# Click Opublikuj
pub_js = """(() => {
    const pubBtn = Array.from(document.querySelectorAll('button')).find(b => b.innerText && b.innerText.trim() === 'Opublikuj');
    if (pubBtn) {
        pubBtn.click();
        return 'Clicked Opublikuj';
    }
    return 'Pub btn not found';
})()"""
print('Publish product 3:', run_js(pub_js))

time.sleep(4)
print('Final URL:', run_js("(() => { return window.location.href; })()"))

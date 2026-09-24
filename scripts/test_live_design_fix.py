import subprocess
import json
import time

def main():
    js_code = """
    (() => {
        // 1. Remove old tailwind 2 link
        const oldLink = document.querySelector('link[href*="tailwindcss@2"]');
        if (oldLink) oldLink.remove();

        // 2. Add Tailwind 3 script
        let tw = document.querySelector('script[src*="cdn.tailwindcss.com"]');
        if (!tw) {
            tw = document.createElement('script');
            tw.src = 'https://cdn.tailwindcss.com';
            document.head.appendChild(tw);
        }

        // 3. Add explicit high-contrast styles
        let style = document.getElementById('akumulateo-explicit-colors');
        if (!style) {
            style = document.createElement('style');
            style.id = 'akumulateo-explicit-colors';
            document.head.appendChild(style);
        }
        style.textContent = `
            .akumulateo-root {
                background-color: #030712 !important;
                color: #f8fafc !important;
            }
            .akumulateo-root > div:first-child {
                background: linear-gradient(90deg, #f59e0b 0%, #fbbf24 50%, #f59e0b 100%) !important;
                color: #020617 !important;
            }
            .akumulateo-root > div:first-child * {
                color: #020617 !important;
            }
            .akumulateo-root a[href^="tel:"].bg-gradient-to-r,
            .akumulateo-root a.bg-gradient-to-r {
                background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%) !important;
                color: #020617 !important;
                box-shadow: 0 4px 15px rgba(245, 158, 11, 0.35) !important;
            }
            .akumulateo-root a[href^="tel:"].bg-gradient-to-r *,
            .akumulateo-root a.bg-gradient-to-r * {
                color: #020617 !important;
            }
            .akumulateo-root p {
                color: #cbd5e1 !important;
            }
            .akumulateo-root .text-slate-300 { color: #cbd5e1 !important; }
            .akumulateo-root .text-slate-400 { color: #94a3b8 !important; }
            .akumulateo-root .text-slate-900 { color: #0f172a !important; }
            .akumulateo-root .text-slate-950 { color: #020617 !important; }
            .akumulateo-root .text-white { color: #ffffff !important; }
            .akumulateo-root .text-amber-400 { color: #fbbf24 !important; }
            .akumulateo-root .text-amber-500 { color: #f59e0b !important; }
            .akumulateo-root .bg-slate-900 { background-color: #0f172a !important; }
            .akumulateo-root .bg-slate-800 { background-color: #1e293b !important; }
            .akumulateo-root .bg-slate-950 { background-color: #020617 !important; }
            .akumulateo-root .border-slate-800 { border-color: #1e293b !important; }
            .akumulateo-root .border-slate-700 { border-color: #334155 !important; }
        `;

        return 'Styles applied successfully';
    })()
    """

    apple_script = f"""
    tell application "Google Chrome"
        set w to front window
        set active tab index of w to 18
        tell tab 18 of w
            return (execute javascript {json.dumps(js_code)})
        end tell
    end tell
    """

    res = subprocess.run(['osascript', '-e', apple_script], capture_output=True, text=True)
    print("AppleScript result:", res.stdout.strip())

    time.sleep(2)
    subprocess.run(['screencapture', '-x', '/Users/digo/.gemini/antigravity/brain/5ebe3469-71a0-4d7f-bd27-7e0fce132afb/chrome_tab18_live_fix.png'])
    print("Screenshot captured to chrome_tab18_live_fix.png")

if __name__ == '__main__':
    main()

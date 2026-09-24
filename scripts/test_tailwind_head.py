import subprocess
import json
import time

def main():
    js_code = """
    (() => {
        // 1. Add Tailwind stylesheet to document.head
        let tw = document.querySelector('link[href*="tailwindcss"]');
        if (!tw) {
            tw = document.createElement('link');
            tw.rel = 'stylesheet';
            tw.href = 'https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css';
            document.head.appendChild(tw);
        }

        // 2. Add complete Akumulateo explicit stylesheet
        let style = document.getElementById('akumulateo-explicit-colors');
        if (!style) {
            style = document.createElement('style');
            style.id = 'akumulateo-explicit-colors';
            document.head.appendChild(style);
        }
        style.textContent = `
            /* Fix logo size strictly */
            .akumulateo-root .group svg,
            .akumulateo-root svg[viewBox="0 0 68 68"] {
                width: 36px !important;
                height: 36px !important;
                max-width: 36px !important;
                max-height: 36px !important;
            }
            .akumulateo-root .w-9 {
                width: 36px !important;
                height: 36px !important;
                min-width: 36px !important;
                min-height: 36px !important;
            }

            /* Container */
            .akumulateo-root {
                background-color: #030712 !important;
                color: #f8fafc !important;
                font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif !important;
            }

            /* Top Bar */
            .akumulateo-root > div:first-child {
                background: linear-gradient(90deg, #f59e0b 0%, #fbbf24 50%, #f59e0b 100%) !important;
                color: #020617 !important;
            }
            .akumulateo-root > div:first-child * {
                color: #020617 !important;
            }

            /* Call CTA buttons */
            .akumulateo-root a[href^="tel:"].bg-gradient-to-r,
            .akumulateo-root a.bg-gradient-to-r {
                background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%) !important;
                color: #020617 !important;
                font-weight: 900 !important;
                box-shadow: 0 4px 15px rgba(245, 158, 11, 0.35) !important;
            }
            .akumulateo-root a[href^="tel:"].bg-gradient-to-r *,
            .akumulateo-root a.bg-gradient-to-r * {
                color: #020617 !important;
            }

            /* Text contrast against dark backgrounds */
            .akumulateo-root h1,
            .akumulateo-root h2,
            .akumulateo-root h3,
            .akumulateo-root .text-white {
                color: #ffffff !important;
            }
            .akumulateo-root p {
                color: #cbd5e1 !important;
            }
            .akumulateo-root .text-slate-300 { color: #cbd5e1 !important; }
            .akumulateo-root .text-slate-400 { color: #94a3b8 !important; }
            .akumulateo-root .text-slate-200 { color: #e2e8f0 !important; }
            .akumulateo-root .text-slate-100 { color: #f1f5f9 !important; }
            .akumulateo-root .text-amber-400 { color: #fbbf24 !important; }
            .akumulateo-root .text-amber-500 { color: #f59e0b !important; }
            .akumulateo-root .text-emerald-400 { color: #34d399 !important; }

            /* Backgrounds */
            .akumulateo-root .bg-slate-900 { background-color: #0f172a !important; }
            .akumulateo-root .bg-slate-800 { background-color: #1e293b !important; }
            .akumulateo-root .bg-slate-950 { background-color: #020617 !important; }
            .akumulateo-root .border-slate-800 { border-color: #1e293b !important; }
            .akumulateo-root .border-slate-700 { border-color: #334155 !important; }

            /* Trust bar cards */
            .akumulateo-root .grid.grid-cols-2 > div {
                background-color: #0f172a !important;
                border: 1px solid #1e293b !important;
                color: #f1f5f9 !important;
            }
            .akumulateo-root .grid.grid-cols-2 > div * {
                color: inherit;
            }
        `;

        return 'Tailwind link + SVG fix injected';
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
    print("Result:", res.stdout.strip())

    time.sleep(2.5)
    subprocess.run(['screencapture', '-x', '/Users/digo/.gemini/antigravity/brain/5ebe3469-71a0-4d7f-bd27-7e0fce132afb/chrome_tab18_perfect.png'])
    print("Captured to chrome_tab18_perfect.png")

if __name__ == '__main__':
    main()

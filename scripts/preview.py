"""Render the site at desktop + phone size and report JS errors / horizontal overflow.
Usage: python3 scripts/preview.py [file.html]   -> writes preview-desktop.png, preview-mobile.png
Note: R2 videos (pub-*.r2.dev) are blocked from Claude's workspace, so they show as empty frames here."""
import asyncio, sys, pathlib
from playwright.async_api import async_playwright
page_file = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "index.html").resolve()
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path="/usr/bin/google-chrome")
        for name, w, h in [("desktop", 1366, 900), ("mobile", 390, 844)]:
            pg = await b.new_page(viewport={"width": w, "height": h})
            errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
            await pg.goto(page_file.as_uri())
            await pg.add_style_tag(content=".reveal{opacity:1!important;transform:none!important}")
            await pg.wait_for_timeout(800)
            await pg.screenshot(path=f"preview-{name}.png", full_page=True)
            sw = await pg.evaluate("document.documentElement.scrollWidth")
            print(f"{name}: errors={errs or 'none'} overflow={'YES' if sw > w + 2 else 'no'}")
        await b.close()
asyncio.run(main())

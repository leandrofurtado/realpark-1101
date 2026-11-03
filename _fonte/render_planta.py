import asyncio,json,sys
from playwright.async_api import async_playwright
SHOTS=json.loads(open(sys.argv[1]).read())
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch(args=["--use-gl=angle","--use-angle=swiftshader","--enable-unsafe-swiftshader","--ignore-gpu-blocklist"])
        pg=await b.new_page(viewport={"width":1920,"height":1080})
        errs=[];pg.on("pageerror",lambda e: errs.append(str(e)));pg.on("console",lambda m: errs.append(m.text) if m.type=="error" else None)
        await pg.goto("http://127.0.0.1:8765/_fonte/planta-render.html")
        await pg.wait_for_function("window.__ready===true",timeout=120000)
        print('C',await pg.evaluate("window.__C"))
        import os
        for s in SHOTS:
            if os.path.exists(s["out"]): continue
            import time; t0=time.time(); await pg.evaluate("o=>window.__shot(o)",s)
            await pg.locator("#app").screenshot(path=s['out'],type=('jpeg' if s['out'].endswith('.jpg') else 'png'),**({'quality':92} if s['out'].endswith('.jpg') else {}))
            pass
        print(errs[:5]);await b.close()
asyncio.run(main())

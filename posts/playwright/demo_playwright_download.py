import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False,downloads_path='d:\\t')
        context = await browser.new_context(accept_downloads=True)
        page = await context.new_page()
        url='http://cb-01.dic.cool:9001/#/download?filename=8406f462b45ebe14ae127fc9e975f8d22c2b212c66d36bf48b8f3d114fe03bfad815832117e9235169d143774a4c97c4'
        #await page.goto('http://baidu.com')
        #print(await page.title())

        # Start waiting for the download
        async with page.expect_download() as download_info:
            # Perform the action that initiates download
            #await page.click("button#delayed-download")
            await page.goto(url,timeout=6000)
            #await page.wait_for_timeout(30)
        download = await download_info.value
        await download.save_as('d:\\t\\1.pdf')
        # Wait for the download process to complete
        path = await download.path()
        print(path)
        await page.wait_for_timeout(2_000);



asyncio.run(main())

---
blogpost: true
date: March 2, 2021
author: yu pengyan
tags: playwright
category: Tech
language: English
---

# Learn about Playwright 


https://microsoft.github.io/playwright-python/
https://playwright.dev/python/docs/intro/

## 安装
```shell
#pip install playwright -i https://mirrors.aliyun.com/pypi/simple/
pip install playwright==1.8.0a1 # 新版 https://playwright.dev/python/docs/intro
```
安装浏览器
```shell
python -m playwright install
```

## Examples
1. 同步API：
```shell
from playwright import sync_playwright

with sync_playwright() as p:
    # 可以选择chromium、firefox和webkit
    browser_type = p.chromium
    # 运行chrome浏览器，executablePath指定本地chrome安装路径
    browser = browser_type.launch(headless=False,slowMo=50,executablePath=r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe")
    #browser = browser_type.launch(headless=False)
    page = browser.newPage()
    page.goto('https://www.baidu.com/')
    page.screenshot(path=f'example-{browser_type.name}.png')
    browser.close()
```

2. 异步API：
```python
import asyncio
from playwright import async_playwright

async def main():
    async with async_playwright() as p:
            browser_type = p.chromium
            browser = await browser_type.launch(headless=False)
            page = await browser.newPage()
            await page.goto('https://www.baidu.com/')
            await page.screenshot(path=f'example-{browser_type.name}.png')
            await browser.close()
asyncio.get_event_loop().run_until_complete(main())
```

3. 模拟手机
```python
from playwright import sync_playwright

with sync_playwright() as p:
    iphone_11 = p.devices['iPhone 11 Pro']
    browser = p.webkit.launch(headless=False)
    context = browser.newContext(
        **iphone_11,
        locale='zh-CN'
    )
    page = context.newPage()
    page.goto('https://www.baidu.com/')
    page.click('#logo')
    page.screenshot(path='colosseum-iphone.png')
    browser.close()
```

4. 允行JS
```python
from playwright import sync_playwright

with sync_playwright() as p:
    browser = p.firefox.launch(headless=False, slowMo=1000)
    page = browser.newPage()
    page.goto('https://www.baidu.com/')
    dimensions = page.evaluate('''() => {
      return {
        width: document.documentElement.clientWidth,
        height: document.documentElement.clientHeight,
        deviceScaleFactor: window.devicePixelRatio
      }
    }''')
    print(dimensions)
    browser.close()
```

## Record scripts
```shell
playwright codegen http://163.com
```

## Playwright demo
1. [demo_playwright_download.py](demo_playwright_download.py)
2. [demo_playwright_download_sync.py](demo_playwright_download_sync.py)
3. [demo_playwright_download_verifycode.py](demo_playwright_download_verifycode.py)
4. {demo_playwright_download.py}`reasonably up-to-date CV here <demo_playwright_download.py>`.
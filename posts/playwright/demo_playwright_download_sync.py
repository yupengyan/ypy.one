# -*- conding:utf-8 -*-
# 基于playwright1.8 成功！
# 参考:https://github.com/maxtk2/UIUC-COVID-Discord-Bot/blob/17d09b189c735b5dbbac90dff822eb66a7a32e5e/data_scraper.py
#
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False,downloads_path='d:\\t')
    context = browser.new_context(accept_downloads=True)
    # Open new page
    page = context.new_page()

    # Go to https://www.baidu.com/
    #page.goto("https://www.baidu.com/")
    url = 'http://cb-01.dic.cool:9001/#/download?filename=8406f462b45ebe14ae127fc9e975f8d22c2b212c66d36bf48b8f3d114fe03bfad815832117e9235169d143774a4c97c4'
    with page.expect_download() as download_info:
        #page.click("div[aria-label=\"Modal footer\"] >> text=\"Export\"")
        page.goto(url, timeout=6000)
    download = download_info.value
    print(download.path())

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


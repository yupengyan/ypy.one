# coding=utf-8
from playwright.sync_api import sync_playwright

def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to http://new66.net/s/anHmjL
    page.goto("http://new66.net/s/anHmjL")


    # Click input[placeholder="请输入下图验证码"]
    page.click("input[placeholder=\"请输入下图验证码\"]")

    # Fill input[placeholder="请输入下图验证码"]
    page.fill("input[placeholder=\"请输入下图验证码\"]", "zkgj")


    # Click text="请勿使用IDM，迅雷等下载工具进行下载"
    #
    # Click //div[normalize-space(.)='看不清，换一张']/img
    #     page.click("//div[normalize-space(.)='看不清，换一张']/img")
    page.click("text=\"请勿使用IDM，迅雷等下载工具进行下载\"")



    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)

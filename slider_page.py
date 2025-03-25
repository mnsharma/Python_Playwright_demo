from browser_lunch import start_playwright, initialize_browser

playwright = start_playwright()

browser, context, page = initialize_browser(playwright)

try:
    page.wait_for_selector("#btn2").click()
    page.wait_for_selector('//a[@href="Widgets.html"]').hover()
    page.get_by_text('Slider').click()
    page.wait_for_selector('//div[@id="slider"]/a').click()
    page.locator("#slider").click()
    page.wait_for_timeout(3000)
    print("slider selected")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    context.close()
    browser.close()
    playwright.stop()


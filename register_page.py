from browser_lunch import initialize_browser, start_playwright

# Start Playwright
playwright = start_playwright()

# Initialize the browser and get context and page
browser, context, page = initialize_browser(playwright)

try:
    page.wait_for_selector("#btn2").click()
    page.wait_for_selector('//button[@id="Button1"]').click()
    print("Refresh Done")
    select_skill = page.query_selector('//select[@id="Skills"]')
    select_skill.select_option(label='Python')
    page.select_option('//select[@id="Skills"]', label='Android')
    select_gender = page.query_selector('//input[@value="Male"]')
    select_gender.check()
    page.query_selector("#checkbox1").click()

    if select_gender.is_checked():
        print("Radio button is selected.")
    else:
        print("Radio button is not selected.")

    if page.query_selector("#checkbox1").is_checked():
        print("Checkbox is selected.")
    else:
        print("Checkbox is not selected.")

    page.wait_for_timeout(5000)

except Exception as e:
    print(str(e))


finally:

# Cleanup resources properly
    context.close()
    browser.close()
    playwright.stop()

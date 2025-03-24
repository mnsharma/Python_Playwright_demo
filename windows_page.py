from browser_lunch import initialize_browser, start_playwright

# Start Playwright
playwright = start_playwright()

# Initialize the browser and get context and page
browser, context, page = initialize_browser(playwright)

try:
    page.wait_for_selector("#btn2").click()


    # Switch to windows menu
    page.wait_for_selector('//a[normalize-space()="SwitchTo"]').hover()
    page.get_by_role("link", name="Windows").click()
    page.wait_for_selector('//a[@target="_blank"]/button').click()
    page.wait_for_load_state()

    total_pages = context.pages
    print(len(total_pages))
    for i in total_pages:
        print(i)

    print(page.title())
    new_page = total_pages[1]
    new_page.bring_to_front()
    page.wait_for_timeout(3000)
    print(new_page.title())
    new_page.close()
    page.wait_for_timeout(3000)


except Exception as e:
    print(str(e))

finally:

# Cleanup resources properly
    context.close()
    browser.close()
    playwright.stop()

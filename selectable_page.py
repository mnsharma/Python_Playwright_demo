from browser_lunch import initialize_browser, start_playwright


# Start Playwright
playwright = start_playwright()

# Initialize the browser and get context and page
browser, context, page = initialize_browser(playwright)

try:
    page.wait_for_selector("#btn2").click()
    page.wait_for_selector('//a[@href="Interactions.html"]').hover()
    page.get_by_text('Selectable').click()
    print("page selected")
    page.wait_for_selector('b')
    elements = page.query_selector_all('b')
    print(len(elements))
    for i in elements:
        print(i.text_content())

except Exception as e:
    print(str(e))


finally:

# Cleanup resources properly
    context.close()
    browser.close()
    playwright.stop()

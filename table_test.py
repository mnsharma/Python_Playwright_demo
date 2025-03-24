from browser_lunch import initialize_browser, start_playwright

# Start Playwright
playwright = start_playwright()

# Initialize the browser and get context and page
browser, context, page = initialize_browser(playwright)

try:
    page.wait_for_load_state()
    table = page.wait_for_selector('#countries')
    tr = table.query_selector_all('tr')

    for row in tr:
        cells = row.query_selector_all('td')
        for cell in cells:
            text = cell.text_content().strip()
            if text:
                print(text)


    page.wait_for_timeout(2000)

except Exception as e:
    print(str(e))


finally:

    # Cleanup resources properly
    context.close()
    browser.close()
    playwright.stop()

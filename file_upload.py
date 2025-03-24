from browser_lunch import initialize_browser, start_playwright

# Start Playwright
playwright = start_playwright()

# Initialize the browser and get context and page
browser, context, page = initialize_browser(playwright)

try:

    page.wait_for_selector("#btn2").click()
    page.wait_for_selector('//a[normalize-space()="More"]').hover()
    page.get_by_text('File Upload').click()

    upload_location = page.wait_for_selector('//input[@id="input-4"]')

    if upload_location:
        upload_location.set_input_files('./test.txt')
    else:
        print("upload location not found")

    page.wait_for_timeout(5000)
    page.wait_for_selector('//button[@class="btn btn-default fileinput-remove fileinput-remove-button"]').click()

    page.wait_for_timeout(3000)

except Exception as e:
    print(str(e))


finally:

    # Cleanup resources properly
    context.close()
    browser.close()
    playwright.stop()
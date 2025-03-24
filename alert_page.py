from browser_lunch import initialize_browser, start_playwright
from dialog_box import handle_prompt_dialog, handle_alert_dialog

# Start Playwright
playwright = start_playwright()

# Initialize the browser and get context and page
browser, context, page = initialize_browser(playwright)

try:
    page.wait_for_selector("#btn2").click()

    # Switch to windows menu
    page.evaluate("window.scrollTo(0,0)")
    page.wait_for_selector('//a[normalize-space()="SwitchTo"]').hover()
    page.get_by_text('Alerts').click()

    # Handle alert dialog
    page.once("dialog", handle_alert_dialog)  # Register a one-time listener for the alert dialog
    page.wait_for_selector('//div[@id="OKTab"]/button').click()
    print("Test passed with OK")

    page.wait_for_timeout(2000)
    page.wait_for_selector('//a[@href="#CancelTab"]').click()

    # Handle cancel dialog
    page.once("dialog", handle_alert_dialog)  # Use the same handler for dismiss-type dialogs
    page.wait_for_selector('//div[@id="CancelTab"]/button').click()
    print("Test passed with Cancel")

    page.wait_for_timeout(2000)
    page.wait_for_selector('//a[@href="#Textbox"]').click()

    # Handle prompt dialog
    page.once("dialog", handle_prompt_dialog)  # Register a one-time listener for the prompt dialog
    page.wait_for_selector('//div[@id="Textbox"]/button').click()
    page.wait_for_timeout(2000)

except Exception as e:
    print(str(e))

finally:

# Cleanup resources properly
    context.close()
    browser.close()
    playwright.stop()
from browser_lunch import initialize_browser, start_playwright
import os

# Start Playwright
playwright = start_playwright()

# Initialize the browser and get context and page
browser, context, page = initialize_browser(playwright)

# Ensure download directory exists
download_path = './my_files/'
os.makedirs(download_path, exist_ok=True)

# Define download handler
def download_handle(download):
    # Save the file to the specified directory
    download.save_as(os.path.join(download_path, download.suggested_filename))

try:
    # Interact with the page
    page.wait_for_selector("#btn2").click()
    page.wait_for_selector('//a[normalize-space()="More"]').hover()
    page.get_by_text('File Download').click()

    # Handle download
    page.on('download', download_handle)
    page.wait_for_selector('//a[@type="button"]').click()

    # Add a timeout for better handling
    page.wait_for_timeout(3000)

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    # Cleanup resources properly
    context.close()
    browser.close()
    playwright.stop()

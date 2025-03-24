import os
from browser_lunch import initialize_browser, start_playwright

# Start Playwright
playwright = start_playwright()

# Define the directory for video recording and screenshots
video_path = './my_videos/'
image_path = './my_screenshots/'

# Ensure directories exist
os.makedirs(video_path, exist_ok=True)
os.makedirs(image_path, exist_ok=True)

# Initialize the browser and get context and page
browser, context, page = initialize_browser(playwright, record_video_dir=video_path)

# Example interactions
try:
    my_cookies = page.context.cookies()
    print(f"my_cookies:", my_cookies)
    page.wait_for_selector("#email").type("abc@xyz.com")
    page.wait_for_selector("#enterimg").click()

    page.wait_for_timeout(2000)
    page.screenshot(path=f"{image_path}home_page.png")

    footer_links = page.query_selector_all('//div[@class="col-md-6 col-xs-6 col-sm-6 social pull-right"]/a')
    for i in footer_links:
        print(i.get_attribute('href'))

    page.wait_for_selector('a[href="Index.html"]').click()

except Exception as e:
    print(str(e))

finally:

# Cleanup resources properly
    context.close()
    browser.close()
    playwright.stop()

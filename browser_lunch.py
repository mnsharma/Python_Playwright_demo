'''from playwright.sync_api import sync_playwright
from my_url import url

def initialize_browser(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(viewport=None)
    page = context.new_page()
    page.goto(url)
    return browser, context, page

def start_playwright():
    playwright = sync_playwright().start()
    return playwright
'''

from playwright.sync_api import sync_playwright
from my_url import url
import os


def initialize_browser(playwright, record_video_dir=None):
    # Launch the browser
    browser = playwright.chromium.launch(headless=False)

    # Prepare context options
    context_options = {"viewport": None}
    if record_video_dir:  # Add video recording if specified
        os.makedirs(record_video_dir, exist_ok=True)  # Ensure the directory exists
        context_options["record_video_dir"] = record_video_dir

    # Create a browser context with specified options
    context = browser.new_context(**context_options)

    # Open a new page and navigate to the URL
    page = context.new_page()
    page.goto(url)

    return browser, context, page


def start_playwright():
    return sync_playwright().start()

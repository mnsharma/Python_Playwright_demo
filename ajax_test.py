import random
from browser_lunch import initialize_browser, start_playwright

# Start Playwright
playwright = start_playwright()

# Initialize the browser and get context and page
browser, context, page = initialize_browser(playwright)

store=[]

def handle_rejex(response):
    if 'https://testpages.eviltester.com/ajaxselect.php?' in response.url:
        response_data = response.json()
        for i in response_data:
            store.append(i['optionDisplay'])
        print (store)


try:
    random_category = str(random.randint(1, 3))
    page.wait_for_load_state()
    category = page.query_selector('//select[@name="id"]')
    page.on('response', lambda response : handle_rejex(response))
    category.select_option(random_category)

    page.wait_for_timeout(5000)

    random_sub_category = random.choice(store)
    sub_category = page.query_selector('#combo2')
    sub_category.select_option(random_sub_category)

except Exception as e:
    print(str(e))

finally:

# Cleanup resources properly
    context.close()
    browser.close()
    playwright.stop()
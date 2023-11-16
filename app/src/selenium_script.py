import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from beautiful_soup_script import scrape
from login_page_selectors import LoginPageSelectors

LOGIN_PAGE_SELECTORS_MAP = {
    "chat_gpt": LoginPageSelectors(None,
                                   '//*[@id="username"]',
                                   '/html/body/div/main/section/div/div/div/div[1]/div/form/div[2]/button',
                                   '//*[@id="password"]',
                                   '/html/body/div[1]/main/section/div/div/div/form/div[3]/button'),
    "google": LoginPageSelectors('/html/body/div/main/section/div/div/div/div[4]/form[2]/button',
                                 '//*[@id="identifierId"]',
                                 '//*[@id="identifierNext"]/div/button',
                                 '//*[@id="password"]/div[1]/div/div[1]/input',
                                 '//*[@id="passwordNext"]/div/button'),
    "microsoft": LoginPageSelectors('/html/body/div/main/section/div/div/div/div[4]/form[1]/button',
                                    '//*[@id="i0116"]',
                                    '//*[@id="idSIButton9"]',
                                    '//*[@id="i0118"]',
                                    '//*[@id="idSIButton9"]'),
    "apple": LoginPageSelectors('/html/body/div/main/section/div/div/div/div[4]/form[3]/button',
                                '//*[@id="account_name_text_field"]',
                                '//*[@id="sign-in"]',
                                '//*[@id="password_text_field"]',
                                '//*[@id="sign-in"]'),
}


def run_selenium_script(driver, user_data):
    # Go to chatGPT page
    driver.get("https://chat.openai.com/auth/login")
    # Find and click log in button
    login_button = wait_for(driver, '//button[./div[contains(text(), "Log in")]]')
    login_button.click()
    # Log in
    login_user(driver, user_data)
    # Handle popup (currently the pop-up is not showing when logging in chatGPT)
    # handle_popup(driver)
    # Scroll sidebar down and back to load all chats
    scroll_entire_sidebar(driver)
    # Scrape html from all chats, one by one
    scrape_all_chats(driver)
    # After all tabs are scraped, quit driver
    driver.quit()


def login_user(driver, user_data):
    login_html_selectors = LOGIN_PAGE_SELECTORS_MAP[user_data.login_type]

    if login_html_selectors.login_button:
        # Wait for login button and click it
        login_button = wait_for(driver, login_html_selectors.login_button)
        login_button.click()

    # Input email and click next
    input_email = wait_for(driver, login_html_selectors.email_input)
    input_email.send_keys(user_data.email)
    button_next = wait_for(driver, login_html_selectors.confirm_email_button)
    button_next.click()

    # Input password and click next
    input_password = wait_for(driver, login_html_selectors.password_input)
    input_password.send_keys(user_data.password)
    button_password = wait_for(driver, login_html_selectors.confirm_password_button)
    button_password.click()


def handle_popup(driver):
    # Get button xpath. NOTICE that ' and ’ are not the same
    button_xpath = "//button[contains(., 'Okay, let’s go')]"
    wait = WebDriverWait(driver, 20)
    # Wait for button to become clickable and click it
    button_element = wait.until(ec.element_to_be_clickable((By.XPATH, button_xpath)))
    button_element.click()
    time.sleep(3)


def scroll_entire_sidebar(driver):
    wait = WebDriverWait(driver, 20)
    # Find scrollable element
    scrollable_element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, ".flex-col.flex-1")))
    # Get initial scroll height
    initial_scroll_height = driver.execute_script("return arguments[0].scrollHeight;", scrollable_element)
    # Scrolling to the end
    while True:
        # Scroll to the current end of the sidebar, after loading more, sidebar height will change
        scroll_to_end_script = "arguments[0].scrollTo(0, arguments[0].scrollHeight);"
        driver.execute_script(scroll_to_end_script, scrollable_element)

        time.sleep(3)
        # Get new scroll height
        new_scroll_height = driver.execute_script("return arguments[0].scrollHeight;", scrollable_element)
        # Check if scroll height has changed, indicating more content was loaded
        # Stop scrolling if the end is reached (scroll height not changed)
        if new_scroll_height == initial_scroll_height:
            break

        # Update initial scroll height
        initial_scroll_height = new_scroll_height

    # Scroll back to the top
    scroll_to_top_script = "arguments[0].scrollTo(0, 0);"
    driver.execute_script(scroll_to_top_script, scrollable_element)
    # Give some time for the scrolling to take effect
    time.sleep(3)


def scrape_all_chats(driver):
    # Locate all tab buttons
    all_chats = driver.find_elements(By.CSS_SELECTOR, '.flex.items-center.gap-2.rounded-lg.p-2')

    # Go over all tabs and scrape the page html
    for chat in all_chats:
        # Click on a chat to load it
        chat.click()
        # Random sleep time to avoid bot detection and wait for chat to load
        time.sleep(random.randint(2, 5))
        # Get the page html and scrape the data
        page_html = driver.page_source
        scrape(page_html)


# Wait for element with xpath and add random wait time between 2 and 5 seconds
def wait_for(driver, xpath):
    wait = WebDriverWait(driver, 20)
    time.sleep(random.randint(2, 5))
    return wait.until(ec.visibility_of_element_located((By.XPATH, xpath)))

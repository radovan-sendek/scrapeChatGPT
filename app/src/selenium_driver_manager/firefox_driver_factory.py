# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.firefox.options import Options
# from webdriver_manager.firefox import GeckoDriverManager
# from .driver_factory import DriverFactory
#
#
# class FirefoxDriverFactory(DriverFactory):
#     def __init__(self):
#         super().__init__()
#
#     def create_driver(self):
#
#         firefox_options = Options()
#         driver_path = GeckoDriverManager().install()
#
#         #driver_path = "geckodriver"
#
#         # profile = webdriver.FirefoxProfile()
#         #
#         # profile.set_preference("dom.webdriver.enabled", False)
#         # profile.set_preference('useAutomationExtension', False)
#
#         # profile.update_preferences()
#         #desired = DesiredCapabilities.FIREFOX
#
#         webdriver_service = Service(driver_path)
#
#         # firefox_options.add_argument("--disable-blink-features=AutomationControlled")
#         # firefox_options.add_argument(
#         #     "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
#
#         return webdriver.Firefox(service=webdriver_service, options=firefox_options)

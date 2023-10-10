from .chrome_driver_factory import ChromeDriverFactory
# An example of adding a second driver factory
# from .firefox_driver_factory import FirefoxDriverFactory

# List of web browsers for future development, currently only working on Google Chrome
DRIVER_FACTORIES = {
    "chrome": ChromeDriverFactory,
    # An example of adding a second driver factory
    # "firefox": FirefoxDriverFactory,
}


class DriverManager:
    def __init__(self, user_data):
        self.browser_name = user_data.browser
        # Added only for Google Chrome, until the bug is fixed on uc (undetected chromedriver)
        self.chrome_version = user_data.chrome_version

    def get_driver(self):
        manager_class = DRIVER_FACTORIES.get(self.browser_name)
        if not manager_class:
            raise ValueError(f"Unsupported browser {self.browser_name}")

        return manager_class(self.chrome_version).create_driver()

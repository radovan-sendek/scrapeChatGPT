class UserData:
    def __init__(self, os_type):
        self.os_type = os_type
        # Currently only working for Google Chrome, until the bot detection is bypassed for other browsers.
        self.browser = 'chrome'

        self.email = None
        self.password = None
        self.login_type = None
        self.chrome_version = None


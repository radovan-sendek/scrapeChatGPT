import undetected_chromedriver as uc
from .driver_factory import DriverFactory


class ChromeDriverFactory(DriverFactory):
    def __init__(self, version):
        super().__init__()
        self.version = version

    def create_driver(self):

        return uc.Chrome(version_main=int(self.version))


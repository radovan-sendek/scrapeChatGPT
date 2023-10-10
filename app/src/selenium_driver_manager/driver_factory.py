from abc import ABC, abstractmethod


class DriverFactory(ABC):
    """
    Subclasses should implement this method to create a driver instance.
    """
    @abstractmethod
    def create_driver(self):
        pass

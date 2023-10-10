import platform
from tkinter import Tk
from selenium_driver_manager.driver_manager import DriverManager
from selenium_script import run_selenium_script
from ui.app_ui_controller import AppUIController
from user_data import UserData


def main():
    root = Tk()
    root.geometry("500x400")
    root.resizable(width=False, height=False)
    root.title("ChatGPT Scrape")

    os_type = platform.system()
    user_data = UserData(os_type)

    app = AppUIController(root, user_data, start_scrape)

    root.mainloop()


def start_scrape(user_data, update_label):
    try:
        factory = DriverManager(user_data)
        driver = factory.get_driver()
        run_selenium_script(driver, user_data)

    except Exception as e:
        print(e)
        update_label("An error occurred! Please restart the app and try again", "red")


if __name__ == '__main__':
    main()


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

# To bypass the app UI, uncomment from line 40 below and enter credentials here
# If you are using this bypass, comment out line 31

# if __name__ == '__main__':
#     _user_data = UserData(platform.system())
#
#     _user_data.email = "your_email_here"
#     _user_data.password = "your_password_here"
#     # How you log in, using Google, chatGPT, Microsoft or Apple account?
#     # Uncomment corresponding line:
#     # _user_data.login_type = "google"
#     # _user_data.login_type = "chat_gpt"
#     # _user_data.login_type = "microsoft"
#     # _user_data.login_type = "apple"
#
#     # Find the chrome browser version. You can check for version under Settings > Help > About Google Chrome
#     # Example:
#     #_user_data.chrome_version = '117'
#     _user_data.chrome_version = 'chrome_version_number'
#
#     start_scrape(_user_data, None)

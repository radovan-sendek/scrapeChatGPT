import threading
from tkinter import StringVar, W, ttk
from .base_view import BaseView

CONFIG = {
    "Windows": {
        "chrome": "",
        "firefox": "",
        "explorer": ""
    },
    "Linux": {
        "chrome": "https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/115.0.5790.170/linux64"
                  "/chromedriver-linux64.zip",
        "firefox": ""
    },
    "Darwin": {
        "chrome": "",
        "firefox": "",
        "safari": ""
    }
}


def get_browsers_for_os(os_type):
    return CONFIG.get(os_type)


class BrowsersPickView(BaseView):

    def __init__(self, master, controller, user_data, callback):
        super().__init__(master, controller, user_data, callback)

        self.selected_browser_var = StringVar()
        self.selected_browser_url = ""
        self.download_thread_active = False

        browsers = get_browsers_for_os(self.user_data.os_type)

        if browsers:
            self.browsers_label = ttk.Label(self.content_frame, text="Pick your browser to download driver:")
            self.browsers_label.grid(row=0, column=1, pady=10)

            self.content_frame.grid_columnconfigure(0, weight=1)
            self.content_frame.grid_columnconfigure(1, weight=2)
            self.content_frame.grid_columnconfigure(2, weight=1)

            row_num = 1
            for browser, url in browsers.items():
                radio_button = ttk.Radiobutton(self.content_frame, text=browser, variable=self.selected_browser_var,
                                           value=browser)
                radio_button.grid(row=row_num, column=1, sticky=W, pady=5)
                row_num += 1

            self.submit_button = ttk.Button(self.content_frame, text="Submit and Download", command=self.on_submit)
            self.status_label = ttk.Label(self.content_frame, text="")
            self.submit_button.grid(row=999, column=1, pady=10)
            self.status_label.grid(row=1000, column=1, pady=10)
        else:
            self.info_label = ttk.Label(self.content_frame, text="Unsupported Operating System!")
            self.info_label.pack()

    def on_submit(self):
        browser = self.selected_browser_var.get()
        url = self.selected_browser_url

        self.user_data.browser = browser
        self.user_data.browser_driver_url = url

        self.start_download()

    def update_status_label(self, text, color):
        self.status_label.configure(text=text, foreground=color)

    def start_download(self):
        if self.download_thread_active:
            return

        self.submit_button.config(state="disabled")
        self.back_button.config(state="disabled")
        self.download_thread_active = True
        self.update_status_label("Script is running, please wait...", "green")

        try:
            callback_thread = threading.Thread(target=self.callback, args=(self.user_data,))
            callback_thread.start()
            #ova linija je bila i radila dugo, a onda pocela da jebe i prijavljuje da
            # main thread is not in main loop itd itd.
            #self.master.after(5000, self.close_ui)

        except Exception as e:
            print(e)
            self.update_status_label("An error occurred!", "red")

    def close_ui(self):
        self.master.destroy()


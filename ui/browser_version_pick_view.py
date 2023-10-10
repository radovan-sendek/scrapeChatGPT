import threading
from tkinter import StringVar, W, ttk, font
from .base_view import BaseView

VERSIONS = ["115", "116", "117"]


class BrowserVersionPickView(BaseView):

    def __init__(self, master, controller, user_data, callback):
        super().__init__(master, controller, user_data, callback)

        self.selected_version_var = StringVar()
        self.download_thread_active = False

        self.versions_label = ttk.Label(self.content_frame,
                                        text="Which version of chrome/chromium you have?")
        self.versions_label.grid(row=0, column=1, pady=10)

        info_label_font = font.Font(size=8, slant="italic")
        self.info_label = ttk.Label(self.content_frame,
                                    text="You can check for version under Settings > Help > About Google Chrome",
                                    font=info_label_font)
        self.info_label.grid(row=1, column=1, pady=10)

        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=2)
        self.content_frame.grid_columnconfigure(2, weight=1)

        row_num = 2
        for version in VERSIONS:
            radio_button = ttk.Radiobutton(self.content_frame, text=version, variable=self.selected_version_var,
                                           value=version, command=self.on_radio_button_change)
            radio_button.grid(row=row_num, column=1, sticky=W, pady=5)
            row_num += 1

        self.info_text = ttk.Label(self.content_frame, text="Please stand by to complete a CAPTCHA test if prompted!",
                                   wraplength=280)
        self.submit_button = ttk.Button(self.content_frame, text="Start Scraping", state="disabled",
                                        command=self.on_submit)
        self.status_label = ttk.Label(self.content_frame, text="")
        self.info_text.grid(row=998, column=1, pady=10)
        self.submit_button.grid(row=999, column=1, pady=10)
        self.status_label.grid(row=1000, column=1, pady=10)

    def on_submit(self):
        if self.download_thread_active:
            return

        version = self.selected_version_var.get()
        self.user_data.chrome_version = version
        self.update_status_label("", "green")

        self.submit_button.config(state="disabled")
        self.back_button.config(state="disabled")
        self.download_thread_active = True
        self.update_status_label("Script is running, please wait...", "green")

        callback_thread = threading.Thread(target=self.callback, args=(self.user_data, self.update_status_label))
        callback_thread.start()

    def update_status_label(self, text, color):
        self.status_label.configure(text=text, foreground=color)

    def on_radio_button_change(self):
        self.submit_button.config(state="normal")

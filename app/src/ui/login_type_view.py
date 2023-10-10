from tkinter import ttk, font, StringVar, W
from .base_view import BaseView

LOGIN_OPTIONS = {
    "chat_gpt": "Log in using ChatGPT Account",
    "google": "Continue with Google",
    "microsoft": "Continue with Microsoft Account",
    "apple": "Continue with Apple",
}

LOGIN_INFO = {
    "chat_gpt": "",
    "google": "",
    "microsoft": "",
    "apple": "",
}


class LoginTypeView(BaseView):
    def __init__(self, master, controller, user_data):
        super().__init__(master, controller, user_data)
        self.login_type_label = None
        self.info_label = None
        self.submit_button = None

        self.selected_login_type = StringVar()

        self.create_ui_elements()
        self.layout_ui_elements()

    def create_ui_elements(self):
        self.login_type_label = ttk.Label(self.content_frame, text="Pick the way you log in:")
        self.login_type_label.grid(row=0, column=1, pady=10)

        # Create radio buttons based on available options for login.
        row_num = 1
        for login_type, message in LOGIN_OPTIONS.items():
            radio_button = ttk.Radiobutton(self.content_frame, text=message, variable=self.selected_login_type,
                                           value=login_type, command=self.on_radio_button_change)
            radio_button.grid(row=row_num, column=1, sticky=W, pady=5)
            row_num += 1

        info_label_font = font.Font(size=9, slant="italic")
        self.info_label = ttk.Label(self.content_frame, text="", font=info_label_font)
        self.submit_button = ttk.Button(self.content_frame, text="Submit", command=self.on_submit)

    def layout_ui_elements(self):
        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(1, weight=2)
        self.content_frame.grid_columnconfigure(2, weight=1)

        self.info_label.grid(row=999, column=1, pady=10)
        self.submit_button.grid(row=1000, column=1, pady=10)

    def on_submit(self):
        login_type = self.selected_login_type.get()
        self.user_data.login_type = login_type

        self.controller.show_next_view()

    # This method remains in case some more functionality is later needed on radio button change.
    def on_radio_button_change(self):
        self.show_info()

    # Display platform-specific info
    def show_info(self):
        login_type = self.selected_login_type.get()
        text = LOGIN_INFO.get(login_type)
        self.info_label.config(text=text)



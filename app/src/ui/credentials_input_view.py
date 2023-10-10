import re
from tkinter import ttk
from .base_view import BaseView


class CredentialsInputView(BaseView):
    def __init__(self, master, controller, user_data):
        super().__init__(master, controller, user_data)

        self.valid_email = False
        self.confirmed_password = False

        # Widgets
        self.email_label = ttk.Label(self.content_frame, text="Email:")
        self.email_entry = ttk.Entry(self.content_frame)
        self.email_valid_label = ttk.Label(self.content_frame, text="")

        self.password_label = ttk.Label(self.content_frame, text="Enter password:")
        self.password_entry = ttk.Entry(self.content_frame, show="*")

        self.confirm_password_label = ttk.Label(self.content_frame, text="Confirm password:")
        self.confirm_password_entry = ttk.Entry(self.content_frame, show="*")
        self.confirmed_password_label = ttk.Label(self.content_frame, text="")

        self.submit_button = ttk.Button(self.content_frame, text="Submit", state="disabled", command=self.submit)

        # Binding for key release and confirming password
        self.email_entry.bind("<KeyRelease>", self.validate_email)
        self.password_entry.bind("<KeyRelease>", self.confirm_password)
        self.confirm_password_entry.bind("<KeyRelease>", self.confirm_password)

        # Packing the widgets inside a grid
        self.email_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.email_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=2, sticky="ew")
        self.email_valid_label.grid(row=0, column=3, padx=5, pady=5, sticky="w")

        self.password_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5, columnspan=2, sticky="ew")

        self.confirm_password_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.confirm_password_entry.grid(row=2, column=1, padx=5, pady=5, columnspan=2, sticky="ew")
        self.confirmed_password_label.grid(row=2, column=3, padx=5, pady=5, sticky="w")

        self.submit_button.grid(row=3, column=0, columnspan=4, pady=10)

    def submit(self):
        email = self.email_entry.get()
        password = self.password_entry.get()

        self.user_data.email = email
        self.user_data.password = password

        self.controller.show_next_view()

    def validate_email(self, event=None):
        if re.match(r"[^@]+@[^@]+\.[^@]+", self.email_entry.get()):
            self.email_valid_label.config(text="Valid Email", foreground="green")
            self.valid_email = True
        else:
            self.email_valid_label.config(text="Invalid Email", foreground="red")
            self.valid_email = False
        self.update_submit_button_state()

    def confirm_password(self, event=None):
        if (self.password_entry.get() == self.confirm_password_entry.get()) and self.password_entry.get() != "":
            self.confirmed_password_label.config(text="Password Matches", foreground="green")
            self.confirmed_password = True
        else:
            self.confirmed_password_label.config(text="Check Password Again", foreground="red")
            self.confirmed_password = False
        self.update_submit_button_state()

    def update_submit_button_state(self):
        if self.valid_email and self.confirmed_password:
            self.submit_button.config(state="normal")
        else:
            self.submit_button.config(state="disabled")


from .browser_version_pick_view import BrowserVersionPickView
from .credentials_input_view import CredentialsInputView
from .login_type_view import LoginTypeView


class AppUIController:
    def __init__(self, master, user_data, callback):

        # All UI views, in order of appearance
        self.views = [
            LoginTypeView(master, self, user_data),
            CredentialsInputView(master, self, user_data),
            BrowserVersionPickView(master, self, user_data, callback),
        ]
        self.current_view_index = 0
        self.show_current_view()

    def show_current_view(self):
        for index, view in enumerate(self.views):
            if index == self.current_view_index:
                view.pack(fill="both", expand=True)
            else:
                view.pack_forget()

    def show_next_view(self):
        if self.current_view_index < len(self.views) - 1:
            self.current_view_index += 1
            self.show_current_view()

    def show_previous_view(self):
        if self.current_view_index > 0:
            self.current_view_index -= 1
            self.show_current_view()

    # Method not used, left for future development
    def skip_view(self, num):
        if self.current_view_index < len(self.views) - (num + 1):
            self.current_view_index += (num + 1)
            self.show_current_view()

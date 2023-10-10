from tkinter import ttk


class BaseView:
    def __init__(self, master, controller, user_input, callback=None):
        self.master = master
        self.controller = controller
        self.user_data = user_input
        self.callback = callback

        self.frame = ttk.Frame(master)

        self.header_frame = ttk.Frame(self.frame)
        self.header_frame.grid(row=0, column=0, sticky="NSEW")

        self.content_frame = ttk.Frame(self.frame)
        self.content_frame.grid(row=1, column=0, sticky="NSEW")

        self.back_button = ttk.Button(self.header_frame, text="Back", command=self.controller.show_previous_view)
        self.back_button.grid(row=0, column=0, pady=5, padx=10, sticky="W")

        self.center_content()

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def pack_forget(self):
        self.frame.pack_forget()

    def center_content(self):
        self.content_frame.grid_rowconfigure(0, weight=1)
        self.content_frame.grid_columnconfigure(0, weight=1)

        content_width = self.content_frame.winfo_reqwidth()
        content_height = self.content_frame.winfo_reqheight()

        x = (content_width // 2)
        y = (content_height // 2)

        self.content_frame.place(in_=self.frame, anchor="center", relx=0.5, rely=0.5, x=x, y=y)


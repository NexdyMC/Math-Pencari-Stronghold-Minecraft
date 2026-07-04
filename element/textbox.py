import customtkinter as ctk

class TextBox(ctk.CTkTextbox):
    def __init__(self, master):
        super().__init__(master)

        self.configure(
            fg_color="#fff",
            text_color="#000"
        )


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x200")
        self.title("Project Website")

        self.input = TextBox(self)
        self.input.pack(fill="x",expand=True)

if __name__ == "__main__":
    app = App()
    app.mainloop()
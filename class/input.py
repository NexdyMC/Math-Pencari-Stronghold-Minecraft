import customtkinter as ctk

class Input(ctk.CTkEntry):
    def __init__(self, master):
        super().__init__(master)

        self.configure(
            placeholder_text="Masukkan nama",
            width=200
        )

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x200")
        self.title("Project Website")

        self.input = Input(self)
        self.input.pack(pady=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()
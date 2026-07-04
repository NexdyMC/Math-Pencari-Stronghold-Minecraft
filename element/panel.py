import customtkinter as ctk

class Panel(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.configure(
            fg_color="#1ff",
            # bg_color="#1ff",
            corner_radius=999
        )

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x200")
        self.title("Project Website")

        self.input = Panel(self)
        self.input.pack(fill="x",expand=True)


if __name__ == "__main__":
    app = App()
    app.mainloop()

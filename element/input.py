import customtkinter as ctk

class Input(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master)

        self.configure(
            font=('Minecraft', 16),
            **kwargs
            # width=200,
        )
    
    def RowColumn(self, row=0, column=0):
        self.grid(row=row, column=column, sticky="w")



class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x200")
        self.title("Project Website")

        self.input = Input(self).RowColumn(0,0)

if __name__ == "__main__":
    app = App()
    app.mainloop()
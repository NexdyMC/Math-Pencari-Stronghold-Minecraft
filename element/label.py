import customtkinter as ctk

class Label(ctk.CTkLabel):
    def __init__(self, master, text="Label", **kwargs):
        super().__init__(master)

        self.configure(
            text=text,
            font=('Minecraft', 16),
            **kwargs
        )

    def text_color(self, text_color="white"):
        self.configure(text_color=text_color)

    def RowColumn(self, row=0, column=0):
        self.grid(row=row, column=column, sticky="w")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x400")
        self.title("Custom Tkinter")

        self.label = Label(self, "this is a makanan", bg_color="#0ff").RowColumn(0,0 )
        # self.label.text_color("blue")
        # self.label.pack(fill="x")

if __name__ ==  "__main__":
    app = App()
    app.mainloop()
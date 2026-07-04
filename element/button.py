import customtkinter as ctk

class Button(ctk.CTkButton):
    def __init__(self, master, text="Button Click", **kwargs):
        super().__init__(master)

        self.configure(
            text=text,
            corner_radius=0,
            font=('Minecraft', 16),
            **kwargs
        )

    def text_color(self, value="white"):
        self.configure(text_color=value)
    
    def RowColumn(self, row=0, column=0):
        self.grid(row=row, column=column)

# class App(ctk.CTk):
#     def __init__(self):
#         super().__init__()

#         self.geometry("400x200")
#         self.title("Project Website")

#         self.input = Button(self, "KETIK BUTTON")
#         self.input.text_color("#f0f")

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

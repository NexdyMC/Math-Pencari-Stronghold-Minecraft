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
    
    def RowColumn(self, row=0, column=0, sticky="w"):
        self.grid(row=row, column=column, sticky=sticky)
        return self  # <--- TAMBAHKAN INI

    def Padding(self, padx=0, pady=0):
        self.grid(padx=padx, pady=pady)
        return self  # <--- TAMBAHKAN INI
    
    
    @property
    def Text(self):
        return self.cget("text")

    @Text.setter
    def Text(self, value):
        self.configure(text=value)


    # def ShortCut(self)
        # | Enter	        | <Return>
        # | Ctrl + V	    | <Control-v>
        # | Ctrl + S	    | <Control-s>
        # | Esc             | <Escape>
        # | F1 - F12	    | <F1>, <F2>, dst.
        # | Panah top	    | <Up>
        # | Shift + Enter	| <Shift-Return>

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

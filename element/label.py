import customtkinter as ctk

class Label(ctk.CTkLabel):
    def __init__(self, master, text="Label", font=('Minecraft', 16), **kwargs):
        super().__init__(master)
        self.configure(
            text=text,
            font=font,
            **kwargs
        )

    def text_color(self, text_color="white"):
        self.configure(text_color=text_color)
        return self

    def RowColumn(self, row=0, column=0, sticky="w"):
        self.grid(row=row, column=column, sticky=sticky)
        return self

    def Padding(self, padx=0, pady=0):
        self.grid(padx=padx, pady=pady)
        return self  # <--- TAMBAHKAN INI
    
    
    def Span(self, row=None, column=None):
        # Menggunakan grid_configure untuk memperbarui span tanpa reset grid
        grid_args = {}
        if row: grid_args['rowspan'] = row
        if column: grid_args['columnspan'] = column
        
        self.grid_configure(**grid_args)
        return self

    # Tambahan: Property decorator agar bisa pakai .Text = "..."
    @property
    def Text(self):
        return self.cget("text")

    @Text.setter
    def Text(self, value):
        self.configure(text=value)
    
    def getValue(self):
        self.get()
# class App(ctk.CTk):
#     def __init__(self):
#         super().__init__()

#         self.geometry("400x400")
#         self.title("Custom Tkinter")

#         self.label = Label(self, "this is a makanan", bg_color="#0ff").RowColumn(0,0 )
#         # self.label.text_color("blue")
#         # self.label.pack(fill="x")

# if __name__ ==  "__main__":
#     app = App()
#     app.mainloop()
import customtkinter as ctk
# from label import Label

class Panel(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        # Pastikan corner_radius default adalah 0
        if "corner_radius" not in kwargs:
            kwargs["corner_radius"] = 0
        super().__init__(master, **kwargs)
        
        # Simpan state grid agar tidak hilang saat update padding
        self.grid_options = {"row": 0, "column": 0, "padx": 0, "pady": 0,"rowspan": 0, "columnspan": 0, "columnspan": 1, "sticky": "nsew"}

    def RowColumn(self, row=0, column=0, sticky="w"):
        self.grid(row=row, column=column, sticky=sticky)
        return self  # <--- TAMBAHKAN INI

    def Span(self, rowspan=0, columnspan=0):
        self.grid(rowspan=rowspan, columnspan=columnspan)
        return self  # <--- TAMBAHKAN INI

    def Padding(self, padx=0, pady=0):
        self.grid(padx=padx, pady=pady)
        return self  # <--- TAMBAHKAN INI

# class App(ctk.CTk):
#     def __init__(self):
#         super().__init__()

#         self.geometry("400x200")
#         self.title("Project Website")

#         self.input = Panel(self, fg_color="#0ff")
#         self.input.pack(fill="x",expand=True)

#         Label(self.input, "this is a panel").RowColumn(0,0 )


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()

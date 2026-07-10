import customtkinter as ctk

class Input(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master)

        self.configure(
            font=('Minecraft', 16),
            **kwargs
            # width=200,
        )
    
    def RowColumn(self, row=0, column=0, sticky="w"):
        self.grid(row=row, column=column, sticky=sticky)
        return self  # <--- TAMBAHKAN INI

    def Padding(self, padx=0, pady=0):
        self.grid(padx=padx, pady=pady)
        return self  # <--- TAMBAHKAN INI
    
    def getValue(self):
        return self.get()

    @property
    def Value(self):
        return self.cget("value")

    @Value.setter
    def Value(self, value):
        self.configure(textvariable=ctk.StringVar(value=value))
   


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("400x200")
        self.title("Project Website")

        self.input = Input(self).RowColumn(0,0)
    #     self.button = ctk.CTkButton(self, text="tekan aku", command=self.click_output).grid(row=1, column=1)
    #     self.label = ctk.CTkLabel(self, text="output").grid(row=2, column=1)

    # def click_output(self):
    #     self.configure(text="ini hasilnya")
if __name__ == "__main__":
    app = App()
    app.mainloop()
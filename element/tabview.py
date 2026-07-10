import customtkinter as ctk

class TabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

    def Radius(self, value):
        self.configure(corner_radius=value)
        return self

    def Add(self, name):
        self.add(name)
        return self

    def Tab(self, name):
        return self.tab(name)

    def RowColumn(self, row=0, column=0, sticky="nsew"):
        self.grid(row=row, column=column, sticky=sticky)
        return self

    def Padding(self, padx=0, pady=0):
        self.grid(padx=padx, pady=pady)
        return self
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x400")

        self.tabs = (
            TabView(self)
            .RowColumn(0, 0)
            .Padding(10, 10)
        )

        self.tabs.Add("Home")
        self.tabs.Add("Settings")
        self.tabs.Add("About")

        ctk.CTkLabel(
            self.tabs.Tab("Home"),
            text="Welcome"
        ).pack(pady=20)


if __name__ == "__main__":
    App().mainloop()
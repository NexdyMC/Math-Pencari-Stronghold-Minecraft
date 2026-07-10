import customtkinter as ctk

import customtkinter as ctk


class TabView(ctk.CTkTabview):
    def __init__(self, master, **kwargs):
        super().__init__(master)

        self.configure(
            corner_radius=0,
            **kwargs
        )

    def Add(self, name):
        self.add(name)
        return self

    def Remove(self, name):
        self.delete(name)
        return self

    def GetTab(self, name):
        return self.tab(name)

    def RowColumn(self, row=0, column=0, sticky="nsew"):
        self.grid(row=row, column=column, sticky=sticky)
        return self

    def Padding(self, padx=0, pady=0):
        self.grid(padx=padx, pady=pady)
        return self

    @property
    def CurrentTab(self):
        return self.get()

    @CurrentTab.setter
    def CurrentTab(self, value):
        self.set(value)


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("600x400")
        self.title("Tab Example")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.tabs = (
            TabView(self)
            .RowColumn(0, 0, "nsew")
            .Padding(10, 10)
        )

        self.tabs.Add("Home")
        self.tabs.Add("Settings")
        self.tabs.Add("Profile")

        ctk.CTkLabel(
            self.tabs.GetTab("Home"),
            text="Welcome Home"
        ).pack(pady=20)

        ctk.CTkButton(
            self.tabs.GetTab("Settings"),
            text="Save"
        ).pack(pady=20)

        ctk.CTkLabel(
            self.tabs.GetTab("Profile"),
            text="User Profile"
        ).pack(pady=20)


if __name__ == "__main__":
    app = App()
    app.mainloop()
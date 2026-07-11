import customtkinter as ctk


class TabView(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.tabs = {}
        self.current = None

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.tab_bar = ctk.CTkFrame(self, corner_radius=0)
        self.tab_bar.grid(row=0, column=0, sticky="ew")

        self.content = ctk.CTkFrame(self, corner_radius=0)
        self.content.grid(row=1, column=0, sticky="nsew")

    def Add(self, name):

        page = ctk.CTkFrame(self.content)

        btn = ctk.CTkButton(
            self.tab_bar,
            text=name,
            width=120,
            corner_radius=0,
            command=lambda: self.Show(name)
        )

        btn.pack(side="left")

        self.tabs[name] = {
            "button": btn,
            "page": page
        }

        if self.current is None:
            self.Show(name)

        return page

    def Show(self, name):

        for tab in self.tabs.values():
            tab["page"].pack_forget()

        self.tabs[name]["page"].pack(
            fill="both",
            expand=True
        )

        self.current = name

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("800x500")

        tabs = TabView(self)
        tabs.pack(fill="both", expand=True)

        home = tabs.Add("Home")
        about = tabs.Add("About")
        settings = tabs.Add("Settings")

        ctk.CTkLabel(
            home,
            text="HOME PAGE"
        ).pack(pady=30)

        ctk.CTkLabel(
            about,
            text="ABOUT PAGE"
        ).pack(pady=30)

        ctk.CTkLabel(
            settings,
            text="SETTINGS PAGE"
        ).pack(pady=30)


App().mainloop()
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

    def ButtonTabView(
        self,
        font=("Minecraft", 14),
        fg_color="#334155",
        hover_color="#475569",
        text_color="white",
        width=100,
        height=32
    ):
        self._tab_style = {
            "font": font,
            "fg_color": fg_color,
            "hover_color": hover_color,
            "text_color": text_color,
            "width": width,
            "height": height
        }

        for tab in self.tabs.values():
            tab["button"].configure(**self._tab_style)

        return self

    def Add(self, name):

        style = getattr(self, "_tab_style", {})
        page = ctk.CTkFrame(self.content)
        btn = ctk.CTkButton(
            self.tab_bar,
            text=name,
            corner_radius=0,
            command=lambda: self.Show(name),
            **style
        )

        btn.pack(side="left", padx=0, pady=0)

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

    def RowColumn(self, row=0, column=0, sticky="nsew"):
        self.grid(row=row, column=column, sticky=sticky)
        return self

    def Padding(self, padx=0, pady=0):
        self.grid(padx=padx, pady=pady)
        return self
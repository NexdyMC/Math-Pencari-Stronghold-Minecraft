import customtkinter as ctk


class Font(ctk.CtkFont):
    def __init__(self, master):
        super().__init__(master)

        self.configure(
            family="Minecraft", size=12
        )
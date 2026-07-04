import customtkinter as ctk

class CTkCode(ctk.CTkFrame):
    """Widget khusus untuk input kode/teks monospaced"""
    def __init__(self, master, **kwargs):
        super().__init__(master, fg_color="transparent")
        
        self.entry = ctk.CTkEntry(
            self, 
            font=("Courier New", 14), 
            **kwargs
        )
        self.entry.pack(fill="x", expand=True)

    def get(self):
        return self.entry.get()

# Penggunaan
app = ctk.CTk()
app.geometry("400x200")

# Menggunakan widget kustom kita
code_input = CTkCode(app, placeholder_text="Masukkan kode di sini...")
code_input.pack(pady=20, padx=20, fill="x")

app.mainloop()
import customtkinter as ctk

def aksi_tombol():
    print("Tombol ditekan!")

app = ctk.CTk()
app.geometry("300x200")
app.title("CustomTkinter Button States")

# Membuat tombol dengan konfigurasi status
btn = ctk.CTkButton(
    app,
    text="Klik Saya",
    # 1. Normal State (Warna dasar)
    fg_color="#4CAF50",
    
    # 2. Hover State (Warna saat kursor di atas tombol)
    hover_color="#45a049",
    
    # 3. Active/Pressed State 
    # (CTK tidak memiliki parameter 'active_color' eksplisit, 
    # jadi kita bisa menggunakan event binding untuk efek lebih dalam)
    command=aksi_tombol
)
btn.pack(pady=20)

# 4. Disable State
# Tombol di-disable (tidak bisa diklik dan warna berubah otomatis)
btn_disabled = ctk.CTkButton(app, text="Disabled", state="disabled")
btn_disabled.pack(pady=20)

app.mainloop()
import customtkinter as ctk
import math

def to_screen_coords(x, y, cx, cy):
    """Konversi koordinat matematika ke koordinat Canvas Tkinter."""
    return cx + x, cy - y

def draw_line(canvas, coordX, coordY, radius, color):
    """
    Fungsi menggambar garis dari titik (0,0) matematika 
    ke titik hasil rotasi berdasarkan radius (sudut).
    """
    cx, cy = 150, 150
    angle_rad = math.radians(radius)
    
    # Menghitung titik akhir garis berdasarkan sudut
    # Panjang garis diasumsikan 100 unit
    length = 200
    end_x = coordX + length * math.cos(angle_rad)
    end_y = coordY + length * math.sin(angle_rad)
    
    # Konversi ke koordinat layar
    start = to_screen_coords(coordX, coordY, cx, cy)
    end = to_screen_coords(end_x, end_y, cx, cy)
    
    canvas.create_line(start[0], start[1], end[0], end[1], fill=color, width=3)

# Setup Aplikasi
app = ctk.CTk()
app.geometry("300x300")
app.title("Garis Bertabrakan")

canvas = ctk.CTkCanvas(app, width=300, height=300, bg="white")
canvas.pack()

# Memanggil fungsi sebanyak 2 kali untuk membuat garis yang bersilangan
# Garis 1: dari pusat (0,0) sudut 45 derajat
draw_line(canvas, 100, 100, -111, "red")

# Garis 2: dari pusat (0,0) sudut 135 derajat agar bertabrakan
draw_line(canvas, 96, 89, -81, "blue")

# Teks keterangan
canvas.create_text(150, 20, text="ini adalah garis", fill="black", font=("Arial", 12))

app.mainloop()
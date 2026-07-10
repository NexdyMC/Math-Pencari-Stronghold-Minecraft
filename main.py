import customtkinter as ctk
from element.button import Button 
from element.label  import Label
from element.input  import Input
from element.panel  import Panel
from mate import rumus
import math

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # self.geometry("400x200")
        self.title("Calculator Stronghold")
        # self.iconbitmap("icon.ico")
        # self.configure(bg_color="#0ff")
        self.resizable(False, False)
        # self.grid_columnconfigure(0, weight=1, pad=5) # Padding kiri
        # self.grid_columnconfigure(2, weight=1, pad=5) # Padding kanan
        # self.grid_rowconfigure(0, weight=1, pad=5)    # Padding atas
        # self.grid_rowconfigure(2, weight=1, pad=5)    # Padding bawah

        self.panel_windows = Panel(self)
        self.panel_windows.grid(row=1, column=1, sticky="nsew")

        # Panel Screen
        self.panel_input = Panel(self.panel_windows, fg_color="#222")
        self.panel_input.pack(fill="x", expand=True)
        
        self.panel_button = Panel(self.panel_windows, fg_color="#1a1a1a")
        self.panel_button.pack(fill="x", expand=True)

        self.panel_hasil = Panel(self.panel_windows, fg_color="#444")
        self.panel_hasil.pack(fill="x", expand=True)


        # Label(self.panel_input, "Ender Eye 1: ", width=120).pack()
        
        # # label
        Label(self.panel_input, "Ender Eye 1: ", width=120).RowColumn(1,0)       
        Label(self.panel_input, "Ender Eye 2: ", width=120).RowColumn(2,0)
        
        Label(self.panel_input, "Coord X", width=80).RowColumn(0,1)
        Label(self.panel_input, "Coord Y", width=80).RowColumn(0,2)
        Label(self.panel_input, "Radient", width=80).RowColumn(0,3)

        # Input 
        self.coordX1 = Input(self.panel_input, width=80, fg_color="#272727", corner_radius=0, border_width=0).RowColumn(1, 1).Padding(2, 2)
        self.coordZ1 = Input(self.panel_input, width=80, fg_color="#272727", corner_radius=0, border_width=0).RowColumn(1, 2).Padding(2, 2)
        self.angle1 = Input(self.panel_input, width=80, fg_color="#272727", corner_radius=0, border_width=0).RowColumn(1, 3).Padding(2, 2)
        
        self.coordX2 = Input(self.panel_input, width=80, fg_color="#272727", corner_radius=0, border_width=0).RowColumn(2, 1).Padding(2, 2)
        self.coordZ2 = Input(self.panel_input, width=80, fg_color="#272727", corner_radius=0, border_width=0).RowColumn(2, 2).Padding(2, 2)
        self.angle2 = Input(self.panel_input, width=80, fg_color="#272727", corner_radius=0, border_width=0).RowColumn(2, 3).Padding(2, 2)
        
        Label(self.panel_hasil, "Dimension", width=120, fg_color="#0e7490").RowColumn(4,0)
        Label(self.panel_hasil, "Block", width=140, fg_color="#0e7490").RowColumn(4,1).Span(0, 2)
        Label(self.panel_hasil, "Chunk", width=140, fg_color="#0e7490").RowColumn(4,3).Span(0, 2)
        
        Label(self.panel_hasil, "Overworld", width=120, fg_color="#070").RowColumn(5,0)
        self.world_block_x = Label(self.panel_hasil, "-1200", width=70, fg_color="#112D10").RowColumn(5,1)
        self.world_block_y = Label(self.panel_hasil, "-2800", width=70, fg_color="#112D10").RowColumn(5,2)
        self.world_chunk_x = Label(self.panel_hasil, "-2800", width=70, fg_color="#123C10").RowColumn(5,3)
        self.world_chunk_y = Label(self.panel_hasil, "-2800", width=70, fg_color="#123C10").RowColumn(5,4)
        
        Label(self.panel_hasil, "Nether", width=120, fg_color="#700").RowColumn(6,0)
        self.nether_block_x = Label(self.panel_hasil, "-2800", width=70, fg_color="#3F0F0B").RowColumn(6,1)
        self.nether_block_y = Label(self.panel_hasil, "-2800", width=70, fg_color="#3F0F0B").RowColumn(6,2)
        self.nether_chunk_x = Label(self.panel_hasil, "-2800", width=70, fg_color="#580000").RowColumn(6,3)
        self.nether_chunk_y = Label(self.panel_hasil, "-2800", width=70, fg_color="#580000").RowColumn(6,4)
        
        # # Button 
        self.btn_search = Button(self.panel_button, command=self.on_return_pressed, hover_color="#14532d", fg_color="#166534").RowColumn(3, 0).Padding(2 ,2)
        self.btn_search.Text = "Search" 
        # self.bind("<Return>", self.on_return_pressed)
        
        self.btn_remove = Button(self.panel_button, command=self.on_remove_pressed, hover_color="#7f1d1d", fg_color="#b91c1c").RowColumn(3, 1).Padding(2 ,2)
        self.btn_remove.Text = "Reset" 
        # self.bind("<Control-Return>", self.on_remove_pressed)
        
        
    def on_return_pressed(self):
        coordxA = float(self.coordX1.getValue())
        coordzA = float(self.coordZ1.getValue())
        angleA = float(self.angle1.getValue())
        coordxB = float(self.coordX2.getValue())
        coordzB = float(self.coordZ2.getValue())
        angleB = float(self.angle2.getValue())

        hasil = rumus.coord(coordxA, coordzA, angleA, coordxB, coordzB, angleB)
        # hasil = rumus.coord(1000, 1000, coordxB, coordzB, angleA, angleB)
        self.world_block_x.Text = hasil[0]
        self.world_block_y.Text = hasil[1]
        self.world_chunk_x.Text = hasil[0]
        self.world_chunk_y.Text = hasil[1]
    
        self.nether_block_x.Text = hasil[0]
        self.nether_block_y.Text = hasil[1]
        self.nether_chunk_x.Text = hasil[0]
        self.nether_chunk_y.Text = hasil[1]
        
    def on_remove_pressed(self):
        self.world_block_x.Text = ""
        self.world_block_y.Text = ""
        self.world_chunk_x.Text = ""
        self.world_chunk_y.Text = ""
    
        self.nether_block_x.Text = ""
        self.nether_block_y.Text = ""
        self.nether_chunk_x.Text = ""
        self.nether_chunk_y.Text = ""

    def calculate_stronghold(self, coordX1, coordY1, rad1, coordX2, coordY2, rad2):
        deg2rad = (math.pi / 180)
        rad2deg = (180 / math.pi)
        pass

if __name__ == "__main__":
    app = App()
    app.mainloop()

import customtkinter as ctk
from element.button import Button 
from element.label  import Label
from element.input  import Input
from element.panel  import Panel
from element.textbox  import TextBox
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

        self.panel_windows = Panel(self)
        self.panel_windows.grid(row=1, column=1, sticky="nsew")

        # Panel Screen
        self.panel_input = Panel(self.panel_windows, fg_color="#222")
        self.panel_input.pack(fill="x", expand=True)
        
        self.panel_button = Panel(self.panel_windows, fg_color="#1a1a1a")
        self.panel_button.pack(fill="x", expand=True)

        self.panel_hasil = Panel(self.panel_windows, fg_color="#444")
        self.panel_hasil.pack(fill="x", expand=True)

        # self.boxtext = TextBox(self.panel_input, width=400).RowColumn(0, 0)
        Label(self.panel_input)
        Label(self.panel_input, text="Command A").RowColumn(1,0).Padding((4, 10), 0)
        self.CommandA = Input(self.panel_input, width=300, fg_color="#272727", corner_radius=0, border_width=1).RowColumn(1, 1)
        Label(self.panel_input, text="Command B").RowColumn(2,0).Padding((4, 10), 0)
        self.CommandB = Input(self.panel_input, width=300, fg_color="#272727", corner_radius=0, border_width=1).RowColumn(2, 1)
        Label(self.panel_input, text="Gunakan F3 + C untuk mencopy sebuah perintah", text_color="#070", font=('Minecraft', 14)).RowColumn(3, 0).Span(column=2).Padding(4, 6)

        Label(self.panel_hasil, "Dimension", width=120, fg_color="#0e7490").RowColumn(4,0)
        Label(self.panel_hasil, "Block", width=140, fg_color="#0e7490").RowColumn(4,1).Span(0, 2)
        Label(self.panel_hasil, "Chunk", width=140, fg_color="#0e7490").RowColumn(4,3).Span(0, 2)
        
        Label(self.panel_hasil, "Overworld", width=120, fg_color="#070").RowColumn(5,0)
        self.world_block_x = Label(self.panel_hasil, "000", width=70, fg_color="#112D10").RowColumn(5,1)
        self.world_block_y = Label(self.panel_hasil, "000", width=70, fg_color="#112D10").RowColumn(5,2)
        self.world_chunk_x = Label(self.panel_hasil, "000", width=70, fg_color="#123C10").RowColumn(5,3)
        self.world_chunk_y = Label(self.panel_hasil, "000", width=70, fg_color="#123C10").RowColumn(5,4)
        
        Label(self.panel_hasil, "Nether", width=120, fg_color="#700").RowColumn(6,0)
        self.nether_block_x = Label(self.panel_hasil, "000", width=70, fg_color="#3F0F0B").RowColumn(6,1)
        self.nether_block_y = Label(self.panel_hasil, "000", width=70, fg_color="#3F0F0B").RowColumn(6,2)
        self.nether_chunk_x = Label(self.panel_hasil, "000", width=70, fg_color="#580000").RowColumn(6,3)
        self.nether_chunk_y = Label(self.panel_hasil, "000", width=70, fg_color="#580000").RowColumn(6,4)
        
        # # Button 
        self.btn_search = Button(self.panel_button, command=self.on_return_pressed, hover_color="#14532d", fg_color="#166534").RowColumn(3, 0).Padding(2 ,2)
        self.btn_search.Text = "Search" 
        # self.bind("<Return>", self.on_return_pressed)
        
        self.btn_remove = Button(self.panel_button, command=self.on_remove_pressed, hover_color="#7f1d1d", fg_color="#b91c1c").RowColumn(3, 1).Padding(2 ,2)
        self.btn_remove.Text = "Reset" 
        # self.bind("<Control-Return>", self.on_remove_pressed)
        
        
    def on_return_pressed(self):
        pointA = self.CommandA.getValue().split()
        pointB = self.CommandB.getValue().split()

        print(f"Point A: {pointA[6]} {pointA[8]} {pointA[9]}")
        print(f"Point B: {pointB[6]} {pointB[8]} {pointB[9]}")

        hasil = rumus.coord(float(str(pointA[6])), float(str(pointA[8])), float(str(pointA[9])), float(str(pointB[6])), float(str(pointB[8])), float(str(pointB[9])))
        
        overworld_block = rumus.overword_block(hasil[0], hasil[1])
        overworld_chunk = rumus.overword_chunk(hasil[0], hasil[1])
        nether_block = rumus.nether_block(hasil[0], hasil[1])
        nether_chunk = rumus.nether_chunk(hasil[0], hasil[1])
        
        self.world_block_x.Text = str(overworld_block[1])
        self.world_block_y.Text = str(overworld_block[2])
        self.world_chunk_x.Text = str(overworld_chunk[1])
        self.world_chunk_y.Text = str(overworld_chunk[2])
    
        self.nether_block_x.Text = str(nether_block[1])
        self.nether_block_y.Text = str(nether_block[2])
        self.nether_chunk_x.Text = str(nether_chunk[1])
        self.nether_chunk_y.Text = str(nether_chunk[2])
        
    def on_remove_pressed(self):
        self.CommandA.Value = ""
        self.CommandB.Value = ""
        
        self.world_block_x.Text = ""
        self.world_block_y.Text = ""
        self.world_chunk_x.Text = ""
        self.world_chunk_y.Text = ""
    
        self.nether_block_x.Text = ""
        self.nether_block_y.Text = ""
        self.nether_chunk_x.Text = ""
        self.nether_chunk_y.Text = ""

if __name__ == "__main__":
    app = App()
    app.mainloop()

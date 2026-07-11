import customtkinter as ctk
from element.button import Button 
from element.label  import Label
from element.input  import Input
from element.panel  import Panel
from element.tabview import TabView
from mate import rumus

import math

class Screen(ctk.CTk):
    def InputManual():
        pass
    def InputPaste():
        pass
    def ButtonManual():
        pass
    def ButtonManual():
        pass
    def Output():
        pass
    def MenuManual():
        pass
    def MenuPaste():
        pass
    def MenuOption():
        pass
    def MenuAbout():
        pass

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # self.geometry("400x200")
        self.title("Calculator Stronghold")
        # self.iconbitmap("icon.ico")
        self.resizable(False, False)

        self.panel_windows = Panel(self)
        self.panel_windows.grid(row=1, column=1, sticky="nsew")

        # Panel Screen
        self.panel_input = Panel(self.panel_windows, fg_color="#222")
        self.panel_input.pack(fill="x", expand=True)

        self.panel_hasil = Panel(self.panel_windows, fg_color="#444")
        self.panel_hasil.pack(fill="x", expand=True)

        self.tabs = TabView(self.panel_input)
        self.tabs.ButtonTabView(fg_color="#2f4538", hover_color="#3f5d4b", text_color="white")
        self.tabs.RowColumn(0, 0)

        self.content_manual = self.tabs.Add("Manual") 
        self.content_paste  = self.tabs.Add("F3 + C") 
        self.content_option  = self.tabs.Add("Option") 
        self.content_about  = self.tabs.Add("About") 

        self.tab_manual_input = Panel(self.content_manual, fg_color="#333")
        self.tab_manual_input.pack(fill="x", expand=True)
        self.tab_manual_event = Panel(self.content_manual, fg_color="#1a1a1a")
        self.tab_manual_event.pack(fill="x", expand=True)
        
        self.tab_paste_input = Panel(self.content_paste, fg_color="#333")
        self.tab_paste_input.pack(fill="x", expand=True)
        self.tab_paste_event = Panel(self.content_paste, fg_color="#1a1a1a")
        self.tab_paste_event.pack(fill="x", expand=True)

        self.panel_option = Panel(self.content_option, fg_color="#333")
        self.panel_option.pack(fill="x", expand=True)
        
        self.panel_about = Panel(self.content_about, fg_color="#333")
        self.panel_about.pack(fill="x", expand=True)
        

        # ============================================================ #
        # ======================== Menu Option ======================== #
        # ============================================================ #

        Label(self.panel_option, text="Username").RowColumn(1, 0)
        Input(self.panel_option).RowColumn(1, 1)
        Label(self.panel_option, text="Email").RowColumn(2, 0)
        Input(self.panel_option).RowColumn(2, 1)
        Label(self.panel_option, text="Password").RowColumn(3, 0)
        Input(self.panel_option).RowColumn(3, 1)

        # ============================================================ #
        # ======================== Menu About ======================== #
        # ============================================================ #
        Label(self.panel_about, text="Username").RowColumn(1, 0)
        
        # ============================================================ #
        # ======================== Menu Manual ======================== #
        # ============================================================ #

        
        # label : Panel Input : Mode Manual
        # ==================================
        Label(self.tab_manual_input, text="Mode Manual", width=400).RowColumn(0, 0).Span(column=4)
        Label(self.tab_manual_input, "Ender Eye 1: ", width=120).RowColumn(2,0)       
        Label(self.tab_manual_input, "Ender Eye 2: ", width=120).RowColumn(3,0)
        Label(self.tab_manual_input, "Coord X", width=80).RowColumn(1,1)
        Label(self.tab_manual_input, "Coord Y", width=80).RowColumn(1,2)
        Label(self.tab_manual_input, "Radient", width=80).RowColumn(1,3)

        self.coordX1 = Input(self.tab_manual_input, width=80, fg_color="#272727").RowColumn(2, 1).Padding(2, 2)
        self.coordZ1 = Input(self.tab_manual_input, width=80, fg_color="#272727").RowColumn(2, 2).Padding(2, 2)
        self.angle1 = Input(self.tab_manual_input, width=80, fg_color="#272727").RowColumn(2, 3).Padding(2, 2)
        self.coordX2 = Input(self.tab_manual_input, width=80, fg_color="#272727").RowColumn(3, 1).Padding(2, 2)
        self.coordZ2 = Input(self.tab_manual_input, width=80, fg_color="#272727").RowColumn(3, 2).Padding(2, 2)
        self.angle2 = Input(self.tab_manual_input, width=80, fg_color="#272727").RowColumn(3, 3).Padding(2, 2)
        

        # Button : Panel Event : Mode Manual
        # ==================================
        self.btn_search = Button(self.tab_manual_event, command=self.on_return_manual_pressed, hover_color="#14532d", fg_color="#166534").RowColumn(3, 0).Padding(2 ,2)
        self.btn_search.Text = "Enter" 
        self.bind("<Return>", self.on_return_manual_pressed)
        self.btn_remove = Button(self.tab_manual_event, command=self.on_remove_paste_pressed, hover_color="#7f1d1d", fg_color="#b91c1c").RowColumn(3, 1).Padding(2 ,2)
        self.btn_remove.Text = "Reload" 
        self.bind("<Control-Return>", self.on_remove_paste_pressed)

        # ============================================================ #
        # ======================== Menu Paste ======================== #
        # ============================================================ #

        # Input : Panel Input : Mode F3 + C
        # ==================================
        Label(self.tab_paste_input, text="Mode F3 + C", anchor="center", width=400).RowColumn(0,0).Span(column=2)
        Label(self.tab_paste_input, text="Command A").RowColumn(1,0).Padding((4, 10), 0)
        self.CommandA = Input(self.tab_paste_input, width=300, fg_color="#272727").RowColumn(1, 1)
        Label(self.tab_paste_input, text="Command B").RowColumn(2,0).Padding((4, 10), 0)
        self.CommandB = Input(self.tab_paste_input, width=300, fg_color="#272727").RowColumn(2, 1)
        Label(self.tab_paste_input, text="Gunakan F3 + C untuk mencopy sebuah perintah", text_color="#070", font=('Minecraft', 14)).RowColumn(3, 0).Span(column=2).Padding(4, 0)

        
        # Button : Panel Event : Mode F3 + C
        # ==================================
        self.btn_search = Button(self.tab_paste_event, command=self.on_return_paste_pressed, hover_color="#14532d", fg_color="#166534").RowColumn(3, 0).Padding(2 ,2)
        self.btn_search.Text = "Search" 
        self.bind("<Return>", self.on_return_paste_pressed)
        self.btn_remove = Button(self.tab_paste_event, command=self.on_remove_paste_pressed, hover_color="#7f1d1d", fg_color="#b91c1c").RowColumn(3, 1).Padding(2 ,2)
        self.btn_remove.Text = "Reset" 
        self.bind("<Control-Return>", self.on_remove_paste_pressed)


        # Label : Panel Output
        # ==================================
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
        

        
    def on_return_manual_pressed(self, event=None):
        coordxA = float(self.coordX1.getValue())
        coordzA = float(self.coordZ1.getValue())
        angleA = float(self.angle1.getValue())
        coordxB = float(self.coordX2.getValue())
        coordzB = float(self.coordZ2.getValue())
        angleB = float(self.angle2.getValue())

        hasil = rumus.coord(coordxA, coordzA, angleA, coordxB, coordzB, angleB)
        
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
        
    def on_return_paste_pressed(self):
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

    def on_remove_paste_pressed(self, event=None):
        self.coordX1.Value = "" 
        self.coordZ1.Value = "" 
        self.angle1.Value = "" 
        self.coordX2.Value = "" 
        self.coordZ2.Value = "" 
        self.angle2.Value = "" 
        
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

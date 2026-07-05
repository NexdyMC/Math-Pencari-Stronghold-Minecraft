import customtkinter as ctk
from element.button import Button 
from element.label  import Label
from element.input  import Input
from element.panel  import Panel

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        # self.geometry("400x200")
        self.title("this is a panel")

        self.input = Panel(self, fg_color="#555")
        self.input.pack(fill="x", expand=True)

        self.hasil = Panel(self, fg_color="#444")
        self.hasil.pack(fill="x", expand=True)


        # Label(self.input, "Ender Eye 1: ", width=120).pack()
        
        # # label
        Label(self.input, "Ender Eye 1: ", width=120).RowColumn(1,0)       
        Label(self.input, "Ender Eye 2: ", width=120).RowColumn(2,0)
        
        Label(self.input, "Coord X", width=80).RowColumn(0,1)
        Label(self.input, "Coord Y", width=80).RowColumn(0,2)
        Label(self.input, "Radient", width=80).RowColumn(0,3)

        # Input 
        self.coordX1 = Input(self.input, width=80, bg_color="#333" ,fg_color="#444", corner_radius=0, border_width=1).RowColumn(1, 1).Padding(2, 2)
        self.coordY1 = Input(self.input, width=80, bg_color="#333" ,fg_color="#444", corner_radius=0, border_width=1).RowColumn(1, 2).Padding(2, 2)
        self.radius1 = Input(self.input, width=80, bg_color="#333" ,fg_color="#444", corner_radius=0, border_width=1).RowColumn(1, 3).Padding(2, 2)
        
        self.coordX2 = Input(self.input, width=80, bg_color="#333" ,fg_color="#444", corner_radius=0, border_width=1).RowColumn(2, 1).Padding(2, 2)
        self.coordY2 = Input(self.input, width=80, bg_color="#333" ,fg_color="#444", corner_radius=0, border_width=1).RowColumn(2, 2).Padding(2, 2)
        self.radius2 = Input(self.input, width=80, bg_color="#333" ,fg_color="#444", corner_radius=0, border_width=1).RowColumn(2, 3).Padding(2, 2)
        
        Label(self.hasil, "Dimension ", width=120, fg_color="#040").RowColumn(4,0)
        Label(self.hasil, "Block ", width=120, fg_color="#050").RowColumn(4,1)
        Label(self.hasil, "Chunk ", width=120, fg_color="#040").RowColumn(4,3)
        
        Label(self.hasil, "Overworld ", width=120, fg_color="#040").RowColumn(5,0)
        Label(self.hasil, "xxxx ", width=120, fg_color="#040").RowColumn(5,1)
        Label(self.hasil, "yyyy ", width=120, fg_color="#040").RowColumn(5,1).Span(0, 2)
        Label(self.hasil, "xxx ", width=120, fg_color="#040").RowColumn(5,3)
        Label(self.hasil, "yyy ", width=120, fg_color="#040").RowColumn(5,3).Span(0, 2)
        # # # Button 
        # self.btn_search = Button(self.input).RowColumn(3, 0)
        # self.bind("<Return>", self.on_return_pressed)
        # # self.btn4 = Button(self, width=150).RowColumn(3, 1)
        
        # # label output
        # Label(self.output, "Output: ", width=120, fg_color="#050").RowColumn(4,0)
        # Label(self.output, "Output: ", width=120, fg_color="#050").RowColumn(4,1)
        # Label(self.output, "Output: ", width=120, fg_color="#050").RowColumn(4,2)

    def on_return_pressed(self, event):
        print("Enter key pressed")

if __name__ == "__main__":
    app = App()
    app.mainloop()

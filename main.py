import customtkinter as ctk
from element.button import Button 
from element.label  import Label
from element.input  import Input

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x200")
        self.title("this is a panel")

        # label
        self.label = Label(self, "Ender Eye 1: ", width=120).RowColumn(1,0)       
        self.label = Label(self, "Ender Eye 2: ", width=120).RowColumn(2,0)
        
        Label(self, "Coord X", width=70).RowColumn(0,1)
        Label(self, "Coord Y", width=70).RowColumn(0,2)
        Label(self, "Radient", width=70).RowColumn(0,3)

        # Input 
        self.coordX1 = Input(self, width=70, bg_color="#0ff", corner_radius=1, border_width=1).RowColumn(1, 1)
        self.coordY1 = Input(self, width=70, bg_color="#0ff", corner_radius=1, border_width=1).RowColumn(1, 2)
        self.radius1 = Input(self, width=70, bg_color="#0ff", corner_radius=1, border_width=1).RowColumn(1, 3)
        
        self.coordX2 = Input(self, width=70, bg_color="#0ff", corner_radius=1, border_width=1).RowColumn(2, 1)
        self.coordY2 = Input(self, width=70, bg_color="#0ff", corner_radius=1, border_width=1).RowColumn(2, 2)
        self.radius2 = Input(self, width=70, bg_color="#0ff", corner_radius=1, border_width=1).RowColumn(2, 3)
        
        # # Button 
        # self.btn3 = Button(self, width=100).RowColumn(3, 0)
        # self.btn4 = Button(self, width=150).RowColumn(3, 1)

if __name__ == "__main__":
    app = App()
    app.mainloop()

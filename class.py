from tkinter import *
from PIL import ImageTk,Image

class App(Tk): 
    def __init__(self):
        super().__init__()
        self.title('img viewer')
        #self.attributes('-type', 'dialog')

        self.mainloop()

App()

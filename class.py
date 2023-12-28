from tkinter import *
from PIL import ImageTk,Image

class App(Tk): 
    def __init__(self, title, size):
        super().__init__()
        self.title(title)
        self.attributes('-type', 'dialog')
        self.geometry(f'{size[0]}x{size[1]}')
        #self.minsize(600,600)

        self.mainloop()

App('Image viewer', (600,600))

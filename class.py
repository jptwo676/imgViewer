from tkinter import *
from PIL import ImageTk,Image

list_img = []

class App(Tk): 
    def __init__(self, title, size):
        super().__init__()
        #main setup
        self.title(title) 
        self.attributes('-type', 'dialog')
        self.geometry(f'{size[0]}x{size[1]}')

        #self.minsize(f'{size[0]}x{size[1]}')
        
        #main loop
        self.mainloop()

class Photos(ImageTk.PhotoImage): #declare photos and paths 
    def __init__(self, path):
        super().__init__()
        self.path = path 

    def declare_img(self):
        pass

    def add_img(self, list_img):
        pass    

    def remove_img(self, list_img):
        pass


class Display():
    def __init__(self):
        pass
    


App('Image viewer', (600,600))

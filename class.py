from tkinter import *
from PIL import ImageTk,Image
from func import *
 


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
    list_img = [] 
    def __init__(self, parent):
        super().__init__(parent)

    def add_img(self, list_img):
        #image declaration
        img_1 = Photos(Image.open('img1.png')) 
        img_2 = Photos(Image.open('img2.png'))
        img_3 = Photos(Image.open('img3.png'))
                    
    def remove_img(self, list_img):
        pass


App('Image viewer', (600,600))

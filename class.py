from tkinter import *
from PIL import ImageTk,Image
from func import *
 

list_img = [] 

#declaração provisória
img_1 = ImageTk.PhotoImage(Image.open('img1.png')) 
img_2 = ImageTk.PhotoImage(Image.open('img2.png'))
img_3 = ImageTk.PhotoImage(Image.open('img3.png'))



class App(Tk): 
    def __init__(self, title, size, list_img):
        super().__init__()
        #main setup
        self.title(title) 
        self.attributes('-type', 'dialog')
        self.geometry(f'{size[0]}x{size[1]}')

        #self.minsize(f'{size[0]}x{size[1]}')
        

        #main loop
        self.mainloop()

class Display(ImageTk.PhotoImage): #declare photos and paths 
    pass


class Buttons(Button):
        def __init__(self)

    def button_dec():
        pass

    def button_pos():
        pass    


App('Image viewer', (600,600), list_img)

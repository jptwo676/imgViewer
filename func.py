from tkinter import *
from PIL import ImageTk, Image

i = 1

dic_img = {}
list_img = []

def add_img(path): #declara a img    
    img_[i] = ImageTk.PhotoImage(Image.open(path))
    i += 1

def remove_img(path):
    pass

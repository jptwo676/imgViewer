from tkinter import *
from PIL import ImageTk, Image

i = 1

dic_img = {}
list_img = []

def add_img(name, path): #declara a img    
    global i
    name[i] = ImageTk.PhotoImage(Image.open(path))
    i += 1

def remove_img(path):
    pass

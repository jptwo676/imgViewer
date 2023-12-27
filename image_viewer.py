from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('img viewer')
root.attributes('-type', 'dialog')

image_num = 0
count = 0

#fazer o botao << ativado quando passar do 0
#o mainloop() é seletivo

def change_pic(state):  
    '''change the pic, taking next ou last as argument'''
    global my_label          
    global image_num

    if state == 'next_pic':
        image_num += 1 
        my_label.grid_forget() #delete the current image  
        my_label = Label(image=list_img[image_num]) 
        my_label.grid(row=0, column=0, columnspan=5)
        print(image_num)

    elif state == 'last_pic':
        image_num -=1
        my_label = Label(image=list_img[image_num]) 
        my_label.grid(row=0, column=0, columnspan=5)
        print(image_num)
        print('state check')

    elif state == 'zero':
        my_label = Label(image=list_img[0]) #shows the new img
        my_label.grid(row=0, column=0, columnspan=5)
        last.config(state=DISABLED)
        print(image_num)





#put the imgs in a list
my_label = Label()
img_1 = ImageTk.PhotoImage(Image.open('img1.png'))
img_2 = ImageTk.PhotoImage(Image.open('img2.png'))
img_3 = ImageTk.PhotoImage(Image.open('img3.png'))
list_img = [img_1, img_2, img_3]

text = Label(root, text=f'{image_num}') #shows the pic number

next = Button(root, text='>>', command=lambda:change_pic('next_pic'))
last = Button(root, text='<<', command=lambda:change_pic('last_pic'))
exit_button = Button(root, text='EXIT', command=root.quit)

text.grid(row=3, column=2)
next.grid(row=4, column=3)
last.grid(row=4, column=0)
exit_button.grid(row=4,column=2)

change_pic('zero')


root.mainloop()

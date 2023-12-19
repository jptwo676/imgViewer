from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('img viewer')
root.attributes('-type', 'dialog')

image_num = 0
count = 0

#unificar os dois >> e o <<

def change_pic(state):  
    '''change the pic, taking next ou last as argument'''
    global my_label          
    global image_num

    #in case of 0 is the image in exibition
    if image_num == 0 and state == 'next_pic':  #in case the current image is the second one
        my_label.grid_forget() #delete the current image  
        my_label = Label(image=list_img[0]) #shows the new img
        my_label.grid(row=0, column=0, columnspan=5)
        last.config(state=NORMAL)
        image_num += 1 
        print(image_num)
    elif image_num == 0 and state == 'last_pic':
        last.config(state=DISABLED) #disable the button
        print('state check')
    #in case you can go foward
    elif image_num > 0 and image_num != len(list_img):
        my_label.grid_forget()   
        my_label = Label(image=list_img[image_num]) 
        my_label.grid(row=0, column=0, columnspan=5)
        image_num += 1 
        print(image_num)
    
       

def image_zero(): 
    '''shows the defalt image (index=0)'''
    global my_label          

    my_label = Label(image=list_img[0]) 
    my_label.grid(row=0, column=0, columnspan=5)
    #last.config(state=DISABLED) #need to be last command to acess the var
    print(image_num)
   
    


img_1 = ImageTk.PhotoImage(Image.open('img1.png'))
img_2 = ImageTk.PhotoImage(Image.open('img2.png'))
img_3 = ImageTk.PhotoImage(Image.open('img3.png'))
list_img = [img_1, img_2, img_3]



text = Label(root, text=f'{image_num}') #shows the pic number

#test = Button(root, text="test", command=lambda:next_pic())

next = Button(root, text='>>', command=lambda:change_pic('next_pic'))
last = Button(root, text='<<', command=lambda:change_pic('last_pic'))
exit_button = Button(root, text='EXIT', command=root.quit)
if  image_num == 0:
        
    my_label = Label(image=list_img[0]) #shows the new img
    my_label.grid(row=0, column=0, columnspan=5)
    last.config(state=DISABLED)
    image_num += 1

text.grid(row=3, column=2)
next.grid(row=4, column=3)
last.grid(row=4, column=0)
exit_button.grid(row=4,column=2)

root.mainloop()

from googletrans import Translator
from tkinter import *
from PIL import Image, ImageTk


# Tạo function cho các button
def clear():
    src_box.delete(1.0, END)
    des_box.delete(1.0, END)


def translate():
    try:
        t = Translator()
        src_input = src_box.get(1.0, END)
        a = t.translate(src_input, src='vi', dest='en')
        b = a.text
        des_box.delete(1.0, END)
        des_box.insert(END, b)
    except:
        pass


# Tạo Tk window
root = Tk()
root.title('Google Translator')
root.geometry('500x630')
root.iconbitmap(r'C:\Users\Admin\Desktop\Python_projects\Application\Google Translator\images\logo.ico')

bg = Image.open(r'C:\Users\Admin\Desktop\Python_projects\Application\Google Translator\images\background.png')
render = ImageTk.PhotoImage(bg)
img = Label(root, image=render)
img.place(x=0, y=0)

name = Label(root, text='Translator', fg='#FFFFFF', bd=0, bg='#03152D')
name.config(font=('Transformers Movie', 30))
name.pack(pady=10)

src_box = Text(root, width=28, height=8, font=('ROBOTO', 16))
src_box.pack(pady=20)

button_frame = Frame(root)
button_frame.pack()

frm_trans_button = Frame(button_frame)
frm_trans_button.pack(side=LEFT)

frm_middle = Frame(button_frame)
frm_middle.pack(side=LEFT)
blank = Label(frm_middle, text='                     ')


frm_clear_button = Frame(button_frame)
frm_clear_button.pack(side=RIGHT)


trans_button = Button(frm_trans_button, text='Translate',
                      font=('Arial', 12, 'bold'), bg='#303030', fg='#FFFFFF')
trans_button.config(command=translate)
trans_button.pack(side=LEFT, anchor='w', padx=(0, 50))

clear_button = Button(frm_clear_button, text='Clear text',
                      font=('Arial', 12, 'bold'), bg='#303030', fg='#FFFFFF')
clear_button.config(command=clear)
clear_button.pack(side=RIGHT)

des_box = Text(root, width=28, height=8, font=('ROBOTO', 16))
des_box.pack(pady=50)

root.mainloop()

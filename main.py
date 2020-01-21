from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import os

interface = Tk()

imagenPath=''
def openFile():
    imagenPath=filedialog.askopenfilename(initialdir = "Path Where the dialog should open first",title = "Select file")
    
    img = Image.open(imagenPath)
    img = img.resize((600, 300), Image.ANTIALIAS) 
    photoImage = ImageTk.PhotoImage(img)
    panel = Label(interface, image = photoImage)
    panel.grid(column=2, row=1,pady=1, columnspan=2)
    img2 = Image.open(imagenPath).resize((600, 300), Image.ANTIALIAS) 
    photoImage2 = ImageTk.PhotoImage(img2)
    panel2 = Label(interface, image = photoImage2)
    panel2.grid(column=2, row=2,pady=1, columnspan=3)
    interface.mainloop()

Label(interface, 
         text="Alfa").grid(row=3)
Label(interface, 
         text="Gama").grid(row=4)

e1 = Entry(interface)
e2 = Entry(interface)

e1.grid(row=3, column=2)
e2.grid(row=4, column=2)

Button(interface,text='Ver cambios').grid(row=5, column=2,pady=4)
Button(interface,text='Seleccionar imagen', command=openFile).grid(row=5, column=1,pady=4)
interface.mainloop()
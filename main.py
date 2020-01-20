from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import os

interface = Tk()

interface.filename =  filedialog.askopenfilename(initialdir = "Path Where the dialog should open first",title = 
"Practica 1 Open CV")

img = Image.open(interface.filename)
img = img.resize((300, 150), Image.ANTIALIAS) 
photoImage = ImageTk.PhotoImage(img)
panel = Label(interface, image = photoImage)
panel.grid(column=2, row=1,columnspan=3)
img2 = Image.open(interface.filename).resize((300, 150), Image.ANTIALIAS) 
photoImage2 = ImageTk.PhotoImage(img2)
panel2 = Label(interface, image = photoImage2)
panel2.grid(column=2, row=2)
print(img.size )
Label(interface, 
         text="Alfa").grid(row=3)
Label(interface, 
         text="Gama").grid(row=4)

e1 = Entry(interface)
e2 = Entry(interface)

e1.grid(row=3, column=2)
e2.grid(row=4, column=2)

Button(interface, 
          text='Ver cambios').grid(row=5, 
                                                       column=1,  
                                                       pady=4)
interface.mainloop()
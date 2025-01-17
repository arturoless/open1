import cv2
import sys
import numpy as np
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk

import recuperacion_fondo
import recuperacion_movimiento

pathIn = ''
interface = Tk()
entry = ttk.Entry(interface)
entry.insert(0, 0.9675)

def openFile():
    global pathIn
    imagenPath = filedialog.askopenfilename(
        title="Seleccionar archivo de video")
    pathIn = imagenPath
    if pathIn == "":
        messagebox.showwarning("¡ERROR!", "Debes seleccionar un video")

    interface.mainloop()


def estabilizado():
    global pathIn
    if pathIn == "":
        messagebox.showwarning("¡ERROR!", "Debes seleccionar un video")
    else:
        recuperacion_fondo.process_video(pathIn, float(entry.get()))


def movimiento():
    global pathIn
    if pathIn == "":
        messagebox.showwarning("¡ERROR!", "Debes seleccionar un video")
    else:
        recuperacion_movimiento.process_video(pathIn, float(entry.get()))

photo = PhotoImage(file=r"btn.png")

Button(interface, text='Seleccionar video', image=photo, compound=LEFT,
       command=openFile).grid(row=1, column=1)
Label(interface, text="Alfa").grid(row=1, column=2)
entry.grid(row=1, column=3)
Button(interface, text='Procesar video',
       command=estabilizado).grid(row=1, column=4)
Button(interface, text='Procesar video con movimiento',
       command=movimiento).grid(row=1, column=5)
interface.mainloop()

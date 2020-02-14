import cv2
import sys
import numpy as np
from tkinter import *
from tkinter import filedialog

import recuperacion_fondo
import recuperacion_movimiento

pathIn = ''
interface = Tk()


def openFile():
    global pathIn
    imagenPath = filedialog.askopenfilename(
        title="Seleccionar archivo de video")
    pathIn = imagenPath
    interface.mainloop()


def estabilizado():
    global pathIn
    recuperacion_fondo.process_video(pathIn)


def movimiento():
    global pathIn
    recuperacion_movimiento.process_video(pathIn)


Button(interface, text='Seleccionar video',
       command=openFile).grid(row=1, column=1)
Button(interface, text='Procesar video',
       command=estabilizado).grid(row=1, column=2)
Button(interface, text='Procesar video con movimiento',
       command=movimiento).grid(row=1, column=3)
interface.mainloop()

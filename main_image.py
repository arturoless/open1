import cv2
import sys
import numpy as np
from tkinter import *
from tkinter import filedialog

import repair_image
import image1
import recuperacion_movimiento

interface = Tk()


def openFile():
    global pathIn
    imagenPath = filedialog.askopenfilename(
        title="Seleccionar archivo de video")
    pathIn = imagenPath
    interface.mainloop()


Button(interface, text='Seleccionar video',
       command=openFile).grid(row=1, column=1)
Button(interface, text='Procesar video',
       command=image1.process_video()).grid(row=1, column=2)
Button(interface, text='Procesar video con movimiento',
       command=recuperacion_movimiento.process_video()).grid(row=1, column=3)
interface.mainloop()

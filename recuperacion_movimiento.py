import cv2
import sys
import numpy as np
from tkinter import *
from tkinter import filedialog

import repair_image

interface = Tk()
pathIn = 'joker.mp4'


def process_video():
    sec = 0
    frameRate = 0.2
    alpha = 0.9675
    beta = (1.0 - alpha)
    pathOut = 'video.avi'
    fps = 15
    vidcap = cv2.VideoCapture(pathIn)
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    success, image = vidcap.read()
    if success:
        height, width, layers = image.shape
        size = (width, height)
        out = cv2.VideoWriter(
            pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
        global src1
        src1 = image
        r = cv2.selectROI(src1)
        imCrop = src1[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
        cv2.imshow("Image", imCrop)
        cv2.waitKey(1)
        out.write(src1)
    else:
        print('Archivo incorrecto')
    while success:
        sec = round(sec + frameRate, 2)
        vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
        success, image = vidcap.read()
        if success:
            src2 = image
            dst = np.uint8(alpha*(src1)+beta*(repair_image.alinear(src2, imCrop, r)))
            src1 = dst
            out.write(dst)

    out.release()
    print('Listo')


def openFile():
    global pathIn
    imagenPath = filedialog.askopenfilename(
        title="Seleccionar archivo de video")
    pathIn = imagenPath
    interface.mainloop()


Button(interface, text='Seleccionar video',
       command=openFile).grid(row=1, column=1)
Button(interface, text='Procesar video',
       command=process_video).grid(row=1, column=2)
interface.mainloop()


# if __name__ == "__main__":
#     r = cv2.selectROI(src1)
#     imCrop = src1[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

#     # Display cropped image
#     cv2.imshow("Image", imCrop)
#     cv2.waitKey(1)
#     cv2.imshow('Imagen cortada', repair_image.alinear(src1, src2, imCrop, r))
#     cv2.waitKey()

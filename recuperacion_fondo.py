import cv2
import numpy as np
import time
from tkinter import messagebox

def process_video(pathIn):
    sec = 0
    frameRate = 0.2
    alpha = 0.9675
    beta = (1.0 - alpha)
    pathOut = 'video_sin_fondo.avi'
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
        out.write(src1)
    else:
        print('Archivo incorrecto')
    while success:
        print(f'sec: {sec}')
        sec = round(sec + frameRate, 2)
        vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
        success, image = vidcap.read()
        if success:
            src2 = image
            dst = np.uint8(alpha*(src1)+beta*(src2))
            src1 = dst
            out.write(dst)

    out.release()
    print('Listo')
    messagebox.showinfo("!LISTO!", "Video procesado éxitosamente")

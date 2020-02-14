import cv2
import sys
import numpy as np
from tkinter import messagebox

import repair_image as rp


def process_video(pathIn):
    sec = 0
    frameRate = 0.2
    alpha = 0.9675
    beta = (1.0 - alpha)
    pathOut = 'video_estable_sin_fondo.avi'
    fps = 5
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

        recorte = src1[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
        cv2.imshow("Image", recorte)
        cv2.waitKey(1)
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
            dst = np.uint8(alpha*(src1)+beta * (rp.alinear(src2, recorte, r)))
            src1 = dst
            out.write(dst)
    out.release()
    print('Listo')
    messagebox.showinfo("!LISTO!", "Video procesado éxitosamente")

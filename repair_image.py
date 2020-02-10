import cv2
import sys
import numpy as np


def alinear(frame, fragmento, r):
    find = False
    ssdd = 0
    mejor_x_inicial = 0
    mejor_y_inicial = 0

    for filas in range(len(frame)-len(fragmento)):
        for columnas in range(len(frame[0])-len(fragmento[0])):
            temp_sad = 0
            for filas_crop in range(len(fragmento)):
                for columnas_crop in range(len(fragmento[0])):
                    temp_sad += np.power(np.sum(np.subtract(
                        fragmento[filas_crop][columnas_crop], frame[filas+filas_crop][columnas+columnas_crop])), 2)
            ssd = temp_sad/(len(fragmento)*len(fragmento[0]))
            ssd = np.sqrt(ssd)
            if find == False and ssdd == 0:
                ssdd = ssd
            if ssd < ssdd:
                ssdd = ssd
                mejor_x_inicial = filas
                mejor_y_inicial = columnas
                if ssd == 0:
                    find = True
                    break
        if find:
            break

    movimiento_x = r[1]-mejor_x_inicial
    movimiento_y = r[0]-mejor_y_inicial

    print(movimiento_x)
    print(movimiento_y)
    translation_matrix = np.float32(
        [[1, 0, movimiento_y], [0, 1, movimiento_x]])
    num_rows, num_cols = frame.shape[:2]
    img_translation = cv2.warpAffine(
        frame, translation_matrix, (num_cols, num_rows))
    return img_translation

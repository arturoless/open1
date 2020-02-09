import cv2
import sys
import numpy as np


def alinear(imagenFuente, frame, fragmento, r):
    mejor_x_inicial = 0
    mejor_x_final = 0
    mejor_y_inicial = 0
    mejor_y_final = 0
    sad = 0

    find = False
    for filas in range(len(frame)-len(fragmento)):
        for columnas in range(len(frame[0])-len(fragmento[0])):
            for filas_crop in range(len(fragmento)):
                for columnas_crop in range(len(fragmento[0])):
                    temp_sad = np.sum(abs(np.subtract(
                        fragmento[filas_crop][columnas_crop], imagenFuente[filas+filas_crop][columnas+columnas_crop])))
            if filas == 0 and columnas == 0:
                sad = temp_sad
            if temp_sad < sad:
                sad = temp_sad
                mejor_x_inicial = filas
                mejor_x_final = filas+filas_crop+1
                mejor_y_inicial = columnas
                mejor_y_final = columnas+columnas_crop+1
                if sad == 0:
                    find = True
                    break
        print(str(filas))
        if find:
            break

    print(sad)
    print(str(mejor_x_inicial)+','+str(mejor_x_final))
    print(str(mejor_y_inicial)+','+str(mejor_y_final))
    print(r[1])
    print(r[1]+r[3])
    print(r[0])
    print(r[0]+r[2])

    movimiento_x = r[1]-mejor_x_inicial
    movimiento_y = r[0]-mejor_y_inicial

    translation_matrix = np.float32(
        [[1, 0, movimiento_x], [0, 1, movimiento_y]])
    num_rows, num_cols = frame.shape[:2]
    img_translation = cv2.warpAffine(
        imagenFuente, translation_matrix, (num_cols, num_rows))

    return img_translation
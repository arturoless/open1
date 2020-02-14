import cv2
import sys
import numpy as np


def alinear(frame, fragmento, r):
    encontrado = False
    mejor_ssd = 0
    mejor_fila = 0
    mejor_columna = 0
    n=fragmento.shape[0]*fragmento.shape[1]

    for filas in range(frame.shape[0]-fragmento.shape[0]):
        for columnas in range(frame.shape[1]-fragmento.shape[1]):
            frame_submatrix=frame[filas:(filas+fragmento.shape[0]), columnas:(columnas+fragmento.shape[1])]
            ssd = np.sum(np.subtract(fragmento,frame_submatrix)**2)/n
           
            if not encontrado and mejor_ssd == 0:
                mejor_ssd = ssd
            if ssd < mejor_ssd:
                mejor_ssd = ssd
                mejor_fila = filas
                mejor_columna = columnas
                if ssd == 0:
                    encontrado = True
                    break
        if encontrado:
            break
    movimiento_fila = r[1]-mejor_fila
    movimiento_columna = r[0]-mejor_columna

    translation_matrix = np.float32(
        [[1, 0, movimiento_columna], [0, 1, movimiento_fila]])
    num_rows, num_cols = frame.shape[:2]
    img_translation = cv2.warpAffine(
        frame, translation_matrix, (num_cols, num_rows))
    return img_translation

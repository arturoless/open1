import cv2
import sys
import numpy as np


def alinear(frame, fragmento, r):
    find = False
    mejor_ssd = 0
    mejor_x_inicial = 0
    mejor_y_inicial = 0
    n=fragmento.shape[0]*fragmento.shape[1]

    for filas in range(frame.shape[0]-fragmento.shape[0]):
        for columnas in range(frame.shape[1]-fragmento.shape[1]):
            frame_submatrix=frame[filas:(filas+fragmento.shape[0]), columnas:(columnas+fragmento.shape[1])]
            ssd = np.sum(np.subtract(fragmento,frame_submatrix)**2)/n
           
            if not find and mejor_ssd == 0:
                mejor_ssd = ssd
            if ssd < mejor_ssd:
                mejor_ssd = ssd
                mejor_x_inicial = filas
                mejor_y_inicial = columnas
                if ssd == 0:
                    find = True
                    break
        if find:
            break
    print(f'mejor x:{mejor_x_inicial},mejor y:{mejor_y_inicial},ssd:{ssd}')
    movimiento_x = r[1]-mejor_x_inicial
    movimiento_y = r[0]-mejor_y_inicial

    translation_matrix = np.float32(
        [[1, 0, movimiento_y], [0, 1, movimiento_x]])
    num_rows, num_cols = frame.shape[:2]
    img_translation = cv2.warpAffine(
        frame, translation_matrix, (num_cols, num_rows))
    return img_translation

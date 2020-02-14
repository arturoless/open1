import cv2
import numpy as np
from multiprocessing import Process, Manager

def cuarto1(frame, fragmento, size_cuadrante,cuadrante_filas,cuadrante_columnas,find,ssdd,mejor_x_inicial,mejor_y_inicial):
    if cuadrante_filas == size_cuadrante-1:
        margen_filas=int(len(frame)/size_cuadrante)-len(fragmento)
    else:
        margen_filas=int(len(frame)/size_cuadrante)
    if cuadrante_columnas == size_cuadrante-1:
        margen_columnas=int(len(frame[0])/size_cuadrante)-len(fragmento[0])
    else:
        margen_columnas=int(len(frame[0])/size_cuadrante)


    inicio_filas=(cuadrante_filas*int(len(frame)/size_cuadrante))
    inicio_columnas=(cuadrante_columnas*int(len(frame[0])/size_cuadrante))
    
    # rango= np.arange(margen_filas*margen_columnas).reshape(margen_columnas,margen_filas)

    # it = np.nditer(rango,flags=['multi_index'])

    # rango_frag= np.arange(fragmento.shape[1]*fragmento.shape[0]).reshape(fragmento.shape[0],fragmento.shape[1])

    # it_frag = np.nditer(rango_frag,flags=['multi_index'])
    for filas in range(frame.shape[0]-fragmento.shape[0]):
        for columnas in range(frame.shape[1]-fragmento.shape[1]):
            temp_sad=0
            for filas_crop in range(fragmento.shape[0]):
                for columnas_crop in range(fragmento.shape[1]):
                    temp_sad+=np.sum((fragmento[filas_crop][columnas_crop]-frame[inicio_filas+filas+filas_crop][inicio_columnas+columnas+columnas_crop])**2)
            print(f'fila:{filas},columna:{columnas}')
            ssd=temp_sad/(len(fragmento)*len(fragmento[0]))
            if not find.value and ssdd.value==0:
                ssdd.value = ssd
            if (ssd < ssdd.value) and not find.value:
                print(ssd)
                if ssd == 0:
                    print('0')
                    ssdd.value = ssd
                    mejor_x_inicial.value = inicio_filas+filas
                    mejor_y_inicial.value = inicio_columnas+columnas
                    find.value=True
                    break
                ssdd.value = ssd
                mejor_x_inicial.value = inicio_filas+filas
                mejor_y_inicial.value = inicio_columnas+columnas
         
            if find.value:
                break
        if find.value:
                break

def alinear(frame, fragmento, r):
    print('aq')
    ssdd=0
    size=2 
    manager = Manager()
    ssdd = manager.Value('ssd', 0)
    find = manager.Value('find', False)
    mejor_x_inicial = manager.Value('mejor_x_inicial', 0)
    mejor_y_inicial = manager.Value('mejor_y_inicial', 0)
    procesos=[]
    for cuadrante_filas in range(size):
        for cuadrante_columnas in range(size):
            p = Process(target=cuarto1, args=(frame, fragmento, size,cuadrante_filas, cuadrante_columnas,find,ssdd,mejor_x_inicial,mejor_y_inicial,), daemon=True)
            print('ya')
            p.start()
            
            procesos.append(p)
    for p in procesos:
        print('ok')
        p.join()
        
    print(f'{ssdd.value},{mejor_x_inicial.value},{mejor_y_inicial.value}')

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

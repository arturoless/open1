import cv2
import sys
import numpy as np
import threading 
from multiprocessing import Pool, Process, Manager

# global find
# find=False
# global mejor_x_inicial
# mejor_x_inicial = 0
# global mejor_y_inicial
# mejor_y_inicial = 0
# global resultado1
# resultado1=[]
# global resultado2
# resultado2=[]
# global resultado3
# resultado3=[]
# global resultado4
# resultado4=[]


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
    
    rango= np.arange(margen_filas*margen_columnas).reshape(margen_columnas,margen_filas)

    it = np.nditer(rango,flags=['multi_index'])

    rango_frag= np.arange(fragmento.shape[1]*fragmento.shape[0]).reshape(fragmento.shape[0],fragmento.shape[1])

    it_frag = np.nditer(rango_frag,flags=['multi_index'])
    # for x in it:
    #     # print(x)
    #     # print(f'{it.multi_index}')
    #     # for x_f in it_frag:
    #     #     print(f'{it.multi_index},{it_frag.multi_index}')
    #     temp_sad=0
    #     for filas_crop in range(len(fragmento)):
    #         for columnas_crop in range(len(fragmento[0])):
    #             temp_sad+=np.sum((fragmento[filas_crop][columnas_crop]-frame[inicio_filas+it.multi_index[0]+filas_crop][inicio_columnas+it.multi_index[1]+columnas_crop])**2)
    #             print(f'{it.multi_index},{filas_crop},{columnas_crop}')

    for filas in range(margen_filas):
        for columnas in range(margen_columnas):
            temp_sad=0
            for filas_crop in range(len(fragmento)):
                for columnas_crop in range(len(fragmento[0])):
                    temp_sad+=np.sum((fragmento[filas_crop][columnas_crop]-frame[inicio_filas+filas+filas_crop][inicio_columnas+columnas+columnas_crop])**2)
                   
                    # if cuadrante_filas == size_cuadrante-1 and cuadrante_columnas == size_cuadrante-1:
                    #     temp_sad+=np.power(np.sum(np.subtract(fragmento[filas_crop][columnas_crop], frame[inicio_filas+filas_crop][inicio_columnas+columnas_crop])),2)
                    # elif cuadrante_filas == size_cuadrante-1:
                    #     temp_sad+=np.power(np.sum(np.subtract(fragmento[filas_crop][columnas_crop], frame[inicio_filas+filas_crop][inicio_columnas+columnas+columnas_crop])),2)
                    # elif cuadrante_columnas == size_cuadrante-1:
                    #     temp_sad+=np.power(np.sum(np.subtract(fragmento[filas_crop][columnas_crop], frame[inicio_filas+filas+filas_crop][inicio_columnas+filas_crop])),2)
                    # else:
                    #     temp_sad+=np.power(np.sum(np.subtract(fragmento[filas_crop][columnas_crop], frame[inicio_filas+filas+filas_crop][inicio_columnas+columnas+columnas_crop])),2)
    #         # print(f'{filas},{columnas}')
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
            p.start()
            procesos.append(p)
    for p in procesos:
        p.join()
    print(f'{ssdd.value},{mejor_x_inicial.value},{mejor_y_inicial.value}')
if __name__ == "__main__":
    pathIn = 'my.mp4'
    sec = 0
    frameRate = 1
    alpha = 0.9675
    beta = (1.0 - alpha)
    pathOut = 'video.avi'
    img = cv2.imread('open.png')
    fps = 15
    vidcap = cv2.VideoCapture(pathIn)
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    success, image = vidcap.read()
    if success:
        height, width, layers = image.shape
        size = (width, height)
        
        global src1
        src1 = image
        
        pxstep=int(src1.shape[1]/2)
        pystep=int(src1.shape[0]/2)
        x = pxstep
        y = pystep
        grid=image
        #Draw all x lines
        while x <= grid.shape[1]:
            cv2.line(grid, (x, 0), (x, grid.shape[0]), color=(255, 0, 255), thickness=1)
            x += pxstep

        while y <= grid.shape[0]:
            cv2.line(grid, (0, y), (grid.shape[1], y), color=(255, 0, 255),thickness=1)
            y += pystep
        
        r = cv2.selectROI(grid)
        imCrop = src1[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
        
        cv2.imshow("Image", imCrop)
        cv2.waitKey(1)
    sec=3
    # sec = round(sec + frameRate, 2)
    vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
    success, image = vidcap.read()
    if success:
        src2 = image

    alinear(src2,imCrop,r)
    print(r)
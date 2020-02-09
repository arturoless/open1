import cv2
import sys
import numpy as np
import threading 

global find
find=False
global resultado1
resultado1=[]
global resultado2
resultado2=[]
global resultado3
resultado3=[]
global resultado4
resultado4=[]

def cuarto1(frame, fragmento, r):
    global find
    find=False
    mejor_x_inicial = 0
    mejor_x_final = 0
    mejor_y_inicial = 0
    mejor_y_final = 0
    sad = np.sum(abs(np.subtract(
                        fragmento[0][0], frame[0][0])))

    for filas in range(int(len(frame)/2)-len(fragmento)):
        for columnas in range(int(len(frame[0])/2)-len(fragmento[0])):
            for filas_crop in range(len(fragmento)):
                for columnas_crop in range(len(fragmento[0])):
                    temp_sad = np.sum(abs(np.subtract(
                        fragmento[filas_crop][columnas_crop], frame[filas+filas_crop][columnas+columnas_crop])))
            if temp_sad < sad:
                sad = temp_sad
                mejor_x_inicial = filas
                mejor_x_final = filas+filas_crop+1
                mejor_y_inicial = columnas
                mejor_y_final = columnas+columnas_crop+1
                if sad == 0:
                    find = True
                    break
        if find:
            break
    resultado1.append(sad)
    resultado1.append(mejor_x_inicial)
    resultado1.append(mejor_y_inicial)
    print(f'c1:{resultado1}')    

def cuarto2(frame, fragmento, r):
    global find
    find=False
    mejor_x_inicial = 0
    mejor_x_final = 0
    mejor_y_inicial = 0
    mejor_y_final = 0
    sad = np.sum(abs(np.subtract(
                        fragmento[0][0], frame[0][int(len(frame[0])/2)])))

    for filas in range(int(len(frame)/2)-len(fragmento)):
        for columnas in range(int(len(frame[0])/2)-len(fragmento[0])):
            for filas_crop in range(len(fragmento)):
                for columnas_crop in range(len(fragmento[0])):
                    temp_sad = np.sum(abs(np.subtract(
                        fragmento[filas_crop][columnas_crop], frame[filas+filas_crop][int(len(frame[0])/2)+columnas+columnas_crop])))
            if temp_sad < sad:
                sad = temp_sad
                mejor_x_inicial = filas
                mejor_x_final = filas+filas_crop+1
                mejor_y_inicial = columnas + int(len(frame[0])/2)
                mejor_y_final = columnas+columnas_crop+1
                if sad == 0:
                    find = True
                    break
        if find:
            break
    resultado2.append(sad)
    resultado2.append(mejor_x_inicial)
    resultado2.append(mejor_y_inicial)
    print(f'c2:{resultado2}')

def cuarto3(frame, fragmento, r):
    global find
    find=False
    mejor_x_inicial = 0
    mejor_x_final = 0
    mejor_y_inicial = 0
    mejor_y_final = 0
    sad = np.sum(abs(np.subtract(
                        fragmento[0][0], frame[int(len(frame)/2)][0])))

    for filas in range(int(len(frame)/2)-len(fragmento)):
        for columnas in range(int(len(frame[0])/2)-len(fragmento[0])):
            for filas_crop in range(len(fragmento)):
                for columnas_crop in range(len(fragmento[0])):
                    temp_sad = np.sum(abs(np.subtract(
                        fragmento[filas_crop][columnas_crop], frame[int(len(frame)/2)+filas+filas_crop][columnas+columnas_crop])))
            if temp_sad < sad:
                sad = temp_sad
                mejor_x_inicial = filas + int(len(frame)/2)
                mejor_x_final = filas+filas_crop+1
                mejor_y_inicial = columnas
                mejor_y_final = columnas+columnas_crop+1
                if sad == 0:
                    find = True
                    break
        if find:
            break
    resultado3.append(sad)
    resultado3.append(mejor_x_inicial)
    resultado3.append(mejor_y_inicial)
    print(f'c3:{resultado3}')


def cuarto4(frame, fragmento, r):
    global find
    find=False
    mejor_x_inicial = 0
    mejor_x_final = 0
    mejor_y_inicial = 0
    mejor_y_final = 0
    sad = np.sum(abs(np.subtract(
                        fragmento[0][0], frame[int(len(frame)/2)][int(len(frame[0])/2)])))

    for filas in range(int(len(frame)/2)-len(fragmento)):
        for columnas in range(int(len(frame[0])/2)-len(fragmento[0])):
            for filas_crop in range(len(fragmento)):
                for columnas_crop in range(len(fragmento[0])):
                    temp_sad = np.sum(abs(np.subtract(fragmento[filas_crop][columnas_crop], frame[int(len(frame)/2)+filas+filas_crop][int(len(frame[0])/2)+columnas+columnas_crop])))
            if temp_sad < sad:
                sad = temp_sad
                mejor_x_inicial = filas + int(len(frame)/2)
                mejor_x_final = filas+filas_crop+1
                mejor_y_inicial = columnas + int(len(frame[0])/2)
                mejor_y_final = columnas+columnas_crop+1
                if sad == 0:
                    find = True
                    break
        if find:
            break
    resultado4.append(sad)
    resultado4.append(mejor_x_inicial)
    resultado4.append(mejor_y_inicial)
    print(f'c4:{resultado4}')
    

def alinear(frame, fragmento, r):
    t1 = threading.Thread(target=cuarto1, args=(frame, fragmento, r,),name='t1') 
    t2 = threading.Thread(target=cuarto2, args=(frame, fragmento, r,), name='t2')
    t3 = threading.Thread(target=cuarto3, args=(frame, fragmento, r,),name='t3') 
    t4 = threading.Thread(target=cuarto4, args=(frame, fragmento, r,),name='t4')
    t1.start() 
    t2.start() 
    t3.start() 
    t4.start() 
    t1.join() 
    t2.join() 
    t3.join() 
    t4.join() 

    # print(resultado1)
    # print(resultado2)
    # print(resultado3)
    


    # print(f'sad:{sad}')

    # movimiento_x = r[1]-mejor_x_inicial
    # movimiento_y = r[0]-mejor_y_inicial

    # translation_matrix = np.float32(
    #     [[1, 0, movimiento_y], [0, 1, movimiento_x]])
    # num_rows, num_cols = frame.shape[:2]
    # img_translation = cv2.warpAffine(
    #     frame, translation_matrix, (num_cols, num_rows))

    # return img_translation

pathIn = 'piano144.mp4'
sec = 0
frameRate = 1
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
    global src1
    src1 = image
    r = cv2.selectROI(src1)
    imCrop = src1[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    cv2.imshow("Image", imCrop)
    cv2.waitKey(1)
sec=0
# sec = round(sec + frameRate, 2)
vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
success, image = vidcap.read()
if success:
    src2 = image
print(r)
alinear(src1,imCrop,r)
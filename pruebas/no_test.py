import cv2
import sys
import numpy as np
import threading 
import repair_last as rp

global find
find=False
global mejor_x_inicial
mejor_x_inicial = 0
global mejor_y_inicial
mejor_y_inicial = 0
# global resultado1
# resultado1=[]
# global resultado2
# resultado2=[]
# global resultado3
# resultado3=[]
# global resultado4
# resultado4=[]




def alinear(frame, fragmento, r):
    find=False
    
    ssdd=0
    mejor_x_inicial = 0
    mejor_y_inicial = 0
    
    

    for filas in range(len(frame)-len(fragmento)):
        for columnas in range(len(frame[0])-len(fragmento[0])):
            temp_sad=0
            for filas_crop in range(len(fragmento)):
                for columnas_crop in range(len(fragmento[0])):
                        temp_sad+=np.power(np.sum(np.subtract(fragmento[filas_crop][columnas_crop], frame[filas+filas_crop][columnas+columnas_crop])),2)
            ssd=temp_sad/(len(fragmento)*len(fragmento[0]))
            ssd=np.sqrt(ssd)
            if find==False and ssdd==0:
                ssdd=ssd
            if ssd < ssdd:
                ssdd=ssd
                mejor_x_inicial = filas
                mejor_y_inicial = columnas
                if ssd == 0:
                    find=True
                    break
        if find:
            break
    print(f'[0]:[0],{mejor_x_inicial},{mejor_y_inicial}')

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
img = cv2.imread('open.png')
if success:
    height, width, layers = image.shape
    size = (width, height)
    global src1
    src1 = image
    r = cv2.selectROI(src1)
    imCrop = src1[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
    cv2.imshow("Image", imCrop)
    cv2.waitKey(1)
sec=33
# sec = round(sec + frameRate, 2)
vidcap.set(cv2.CAP_PROP_POS_MSEC, 1*1000)
success, image = vidcap.read()
if success:
    src2 = image
print(r)


print(f'filas:{src1.shape[0]},columnas:{src1.shape[1]}')
# r (xinicial, yinicial, xfinal , yfinalc)
# r (columnas, filas, xfinal , yfinalc)
print(r)
print(imCrop.shape[1])
print(imCrop.shape[0])

print(f'rangodecolumnas:{imCrop.shape[1]*5}')
margenenfilas=imCrop.shape[0]*4
margenencolumnas=imCrop.shape[0]*4

print(np.sum((imCrop[1][1]-src1[1][1])**2))
print(np.power(np.sum(np.subtract(imCrop[1][1], src1[1][1])), 2))

print(f'rangodefilas:{r[0]-margenenfilas},{(r[0]+r[2])+margenenfilas}')
print(f'rangodecolumnas:{r[1]-margenencolumnas},{(r[1]+r[3])+margenencolumnas}')

cv2.imshow("alineada",rp.alinear(src2,imCrop,r))
cv2.waitKey(0)

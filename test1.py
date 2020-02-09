import cv2
import sys
import numpy as np
pathIn = 'piano144.mp4'
sec = 0
frameRate = 0.2
vidcap = cv2.VideoCapture(pathIn)
vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
success, image = vidcap.read()
src1 = image


sec = round(sec + frameRate, 2)
vidcap.set(cv2.CAP_PROP_POS_MSEC, sec*1000)
success, image = vidcap.read()
src2 = image

# Select ROI
r = cv2.selectROI(src1)

# Crop image
print(r[1])
print(r[1]+r[3])
print(r[0])
print(r[0]+r[2])
imCrop = src1[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]

# Display cropped image
cv2.imshow("Image", imCrop)
cv2.waitKey(1)

mejor_x_inicial = 0
mejor_x_final = 0
mejor_y_inicial = 0
mejor_y_final = 0
sad = 0


find = False
for filas in range(len(src2)-len(imCrop)):
    for columnas in range(len(src2[0])-len(imCrop[0])):
        for filas_crop in range(len(imCrop)):
            for columnas_crop in range(len(imCrop[0])):
                temp_sad = np.sum(abs(np.subtract(
                    imCrop[filas_crop][columnas_crop], src1[filas+filas_crop][columnas+columnas_crop])))
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

translation_matrix = np.float32([[1, 0, movimiento_x], [0, 1, movimiento_y]])
num_rows, num_cols = src2.shape[:2]
img_translation = cv2.warpAffine(src1, translation_matrix, (num_cols, num_rows))
cv2.imshow('WarpAffine', img_translation)
cv2.waitKey()
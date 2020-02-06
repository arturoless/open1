from __future__ import print_function
from tkinter import *
import argparse
import numpy as np
import cv2 as cv
from builtins import input
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image
import os


interface = Tk()
imagenPath = ''
panel2 = None

def openFile():
    global imagenPath
    global panel2
    imagenPath = filedialog.askopenfilename(
        initialdir="Users\Arturo Lessieur\Pictures", title="Seleccionar archivo")
    img = Image.open(imagenPath)
    img = img.resize((600, 300), Image.ANTIALIAS)
    photoImage = ImageTk.PhotoImage(img)
    panel = Label(interface, image=photoImage)
    panel.grid(column=2, row=1, pady=2, columnspan=2)

    interface.mainloop()


def brightness():
    parser = argparse.ArgumentParser(
        description='Code for Changing the contrast and brightness of an image! tutorial.')
    parser.add_argument(
        '--input', help='Path to input image.', default=imagenPath)
    args = parser.parse_args()

    image = cv.imread(cv.samples.findFile(args.input))
    if image is None:
        print('Could not open or find the image: ', args.input)
        exit(0)
    new_image = np.zeros(image.shape, image.dtype)
    alpha = 1.0  # Simple contrast control
    beta = 0    # Simple brightness control

    alpha = int(e1.get())
    beta = float(e2.get())
    # Initialize values
    print(' Basic Linear Transforms ')
    print('-------------------------')
    try:
        alpha = float(alpha)
        beta = int(beta)
    except ValueError:
        print('Error, not a number')
    # Do the operation new_image(i,j) = alpha*image(i,j) + beta
    # Instead of these 'for' loops we could have used simply:
    # new_image = cv.convertScaleAbs(image, alpha=alpha, beta=beta)
    # but we wanted to show you how to access the pixels :)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                new_image[y, x, c] = np.clip(
                    alpha*image[y, x, c] + beta, 0, 255)
    #cv.imshow('Original Image', image)
    #cv.imshow('New Image', new_image)
    cv.imwrite("new_image.jpg", new_image)
    img = Image.open("new_image.jpg")
    img = img.resize((600, 300), Image.ANTIALIAS)
    photoImage = ImageTk.PhotoImage(img)
    panel2 = Label(interface, image=photoImage)
    panel2.grid(column=2, row=2, pady=2, columnspan=2)
    interface.mainloop()
    os.remove("new_image.jpg")
    # Wait until user press some key
    cv.waitKey()


Label(interface,
      text="Alfa [1.0-3.0]").grid(row=3)
Label(interface,
      text="Gama [0-100]").grid(row=4)

e1 = Entry(interface)
e2 = Entry(interface)

e1.grid(row=3, column=2)
e2.grid(row=4, column=2)

Button(interface, text='Ver cambios', command=brightness).grid(
    row=5, column=2, pady=4)
Button(interface, text='Seleccionar imagen',
       command=openFile).grid(row=5, column=1, pady=4)
interface.mainloop()

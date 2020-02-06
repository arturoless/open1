import cv2
import numpy as np
vidcap = cv2.VideoCapture('1.mp4')
def getFrame(sec,frames_video):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        height, width, layers = image.shape
        global size
        size = (width,height)
        frames_video.append(image)
       
        #cv2.imwrite("src/"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
frames_video=[]
sec = 0
frameRate = 0.5 #//it will capture image in each 0.5 second
count=0
success = getFrame(sec,frames_video)

while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec,frames_video)

alpha = 0.93
pathOut = 'video.avi'
fps = 0.75
out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)

src1 = cv2.imread(cv2.samples.findFile('src/0.jpg'))
out.write(src1)
for _ in range(count-1):
    src2 = frames_video[_+1]
    # [load]
    if src1 is None:
        print("Error loading src1")
        exit(-1)
    elif src2 is None:
        print("Error loading src2")
        exit(-1)
    # [blend_images]
    beta = (1.0 - alpha)
    dst = np.uint8(alpha*(src1)+beta*(src2))
    # [blend_images]
    src1=dst
    # [display]
    out.write(dst)
    # cv2.imshow('dst', dst)
    # cv2.waitKey(0)
    # # [display]
    # cv2.destroyAllWindows()
out.release()
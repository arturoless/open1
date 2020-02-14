import numpy as np  
m1=[[[4,5,3],[4,5,3],[4,5,3]],[[4,5,3],[4,5,3],[4,5,3]]]
m2=[[[2,2,2],[2,2,2],[2,2,2]],[[2,2,2],[2,2,2],[2,2,2]]]
imCrop = src1[int(r[1]):int(r[1]+r[3]), int(r[0]):int(r[0]+r[2])]
print(np.subtract(m1,m2))
res=np.subtract(m1,m2)**2
print(res)
print(np.sum(np.subtract(m1,m2)**2))
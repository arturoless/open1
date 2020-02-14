import numpy as np
# a = np.arange(3)
# print(a)
b = np.arange(6,12).reshape(2,3)
it = np.nditer(b, flags=['multi_index'])
for x in it:
    print(f'{x}, {it.multi_index[1]}')
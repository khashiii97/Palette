from collections import defaultdict
from matplotlib import pyplot as plt

import  numpy as np
#super-matrix 
maxs = np.load("maxs.npy",allow_pickle=True)
label_set = np.load("label_to_setnum_1000_5_1.npy",allow_pickle=True)
label_set = label_set.tolist()


print(maxs.shape)

print(label_set)

for key,value in label_set.items():
    print(key)
    print(value)
    break
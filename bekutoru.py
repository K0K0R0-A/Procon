from PIL import Image
import numpy as np
from matplotlib import pylab as plt
import sys

# img_path = "C:\Users\Kokor\Documents\procon\image\chunk_116.png"
# img_path2 = "C:\Users\Kokor\Documents\procon\image\chunk_117.png"

img = np.array(Image.open('chunk_116.png'))
img2 = np.array(Image.open('chunk_117.png'))

print("The first image shape is ",img.shape)
print("The second image shape is ",img2.shape)

for i in range(60):
    img_v = img[i][30]/255
    img2_v = img2[i][0]/255

    # percent = np.dot(img_v,img2_v)/(np.linalg.norm(img_v)*np.linalg.norm(img2_v))
    percent = (img_v[0]*img2_v[0])+(img_v[1]*img2_v[1])+(img_v[2]*img2_v[2])
    print("The percent in[ ", i ," ]rows is : ",percent)

# for j in range(60):
#     print(img[j][63]," : ",img2[j][0])
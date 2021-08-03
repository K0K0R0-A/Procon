from PIL import Image
import numpy as np
from matplotlib import pylab as plt
import sys
import cv2

img_path = "/Users/kokoro/Documents/procon_displace/img/chunk_116.png"
img_path2 = "/Users/kokoro/Documents/procon_displace/img/chunk_117.png"


img = np.array(Image.open(img_path))
img2 = np.array(Image.open(img_path2))

# print("The first image shape is ",img.shape)
# print("The second image shape is ",img2.shape)

true_count = 0
false_count =0

for i in range(15):
    # img_t = cv2.imread("chunk_"+str(i)+".png",cv2.IMREAD_GRAYSCALE)
    img_c = np.array(Image.open("/Users/kokoro/Documents/procon_displace/img/output_003/chunk_"+str(i)+".png"))
for i in range(60):
    img_v = img[i][30]/255
    img2_v = img2[i][0]/255

    # percent = (img_v[0]*img2_v[0])+(img_v[1]*img2_v[1])+(img_v[2]*img2_v[2])
    percent = np.dot(img_v,img2_v) / ((np.linalg.norm(img_v)) * np.linalg.norm(img2_v))

    print(img_v," : ",img2_v)
    print("The percent in[ ", i ," ]rows is : ",percent)

    if percent>=0.96:
        true_count = true_count+1
    else :
        false_count = false_count+1

if true_count > false_count:
    print(true_count)
    print("side by side")
else :
    print(false_count)
    print("Not side by side")
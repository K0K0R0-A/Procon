from PIL import Image
import numpy as np
from matplotlib import pylab as plt
import sys
import cv2

img_slice = 4
img_num = 15
def main():
    loader()
    make_list()
    make_one_list()
    arrange()
def rotate_90(img):
    return img.rotate(90)

def rotate_180(img):
    return img.rotate(180)

def rotate_270(img):
    return img.rotate(270)

def normarize(n):
    return n / 255
#load image and change to vector
def loader():
    img_list = [f"/Users/kokoro/Documents/procon_displace/img/output_kiritanpo/chunk_{i}.png" for i in range(img_num)]
    pre_color_vector = list(map(Image.open,img_list))
    color_vector = list(map(np.array,pre_color_vector))
    norm_color_vector = list(map(normarize,color_vector))
    pre_color_vector_90 = list(map(rotate_90,pre_color_vector))
    color_vector_90 = list(map(np.array,pre_color_vector_90))
    norm_color_vector_90 = list(map(normarize,color_vector_90))
    pre_color_vector_180 = list(map(rotate_180,pre_color_vector))
    color_vector_180 = list(map(np.array,pre_color_vector_180))
    norm_color_vector_180 = list(map(normarize,color_vector_180))
    pre_color_vector_270 = list(map(rotate_270,pre_color_vector))
    color_vector_270 = list(map(np.array,pre_color_vector_270))
    norm_color_vector_270 = list(map(normarize,color_vector_270))
    return norm_color_vector,norm_color_vector_90,norm_color_vector_180,norm_color_vector_270
norm_color_vector,norm_color_vector_90,norm_color_vector_180,norm_color_vector_270 = loader()

origin_list = []
def make_one_list():
    for i in range (len(norm_color_vector)):
        pre_origin_list = []
        pre_origin_list.append(norm_color_vector[i])
        pre_origin_list.append(norm_color_vector_90[i])
        pre_origin_list.append(norm_color_vector_180[i])
        pre_origin_list.append(norm_color_vector_270[i])
        origin_list.append(pre_origin_list)

img_width = norm_color_vector[1].shape[1]
img_height = norm_color_vector[1].shape[0]
answer_list = []
line_dictionary = {0:[0,1,2,3]}
angle_list = []
line_key = [0]
def make_list():
    for i in range((img_slice)*(img_slice)):
        a = []
        answer_list.append(a)

def find_num(vector1,number,number2,height,width,vector2,number3,number4,height2,width2):
    origin_vector = vector1[number][number2][height][width]
    compare_vector = vector2[number3][number4][height2][width2]
    percent = np.dot(origin_vector,compare_vector) / (np.linalg.norm(origin_vector) * np.linalg.norm(compare_vector))
    return percent

def get_true_count(percent):
    true_count = 0
    if percent >= 0.994:
        true_count = true_count +1
    return true_count
def arrange():
    num = 0
    num2 = 0
    num_c = 0
    num_c2 = 0
    pixel_length = origin_list[0][0].shape[0]
    length = pixel_length -1
    answer_list[0] = 0
    max_index = [[0]]
    for g in range(1):
        true_list = []
        angle_samp = [0,1,2,3]
        samp_list = []
        line_num = 0
        for f in range(len(line_dictionary)):
            line_len = len(line_dictionary[line_key[f]])
            line_num = line_num + line_len
        print(line_num)
        for h in range ():
            for i in range (img_num):
                true_count_0 = 0
                true_count_90 = 0
                true_count_180 = 0
                true_count_270 = 0
                pre_true_list = []
                # compare
                for j in range(pixel_length-1):
                    if h ==1:
                        num=j
                        num2=length
                        num_c=j
                        num_c2=0
                    elif h ==2:
                        num=0
                        num2=j
                        num_c=length
                        num_c2=j
                    elif h ==3:
                        num=j
                        num2=0
                        num_c=j
                        num_c2=length
                    elif h ==4:
                        num=length
                        num2=j
                        num_c=0
                        num_c2=j
                    x = find_num(origin_list,g,0,num,num2,origin_list,i,0,num_c,num_c2)
                    x_90 = find_num(origin_list,g,0,num,num2,origin_list,i,1,num,num_c2)
                    x_180 = find_num(origin_list,g,0,num,num2,origin_list,i,2,num_c,num_c2)
                    x_270 = find_num(origin_list,g,0,num,num2,origin_list,i,3,num_c,num_c2)
                    if x >= 0.994:
                        true_count_0 = true_count_0 +1
                    if x_90 >= 0.994:
                        true_count_90 = true_count_90 +1 
                    if x_180 >= 0.994:
                        true_count_180 = true_count_180 +1 
                    if x_270 >= 0.994:
                        true_count_270 = true_count_270 +1 
                pre_true_list.append(true_count_0)
                pre_true_list.append(true_count_90)
                pre_true_list.append(true_count_180)
                pre_true_list.append(true_count_270)
                true_list.append(pre_true_list)
        #find maximum number image
        #まだmax_indexに追加していない
        check = answer_list.index(max_index[0][0])
        print(max_index)
        print(check)
        max_num = max(list(map(lambda y: max(y),true_list)))
        np_true = np.array(true_list)
        pre_max_index = np.argwhere(np_true == max_num)
        count = 0
        #arenge the number 
        while True:
            max_index = pre_max_index
            if max_index[0][0] >= img_num:
                max_index[0][0] = max_index[0][0] - img_num
                count = count + 1
            else:
                break
        angle_list.append(max_index[0])
        angle_index = angle_samp.index(max_index[0][1])
        angle_samp.pop(angle_index)
        samp_list.append(angle_samp[0])
        samp_list.append(angle_samp[1])
        samp_list.append(angle_samp[2])
        line_dictionary[max_index[0][0]] = samp_list
        line_key.append(max_index[0][0])
        #decide the place to add
        #画像が右端だった時に指定された場所が右側だった場合の対処
        # if count == 0:
        #画像が最上列だった時に指定された場所が上な事に加え、最下段にも要素が入っている時の対処
        # if count == 1 and check <= 3:
        #     for i in range(4):
        #         del answer_list[(len(answer_list))-1]
        #         answer_list.insert(0,[])
        #     answer_list[check+4] = max_index[0][0]
        #画像が左端だった時に指定された場所が左側だった場合の対処
        # if count ==2 :
        #画像が最下段だった時に指定された場所が下な事に加え、最上段にも要素が入っている時の対処
        # if count ==3 :
        # print(max_index)
        # print(count)
        # print(answer_list)
main()

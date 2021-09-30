from PIL import Image
import numpy as np
from matplotlib import pylab as plt
import sys
import cv2

img_angle_list = ["0","90","180","270"]
img_num = 15
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

#make empty list
# judgement_list = []
# def make_list():
#     for i in range(img_num):
#         empty_list = []
#         judgement_list.append(empty_list)
# print(judgement_list[])
#rearrange the imag
final_dictionary = {}
img_width = norm_color_vector[1].shape[1]
img_height = norm_color_vector[1].shape[0]
def arrange():
    maximum_width = 16
    maximum_height = 16
    final_dictionary[1] = 0
    #find highest similar percent in each edge
    for i in range (1):
        for j in range (img_num):
            true_count = 0
            true_count_90 = 0
            true_count_180 = 0
            true_count_270 = 0
            true_list = []
            true_list_90 = []
            true_list_180 = []
            true_list_270 = []
            final_true_list = []
            final_index_list = []
            direction_list = []
            right_list = []
            right_list_90 = []
            right_list_180 = []
            right_list_270 = []
            down_list = []
            down_list_90 = []
            down_list_180 = []
            down_list_270 = []
            left_list = []
            left_list_90 = []
            left_list_180 = []
            left_list_270 = []
            up_list = []
            up_list_90 = []
            up_list_180 = []
            up_list_270 = []
            #right edge
            for k in range (img_height-1):
                direction = 1
                #load
                orgin_img = norm_color_vector[i][k][img_width-1]
                compare_img = norm_color_vector[j][k][0]
                compare_img_90 = norm_color_vector_90[j][k][0]
                compare_img_180 = norm_color_vector_180[j][k][0]
                compare_img_270 = norm_color_vector_270[j][k][0]
                #compare
                percent = np.dot(orgin_img,compare_img) / (np.linalg.norm(orgin_img) * np.linalg.norm(compare_img))
                percent_90 = np.dot(orgin_img,compare_img_90) / (np.linalg.norm(orgin_img) * np.linalg.norm(compare_img_90))
                percent_180 = np.dot(orgin_img,compare_img_180) / (np.linalg.norm(orgin_img) * np.linalg.norm(compare_img_180))
                percent_270 = np.dot(orgin_img,compare_img_270) / (np.linalg.norm(orgin_img) * np.linalg.norm(compare_img_270))
                #Threshold(閾値)
                if percent >= 0.994:
                    true_count = true_count + 1
                if percent_90 >= 0.994:
                    true_count_90 = true_count_90 + 1
                if percent_180 >= 0.994:
                    true_count_180 = true_count_180 + 1
                if percent_270 >= 0.994:
                    true_count_270 = true_count_270 + 1
            direction_list.append(direction)
            true_list.append(true_count)   
            true_list_90.append(true_count_90)
            true_list_180.append(true_count_180)
            true_list_270.append(true_count_270)
            true_count = 0
            true_count_90 = 0
            true_count_180 = 0
            true_count_270 = 0
            #under edge
            for k in range (img_width - 1):
                direction = 2
                orgin_img_2 = norm_color_vector[i][img_height-1][k]
                compare_img_2 = norm_color_vector[j][0][k]
                compare_img_90_2 = norm_color_vector_90[j][0][k]
                compare_img_180_2 = norm_color_vector_180[j][0][k]
                compare_img_270_2 = norm_color_vector_270[j][0][k]
                percent_2 = np.dot(orgin_img_2,compare_img_2) / (np.linalg.norm(orgin_img_2) * np.linalg.norm(compare_img_2))
                percent_90_2 = np.dot(orgin_img_2,compare_img_90_2) / (np.linalg.norm(orgin_img_2) * np.linalg.norm(compare_img_90_2))
                percent_180_2 = np.dot(orgin_img_2,compare_img_180_2) / (np.linalg.norm(orgin_img_2) * np.linalg.norm(compare_img_180_2))
                percent_270_2 = np.dot(orgin_img_2,compare_img_270_2) / (np.linalg.norm(orgin_img_2) * np.linalg.norm(compare_img_270_2))
                if percent_2 >= 0.994:
                    true_count = true_count + 1
                if percent_90_2 >= 0.994:
                    true_count_90 = true_count_90 + 1
                if percent_180_2 >= 0.994:
                    true_count_180 = true_count_180 + 1
                if percent_270_2 >= 0.994:
                    true_count_270 = true_count_270 + 1
            direction_list.append(direction)
            true_list.append(true_count)   
            true_list_90.append(true_count_90)
            true_list_180.append(true_count_180)
            true_list_270.append(true_count_270)
            true_count = 0
            true_count_90 = 0
            true_count_180 = 0
            true_count_270 = 0
            #left edge
            for k in range(img_height - 1):
                direction = 3
                orgin_img_3 = norm_color_vector[i][k][0]
                compare_img_3 = norm_color_vector[j][k][img_width-1]
                compare_img_90_3 = norm_color_vector_90[j][k][img_width-1]
                compare_img_180_3 = norm_color_vector_180[j][k][img_width-1]
                compare_img_270_3 = norm_color_vector_270[j][k][img_width-1]
                percent_3 = np.dot(orgin_img_3,compare_img_3) / (np.linalg.norm(orgin_img_3) * np.linalg.norm(compare_img_3))
                percent_90_3 = np.dot(orgin_img_3,compare_img_90_3) / (np.linalg.norm(orgin_img_3) * np.linalg.norm(compare_img_90_3))
                percent_180_3 = np.dot(orgin_img_3,compare_img_180_3) / (np.linalg.norm(orgin_img_3) * np.linalg.norm(compare_img_180_3))
                percent_270_3 = np.dot(orgin_img_3,compare_img_270_3) / (np.linalg.norm(orgin_img_3) * np.linalg.norm(compare_img_270_3))
                if percent_3 >= 0.994:
                    true_count = true_count + 1
                if percent_90_3 >= 0.994:
                    true_count_90 = true_count_90 + 1
                if percent_180_3 >= 0.994:
                    true_count_180 = true_count_180 + 1
                if percent_270_3 >= 0.994:
                    true_count_270 = true_count_270 + 1
            direction_list.append(direction)
            true_list.append(true_count)   
            true_list_90.append(true_count_90)
            true_list_180.append(true_count_180)
            true_list_270.append(true_count_270)
            true_count = 0
            true_count_90 = 0
            true_count_180 = 0
            true_count_270 = 0
            #up edge
            for k in range(img_width - 1):
                direction = 4
                orgin_img_4 = norm_color_vector[i][0][k]
                compare_img_4 = norm_color_vector[j][img_height-1][0]
                compare_img_90_4 = norm_color_vector_90[j][img_height-1][0]
                compare_img_180_4 = norm_color_vector_180[j][img_height-1][0]
                compare_img_270_4 = norm_color_vector_270[j][img_height-1][0]
                percent_4 = np.dot(orgin_img_4,compare_img_4) / (np.linalg.norm(orgin_img_4) * np.linalg.norm(compare_img_4))
                percent_90_4 = np.dot(orgin_img_4,compare_img_90_4) / (np.linalg.norm(orgin_img_4) * np.linalg.norm(compare_img_90_4))
                percent_180_4 = np.dot(orgin_img_4,compare_img_180_4) / (np.linalg.norm(orgin_img_4) * np.linalg.norm(compare_img_180_4))
                percent_270_4 = np.dot(orgin_img_4,compare_img_270_4) / (np.linalg.norm(orgin_img_4) * np.linalg.norm(compare_img_270_4))
                if percent_4 >= 0.994:
                    true_count = true_count + 1
                if percent_90_4 >= 0.994:
                    true_count_90 = true_count_90 + 1
                if percent_180_4 >= 0.994:
                    true_count_180 = true_count_180 + 1
                if percent_270_4 >= 0.994:
                    true_count_270 = true_count_270 + 1
            direction_list.append(direction)
            true_list.append(true_count)   
            true_list_90.append(true_count_90)
            true_list_180.append(true_count_180)
            true_list_270.append(true_count_270)
            true_count = 0
            true_count_90 = 0
            true_count_180 = 0
            true_count_270 = 0
        #find max true num from each angle 
        max_true = max(true_list)
        index_true = true_list.index(max_true)
        max_true_90 = max(true_list_90)
        index_true_90 = true_list_90.index(max_true_90)
        max_true_180 = max(true_list_180)
        index_true_180 = true_list_180.index(max_true_180)
        max_true_270 = max(true_list_270)
        index_true_270 = true_list_270.index(max_true_270)
        
        final_true_list.append(max_true)
        final_index_list.append(index_true)
        final_true_list.append(max_true_90)
        final_index_list.append(index_true_90)
        final_true_list.append(max_true_180)
        final_index_list.append(index_true_180)
        final_true_list.append(max_true_270)
        final_index_list.append(index_true_270)

        max_num = max(final_true_list)
        final_index = final_true_list.index(max_num)
        angle_num = final_index_list[final_index]
        final_dictionary[final_index] = angle_num
        print(final_dictionary)
loader()
arrange()



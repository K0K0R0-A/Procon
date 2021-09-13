from PIL import Image
import numpy as np
from matplotlib import pylab as plt
import sys
import cv2

# img_path = "/Users/kokoro/Documents/procon_displace/img/chunk_116.png"
# img_path2 = "/Users/kokoro/Documents/procon_displace/img/chunk_117.png"

# img = np.array(Image.open(img_path))
# img2 = np.array(Image.open(img_path2))

# print("The first image shape is ",img.shape)
# print("The second image shape is ",img2.shape)
for i in range(1):
    true_count_list = []
    img_list = []
    img_angle = []
    final_img_list = []
    final_num_list = []
    img_path_list = []
    final_angle_list = []

    for j in range(2):

        if i < 9:
            path_1 = "/Users/kokoro/Documents/procon_displace/img/output_kiritanpo(2)/chunk_"+"0"+str(i)+".png"
            im1 = Image.open(path_1)
            img_c = np.array(im1)
            print("first_img : chunk_0"+str(i))
        else:
            path_1 = "/Users/kokoro/Documents/procon_displace/img/output_kiritanpo(2)/chunk_"+str(i)+".png"
            im1 = Image.open(path_1)
            img_c = np.array(im1)
            print("first_img : chunk_"+str(i))

        if j < 9:
            path_2 = "/Users/kokoro/Documents/procon_displace/img/output_kiritanpo(2)/chunk_"+"0"+str(j+1)+".png"
            im2 = Image.open(path_2)
            img_d = np.array(im2)
            print("second_img : chunk_0"+str(j+1))
        else:
            path_2 = "/Users/kokoro/Documents/procon_displace/img/output_kiritanpo(2)/chunk_"+str(j+1)+".png"
            im2 = Image.open(path_2)
            img_d = np.array(im2)
            print("second_img : chunk_"+str(j+1))

        img_path_list.append(path_2)
        img_sv = img_c.shape[0]
        img_sh = img_c.shape[1]
        true_count = 0
        false_count = 0

        for k in range(img_sv-1):
            imgv_c = img_c[k][img_sh-1]/255
            imgv_d = img_d[k][0]/255
            percent = np.dot(imgv_c,imgv_d) / (np.linalg.norm(imgv_c) * np.linalg.norm(imgv_d))
            # print(imgv_c," : ",imgv_d)
            # print("The percent in[ ", k ," ]rows is : ",percent)
            if percent>=0.994:
                true_count = true_count+1
            else :
                false_count = false_count+1    

        true_count_list.append(true_count)
        img_list.append(img_d)
        img_angle.append("Angle:0")
        print("true:",true_count)
        print("false:",false_count)

        true_count = 0
        false_count = 0
        img_rotate_1 = im2.rotate(90)
        img_d = np.array(img_rotate_1)
        img_sv = img_c.shape[0]
        img_sh = img_c.shape[1]
        for l in range(img_sv-1):
            imgv_c = img_c[l][img_sh-1]/255
            imgv_d = img_d[l][0]/255
            percent = np.dot(imgv_c,imgv_d) / ((np.linalg.norm(imgv_c)) * np.linalg.norm(imgv_d))
            # print(imgv_c," : ",imgv_d)
            # print("The percent in[ ", k ," ]rows is : ",percent)
            if percent>=0.994:
                true_count = true_count+1
            else :
                false_count = false_count+1   

        true_count_list.append(true_count)
        img_list.append(img_d)
        img_angle.append("Angle:90")
        print("true:",true_count)
        print("false:",false_count)

        true_count = 0
        false_count = 0
        img_rotate_2 = im2.rotate(180)
        img_d = np.array(img_rotate_2)
        img_sv = img_c.shape[0]
        img_sh = img_c.shape[1]
        for m in range(img_sv-1):
            imgv_c = img_c[m][img_sh-1]/255
            imgv_d = img_d[m][0]/255
            percent = np.dot(imgv_c,imgv_d) / ((np.linalg.norm(imgv_c)) * np.linalg.norm(imgv_d))
            # print(imgv_c," : ",imgv_d)
            # print("The percent in[ ", k ," ]rows is : ",percent)
            if percent>=0.994:
                true_count = true_count+1
            else :
                false_count = false_count+1   

        true_count_list.append(true_count)
        img_list.append(img_d)
        img_angle.append("Angle:180")
        print("true:",true_count)
        print("false:",false_count)

        true_count = 0
        false_count =0
        img_rotate_3 = im2.rotate(270)
        img_d = np.array(img_rotate_3)
        img_sv = img_c.shape[0]
        img_sh = img_c.shape[1]
        for n in range(img_sv-1):
            imgv_c = img_c[n][img_sh-1]/255
            imgv_d = img_d[n][0]/255
            percent = np.dot(imgv_c,imgv_d) / ((np.linalg.norm(imgv_c)) * np.linalg.norm(imgv_d))
            # print(imgv_c," : ",imgv_d)
            # print("The percent in[ ", k ," ]rows is : ",percent)
            if percent>=0.994:
                true_count = true_count+1
            else :
                false_count = false_count+1   

        true_count_list.append(true_count)
        img_list.append(img_d)
        img_angle.append("Angle:270")
        print("true:",true_count)
        print("false:",false_count)

        for m in range(len(true_count_list)-1):
            first_component = true_count_list[m]
            second_component = true_count_list[m+1]
            if(first_component > second_component):
                final_img = img_list[m]
                final_angle = img_angle[m]
                final_num = first_component
            else:
                final_img = img_list[m+1]
                final_angle = img_angle[m+1]
                final_num = second_component
        final_num_list.append(final_num)
        final_img_list.append(final_img)
        final_angle_list.append(final_angle)
    
    for o in range(len(final_num_list)-1):
        num_one = final_num_list[o]
        num_two = final_num_list[o+1]
        if(num_one > num_two):
            adjecent_img = final_img_list[o]
            img_path = img_path_list[o]
            angle_num = final_angle_list[o]
        else:
            adjecent_img = final_img_list[o+1]
            img_path = img_path_list[o+1]
            angle_num = final_angle_list[o+1]
    
    print(path_1)
    print("match with")
    print(img_path)
    print(angle_num)





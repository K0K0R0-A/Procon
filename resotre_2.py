from PIL import Image
import numpy as np
from matplotlib import pylab as plt
import sys
import cv2
img_slice_vertical = 4
img_slice_holizontal = 4
img_num = 16
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
    img_list = [f"/Users/kokoro/Documents/procon_displace/img/output_kiritanpo/chunk_{i}.png" for i in range(img_num-1)]
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
origin_compare_list = []
origin_ans_list = []
origin_index_list = []
origin_ans =[]
origin_index =[]
def make_one_list():
    for i in range (len(norm_color_vector)):
        pre_origin_list = []
        pre_origin_list.append(norm_color_vector[i])
        pre_origin_list.append(norm_color_vector_90[i])
        pre_origin_list.append(norm_color_vector_180[i])
        pre_origin_list.append(norm_color_vector_270[i])
        origin_list.append(pre_origin_list)
        origin_compare_list.append(pre_origin_list)
        origin_ans_list.append([0,1,2,3])
        origin_index_list.append([0,1,2,3])
        origin_ans.append(i)
        origin_index.append(i)
    del origin_compare_list[0]
    del origin_index_list[0]
    del origin_index[0]

img_width = norm_color_vector[1].shape[1]
img_height = norm_color_vector[1].shape[0]
answer_list = []
line_dictionary = {0:[0,1,2,3]}
angle_list = []
line_key = [0]
line_list = [[0,1,2,3]]
angle_samp = [0,1,2,3]
samp_list = []
#line_listの修正
def add_to_line(max_index,count,samp_num,g,check_index,edge):
    samp_list = []
    angle_samp = [0,1,2,3]
    angle_index = angle_samp.index(samp_num)
    del angle_samp[angle_index]

    if count == 0:
        check_del = check_index + 1
        if edge == False:
            if answer_list[check_del+1] != []:
                angle_index = angle_samp.index(0)
                del angle_samp[angle_index]
        if answer_list[check_del-img_slice_holizontal] != []:
            angle_index = angle_samp.index(3)
            del angle_samp[angle_index]
        if answer_list[check_del+img_slice_holizontal] != []:
            angle_index = angle_samp.index(1)
            del angle_samp[angle_index]

    if count == 1:
        check_del = check_index - img_slice_holizontal
        if edge == False:
            if answer_list[check_del-img_slice_holizontal] != []:
                angle_index = angle_samp.index(1)
                del angle_samp[angle_index]
        if answer_list[check_del-1] != []:
            angle_index = angle_samp.index(0)
            del angle_samp[angle_index]
        if answer_list[check_del+1] != []:
            angle_index = angle_samp.index(2)
            del angle_samp[angle_index]

    if count == 2:
        check_del = check_index - 1
        if edge == False:
            if answer_list[check_del-1] != []:
                angle_index = angle_samp.index(2)
                del angle_samp[angle_index]
        if answer_list[check_del-img_slice_holizontal] != []:
            angle_index = angle_samp.index(3)
            del angle_samp[angle_index]
        if answer_list[check_del+img_slice_holizontal] != []:
            angle_index = angle_samp.index(1)
            del angle_samp[angle_index]
                
    if count == 3:
        check_del = check_index + img_slice_holizontal
        if edge == False:
            if answer_list[check_del+img_slice_holizontal] != []:
                angle_index = angle_samp.index(3)
                del angle_samp[angle_index]
        if answer_list[check_del+1] != []:
            angle_index = angle_samp.index(2)
            del angle_samp[angle_index]
        if answer_list[check_del-1] != []:
            angle_index = angle_samp.index(0)
            del angle_samp[angle_index]
    # samp_num.append()
    print(angle_samp)
    line_list.append(angle_samp)
    line_key.append(max_index[0][0])
    line_dictionary[max_index[0][0]] = samp_list
def make_list():
    for i in range((img_slice_vertical)*(img_slice_holizontal)):
        a = []
        answer_list.append(a)
        angle_list.append(a)
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
#---------------------------------------------------------------------------------------
def arrange():
    num = 0
    num2 = 0
    num_c = 0
    num_c2 = 0
    pixel_length = origin_list[0][0].shape[0]
    length = pixel_length -1
    answer_list[0] = 0
    angle_list[0] = 0
    max_index = [[0,0]]
    max_list = []
    max_index_list = []
    line_max = []
    line_max_index = []
    true_list = []
    true_line_list = []
    #全画像分の数ループ
    for g in range(img_num):
        true_list = []
        angle_samp = [0,1,2,3]
        samp_list = []
        line_num = 0
        line_sum = 0
        line_element = []
        line_max = []
        line_max_index =[]
        check_max_list = []
        select_img = []
        #line_listに追加された画像分ループ
        for c in range(len(line_list)):
            line_img_num = line_key[c]
            max_list = []
            max_index_list = []
            #line_listに追加された画像の辺の分ループ
            for d in range(len(line_list[c])):
                line_angle_num = line_list[c][d]
                #比べる画像分ループ
                true_list = []
                true_line_list = []
                for i in range (len(origin_compare_list)):
                    true_count_0 = 0
                    true_count_90 = 0
                    true_count_180 = 0
                    true_count_270 = 0
                    pre_true_list = []
                    # 1ピクセルごとに比べる
                    for j in range(pixel_length-1):
                        if line_angle_num ==0:
                            num=j
                            num2=length
                            num_c = j
                            num_c2 = 0
                        elif line_angle_num ==1:
                            num=0
                            num2=j
                            num_c = length
                            num_c2 = j
                        elif line_angle_num ==2:
                            num=j
                            num2=0
                            num_c = j
                            num_c2 = length
                        elif line_angle_num ==3:
                            num=length
                            num2=j
                            num_c = 0
                            num_c2 = j
                        # x = find_num(origin_list,line_img_num,line_angle_num,num,num2,origin_compare_list,i,0,num_c,num_c2)
                        # x_90 = find_num(origin_list,line_img_num,line_angle_num,num,num2,origin_compare_list,i,1,num_c,num_c2)
                        # x_180 = find_num(origin_list,line_img_num,line_angle_num,num,num2,origin_compare_list,i,2,num_c,num_c2)
                        # x_270 = find_num(origin_list,line_img_num,line_angle_num,num,num2,origin_compare_list,i,3,num_c,num_c2)
                        origin_1 = origin_list[line_img_num][line_angle_num][num][num2]
                        compare_2 = origin_compare_list[i][0][num_c][num_c2]
                        compare_2_1 = origin_compare_list[i][1][num_c][num_c2]
                        compare_2_2 = origin_compare_list[i][2][num_c][num_c2]
                        compare_2_3 = origin_compare_list[i][3][num_c][num_c2]
                        percent_1 = np.dot(origin_1,compare_2) / (np.linalg.norm(compare_2) * np.linalg.norm(compare_2))
                        percent_2 = np.dot(origin_1,compare_2_1) / (np.linalg.norm(compare_2_1) * np.linalg.norm(compare_2_1))
                        percent_3 = np.dot(origin_1,compare_2_2) / (np.linalg.norm(compare_2_2) * np.linalg.norm(compare_2_2))
                        percent_4 = np.dot(origin_1,compare_2_3) / (np.linalg.norm(compare_2_3) * np.linalg.norm(compare_2_3))
                        if percent_1 >= 0.994:
                            true_count_0 = true_count_0 +1
                        if percent_2 >= 0.994:
                            true_count_90 = true_count_90 +1 
                        if percent_3 >= 0.994:
                            true_count_180 = true_count_180 +1 
                        if percent_4 >= 0.994:
                            true_count_270 = true_count_270 +1 
                    #ピクセルごとの類似度の合計を追加
                    pre_true_list.append(true_count_0)
                    pre_true_list.append(true_count_90)
                    pre_true_list.append(true_count_180)
                    pre_true_list.append(true_count_270)
                    true_list.append(pre_true_list)
                    # print("fir",len(true_list))
                # print("sec",len(true_list))
                #line_keyの画像それぞれの辺の類似度を求めて最大値を決める
                # print(true_list)
                max_samp = max(list(map(lambda y: max(y),true_list)))
                np_samp = np.array(true_list)
                pre_max_index_samp = np.argwhere(np_samp == max_samp)
                max_list.append(max_samp)
                max_index_list.append(pre_max_index_samp[0])
            #上の最大値をline_key分用意してその中で最大値を決める
            # print(pre_max_index_samp)
            max_samp_2 = max(max_list)
            max_index_num = max_list.index(max_samp_2)
            final_max_index = max_index_list[max_index_num]
            line_max.append(max_samp_2)
            line_max_index.append(final_max_index)
            check_max_list.append(max_list)
        #max_listを全部入れるlistが必要
        #追加する側のindex
        max_n = max(line_max)
        max_i = line_max.index(max_n)
        max_f = line_max_index[max_i]
        #追加される側のindex
        for i in range(len(check_max_list)-1):
            if len(check_max_list[i]) == 0:
                del check_max_list[i]
        np_max = np.argmax(check_max_list)
        max_check = False
        max_count = 0
        # print(check_max_list)
        while True:
            if np_max > (len(check_max_list[max_count])-1):
                np_max = np_max - len(check_max_list[max_count])
                max_count = max_count + 1
            else:
                test = [(max_count,np_max)] 
                break
        # re_max = max(list(map(lambda y: max(y),check_max_list)))
        # np_check = np.array(check_max_list)
        # np_index = np.argwhere(np_check == re_max)
        # for y, row in enumerate(check_max_list):
        #     try:
        #         pos = (y, row.index(re_max))
        #         break
        #     except ValueError:
        #         pass
        # test = [pos]
        max_num = test
        #checkの追加
        img_rotate = max_num[0][1]
        check_num = line_key[max_num[0][0]]
        check = answer_list.index(check_num)
        old_check = check_num
        #追加する側のindexの修正
        ans_1 = origin_index[max_f[0]]
        ans_img = origin_ans.index(ans_1)
        max_index[0][0] = ans_img
        max_index[0][1] = max_f[1]
        # print(check)
        # print(max_num)
        # print(line_list)
        judgement = False
#---------------------------------------------------------------------------------------
        loop_count = 0
        while judgement == False:
            #上の最大値をline_key分用意してその中で最大値を決める
            if loop_count > 0:
                #追加する側のindex
                max_n = max(line_max)
                max_i = line_max.index(max_n)
                max_f = line_max_index[max_i]
                #追加される側のindex
                for i in range(len(check_max_list)-1):
                    if len(check_max_list[i]) == 0:
                        del check_max_list[i]
                # print((check_max_list))
                np_max = np.argmax(check_max_list)
                max_check = False
                max_count = 0
                while True:
                    if np_max > (len(check_max_list[max_count])-1):
                        np_max = np_max - len(check_max_list[max_count])
                        max_count = max_count + 1
                    else:
                        test = [(max_count,np_max)] 
                        break
                max_num = test
                #checkの追加
                img_rotate = max_num[0][1]
                check_num = line_key[max_num[0][0]]
                check = answer_list.index(check_num)
                old_check = check_num
                #追加する側のindexの修正
                ans_1 = origin_index[max_f[0]]
                ans_img = origin_ans.index(ans_1)
                max_index[0][0] = ans_img
                max_index[0][1] = max_f[1]
            print(line_list)
            print(max_num)
            print("num",check,img_rotate)
            print("index",max_index)
            loop_count = loop_count + 1
            count = img_rotate
            del check_max_list[max_num[0][0]][max_num[0][1]]
            #最大値のindexの値を正しい表記に直す
            while True:
                if max_index[0][0] >= img_num-1:
                    max_index[0][0] = max_index[0][0] - (img_num-1)
                else:
                    break
            right_blank = 0
            up_blank = 0
            right_count = 0
            left_count = 0
            left_blank = 0
            down_blank = 0
            down_n = 0
#---------------------------------------------------------------------------------------
            #選択された画像が最右段にあるかどうかと最左段に要素があるかどうかの確認
            for i in range(1,img_slice_vertical+1):
                right_num = (img_slice_holizontal*i)-1
                if right_num == check:
                    right_count = right_count+1
                right_n = img_slice_holizontal*i-img_slice_holizontal
                if (answer_list[right_n]) == []:
                    right_blank = right_blank+1
            #最下段に要素があるかどうかの確認
            for i in range(img_slice_holizontal):
                up_n = (img_num-img_slice_holizontal)+i
                if (answer_list[up_n]) == []:
                    up_blank = up_blank +1
            #選択された画像が最左段にあるかどうかと最右段に要素があるかどうかの確認
            for i in range(1,img_slice_vertical+1):
                left_num = (img_slice_holizontal*i)-img_slice_holizontal
                if left_num == check:
                    left_count = left_count+1
                left_n = (img_slice_holizontal*i)-1
                if (answer_list[left_n]) == []:
                    left_blank = left_blank+1
            #最上段に要素があるかどうかの確認
            for i in range(img_slice_holizontal):
                if (answer_list[down_n]) == []:
                    down_blank = down_blank +1
                down_n = down_n + 1
#---------------------------------------------------------------------------------------

            #画像が右端だった時に指定された場所が右側だった場合
            if count == 0 and right_count>=1:
                #最左段に要素が無ければ、最左段を消して最右段に一列追加
                if right_blank == img_slice_vertical:
                    for i in range(1,img_slice_vertical+1):
                        del_num = (img_slice_holizontal*i)-img_slice_holizontal
                        insert_num = (img_slice_holizontal*i)-1
                        del answer_list[del_num]
                        del angle_list[del_num]
                        answer_list.insert(insert_num,[])
                        angle_list.insert(insert_num,[])
                    new_check = answer_list.index(old_check)
                    answer_list[new_check+1] = max_index[0][0]
                    angle_list[new_check+1] = max_index[0][1]
                    del origin_compare_list[max_f[0]]
                    # del origin_index_list[max_index[0][0]]
                    del origin_index[max_f[0]]
                    samp_num = 2
                    add_to_line(max_index,count,samp_num,g,new_check,True)
                    del line_list[max_num[0][0]][max_num[0][1]]
                    judgement = True
            #指定された場所が右側で、画像が最右段じゃない時
            elif count == 0 and answer_list[check+1]==[]:
                answer_list[check+1] = max_index[0][0]
                angle_list[check+1] = max_index[0][1]
                del origin_compare_list[max_f[0]]
                # del origin_index_list[max_index[0][0]]
                del origin_index[max_f[0]]
                samp_num = 2
                add_to_line(max_index,count,samp_num,g,check,False)
                del line_list[max_num[0][0]][max_num[0][1]]
                judgement = True
            #画像が最上列だった時に指定された場所が上な時
            if count == 1 and check <= img_slice_holizontal-1:
                #最下段に要素が無ければ、最下段を消して最上段に一列追加
                if up_blank == img_slice_holizontal:
                    for i in range(img_slice_holizontal):
                        del answer_list[(len(answer_list))-1]
                        del angle_list[(len(angle_list))-1]
                        answer_list.insert(0,[])
                        angle_list.insert(0,[])
                    new_check = answer_list.index(old_check)
                    answer_list[new_check-img_slice_holizontal] = max_index[0][0]
                    angle_list[new_check-img_slice_holizontal] = max_index[0][1]
                    del origin_compare_list[max_f[0]]
                    # del origin_index_list[max_index[0][0]]
                    del origin_index[max_f[0]]
                    samp_num = 3
                    add_to_line(max_index,count,samp_num,g,new_check,True)
                    del line_list[max_num[0][0]][max_num[0][1]]
                    judgement = True
            #指定された場所が上で、画像が最上段じゃない時
            elif count == 1 and answer_list[check-img_slice_holizontal]==[]:
                answer_list[check - img_slice_holizontal] = max_index[0][0]
                angle_list[check - img_slice_holizontal] = max_index[0][1]
                del origin_compare_list[max_f[0]]
                # del origin_index_list[max_index[0][0]]
                del origin_index[max_f[0]]
                samp_num = 3
                add_to_line(max_index,count,samp_num,g,check,False)
                del line_list[max_num[0][0]][max_num[0][1]]
                judgement = True
            #画像が左端だった時に指定された場所が左側だった場合
            if count ==2 and left_count >=1 and max_num[0][1]!= 0:
                #最右段に要素が無ければ、最右段を消して最左段に一列追加
                if left_blank == img_slice_vertical:
                    for i in range(1,img_slice_vertical+1):
                        del_num = (img_slice_holizontal*i)-1
                        insert_num = (img_slice_holizontal*i)-img_slice_holizontal
                        del answer_list[del_num]
                        del angle_list[del_num]
                        answer_list.insert(insert_num,[])
                        angle_list.insert(insert_num,[])
                    new_check = answer_list.index(old_check)
                    answer_list[new_check-1] = max_index[0][0]
                    angle_list[new_check-1] = max_index[0][1]
                    del origin_compare_list[max_f[0]]
                    # del origin_index_list[max_index[0][0]]
                    del origin_index[max_f[0]]
                    samp_num = 0
                    add_to_line(max_index,count,samp_num,g,new_check,True)
                    del line_list[max_num[0][0]][max_num[0][1]]
                    judgement = True
            #指定された場所が左で、画像が最左段じゃない時
            elif count == 2 and answer_list[check-1]==[]:
                answer_list[check-1] = max_index[0][0]
                angle_list[check-1] = max_index[0][1]
                del origin_compare_list[max_f[0]]
                # del origin_index_list[max_index[0][0]]
                print(origin_index)
                print(max_index[0][0])
                # origin_index_num = origin_index.index(max_index[0][0])
                del origin_index[max_f[0]]
                samp_num = 0
                add_to_line(max_index,count,samp_num,g,check,False)
                del line_list[max_num[0][0]][max_num[0][1]]
                judgement = True
            #画像が最下段だった時に指定された場所が下な時
            if count == 3 and check >= img_num - img_slice_holizontal and max_num[0][1]!= 1:
                #最上段に要素が無ければ、最上段を消して最下段に一列追加
                if down_blank == img_slice_holizontal:
                    for i in range(img_slice_holizontal):
                        del answer_list[0]
                        del angle_list[0]
                        answer_list.insert(len(answer_list)-1,[])
                        angle_list.insert(len(angle_list)-1,[])
                    new_check = answer_list.index(old_check)
                    answer_list[new_check+img_slice_holizontal] = max_index[0][0]
                    angle_list[new_check+img_slice_holizontal] = max_index[0][1]
                    del origin_compare_list[max_f[0]]
                    # del origin_index_list[max_index[0][0]]
                    del origin_index[max_f[0]]
                    samp_num = 1
                    add_to_line(max_index,count,samp_num,g,new_check,True)
                    del line_list[max_num[0][0]][max_num[0][1]]
                    judgement = True
            #指定された場所が下で、画像が最下段じゃない時
            elif count == 3 and answer_list[check+img_slice_holizontal]==[]:
                answer_list[check+img_slice_holizontal] = max_index[0][0]
                angle_list[check+img_slice_holizontal] = max_index[0][1]
                del origin_compare_list[max_f[0]]
                # del origin_index_list[max_index[0][0]]
                del origin_index[max_f[0]]
                samp_num = 1
                add_to_line(max_index,count,samp_num,g,check,False)
                del line_list[max_num[0][0]][max_num[0][1]]
                judgement = True
        # print(count)
        print("ans",answer_list)
        print("ang",angle_list)
        # print(line_list)
        # print(line_key)
main()

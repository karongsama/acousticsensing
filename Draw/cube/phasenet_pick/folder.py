import os
import numpy
import cv2

path=r'D:\coding\AcousticSensing\Draw\cube\phasenet_pick'
# for i in range(24):
#     os.mkdir(path+'\\'+str(i+1))

# 读取全部jpg文件
def read_all_jpg(path):
    file_list = []
    files = os.listdir(path)
    for f in files:
        if os.path.splitext(f)[1] == '.jpg':
            file_list.append(f)
    return file_list

todolist=read_all_jpg(path)
for i in range(len(todolist)):
    #截取下划线前的数字
    num=int(todolist[i].split('_')[0])
    #根据数字存入对应文件夹
    img=cv2.imread(path+'\\'+todolist[i])
    cv2.imwrite(path+'\\'+str(num)+'\\'+todolist[i],img)
import os
import sys
from webbrowser import get

temp_=os.path.realpath(sys.argv[0])     # 获取当前运行的文件名称
#print(os.path.dirname(temp_))     




def get_allfile(path):  # 获取所有文件
    str1 = ''
    all_file = []
    for f in os.listdir(path):  #listdir返回文件中所有目录
        #f_name = os.path.join(path, f)

        f_name = os.path.join(path, f)
        all_file.append(f_name)

        all_file.append(f)
        if str1 != '':
            str1 = str1 + "|"+f_name
        else:
            str1 +=f_name





    return str1


def getfile(name):
    all_file=get_allfile(os.path.dirname(temp_)+name)  #tickets要获取文件夹名
    
    return all_file


 
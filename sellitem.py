from locale import currency
import math
from multiprocessing import ProcessError
import random
import threading
import time ,_FindMost,path
import tkinter
import win32com.client
dm = win32com.client.Dispatch('dm.dmsoft')



print(dm.ver())#输出版本号
def findPic():
    picstr= path.getfile("/sell")

    intX=0
    intY=0
    isI, px, py =dm. FindPic(0,0,1920,1080, picstr,"000000",1,0,intX,intY)
    print(  isI, px, py)
    if isI != -1: 
        
    
            dm.moveto(px, py)
            time.sleep(0.1)
            dm.leftclick()
            time.sleep(0.1)

            isI, px, py =dm. FindPic(0,0,1920,1080, 'sellbut.bmp',"000000",1,0,intX,intY)
            print(  isI, px, py)
            if isI != -1: 
                
    
                dm.moveto(px, py)
                time.sleep(0.1)
                dm.leftclick()
                time.sleep(0.1)



findPic()

for  i in  range(20):
    findPic()
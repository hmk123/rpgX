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

#dm.SetDict(112233,"d:\\Desktop\\3.1233\\num.txt")
#dm.UseDict(112233)

hwnd = dm.FindWindow("","Digimon RPG")
if (hwnd != 0 ) :
    dm.SetWindowState(hwnd, 1)
    flag = dm.BindWindow(hwnd,"normal","normal","normal",0)
 
    
    if flag != 1:
        flag =dm.BindWindow(hwnd,"dx","windows3","windows",0)
    if flag != 1:   
        exit(0)

mo= [   ["ffff94","2|-18|944539,4|-27|944539,8|2|d6b663,3|8|c6aa5a"],
        ["ffff94","2|-18|944539,4|-27|944539,8|2|d6b663,3|8|c6aa5a"],
        ["d6ba63","4|-1|e76d5a,-3|-1|ceae5a,3|-2|9c4942,1|3|5a2c21"],
        ["bda252","-6|-5|e7695a,-5|-7|e7695a,-3|10|b55942,1|-1|c6a65a"]


    ]

def find():
    px = 0 
    py = 0
    isI = 0
    x = 0
    y = 0
    while 1 :      
        for     item in mo:    
            isI, px, py = dm.FindMultiColor(0, 0, 800, 600, item[0], item[1], 1.0, 1, x, y)
            if isI == 1:
                pass
#t1 = threading.Thread(target=find)
#t1.setDaemon(True)
#t1.start()








state = {   "find" :   _FindMost.  findM(dm)            }
currState = "find"
t = time.time()
tt = 0
 


def moveP(radius,x,y):
           # 圆半径
    min_angle = 0       # 每次循环角度计算
    max_angle = 360     # 最大角度
    spacing = 35        # 三角形的角度 可调整
    duration = 0.0      # 鼠标移动速度
    while min_angle <= max_angle:
            time.sleep(0.01)
            # 角度计算
            min_angle += spacing
            # x,y 绝对坐标计算ZZZZ
            x2 = ('%.0f' % (x + radius * math.cos(min_angle * math.pi / 180)))
            y2 = ('%.0f' % (y + radius * math.sin(min_angle * math.pi / 180)))
            
            v = "ce75de","5|-2|efaeff,0|-5|f7d3ff,4|0|b565bd,-1|-2|d696de"
            b= "fffbd6","5|0|fffbd6,5|6|310000,-2|7|182c5a,7|4|ad9263"
            

            # 绝对坐标移动鼠标
            dm.moveTo(int(x2), int(y2))
            time.sleep(0.02)
            intX=0
            intY=0
            isI, px, py = dm.FindMultiColor(0, 0, 800, 600, v[0], v[1], 1.0, 1, intX,intY)
            
            if isI == 1: 
                dm.KeyDownChar("ctrl")
                dm.moveto(int(x2), int(y2))
                time.sleep(0.1)
                dm.leftclick()
                dm.KeyUpChar("ctrl")
                time.sleep(0.5)
                return
           
            isI, px, py =dm. FindPic(0, 0, 799, 599, "e.bmp","000000",0.9,0,intX,intY)

            if isI != -1: 
                dm.KeyDownChar("ctrl")
                dm.moveto(int(x2), int(y2))
                time.sleep(0.02)
                dm.leftclick()
                dm.KeyUpChar("ctrl")
                return

               


##  pic 




def findPic():
    picstr= path.getfile("/long")

    intX=0
    intY=0
    isI, px, py =dm. FindPic(18,7,784,453, picstr,"000000",1,0,intX,intY)
    print(  isI, px, py)
    if isI != -1: 
    
            moveP(random.randrange(35,50),px, py)
        


f= findPic

def clickitem():

    itempic = path.getfile("/item")
    intX=0
    intY=0
    dm.KeyDownChar("alt")
    isI, px, py =dm. FindPic(0, 0, 799, 599, itempic,"000000",1,0,intX,intY)
    if isI != -1: 
        dm.moveto(int(px)+5, int(py))
        time.sleep(0.02)
        dm.leftclick()
    dm.KeyUpChar("alt")


def shiftZ ():
        
    b_mian = "29a2ce","27|1|6bef7b,31|7|31c3e7,25|-5|84a66b,14|16|31c3e7"
    intX=0
    intY=0
    while 1:
        if dm.FindMultiColor(0, 0, 800, 600, b_mian[0], b_mian[1], 1.0, 1,intX,intY)[0]!=1:
            break

        picstr= path.getfile("/me")

        intX=0
        intY=0
        ###isI, px, py =dm. FindPic(18,7,784,453, picstr,"000000",1,0,intX,intY)
    

        

        isI, px, py =dm. FindPic(0, 0, 799, 599, "me/2.bmp","000000",0.9,0,intX,intY)
        if isI !=-1: 
                break
        else:
            dm.KeyDownChar("shift")
            dm.KeyPressChar("z") 
            dm.KeyUpChar("shift")
            



evo = shiftZ
ci = clickitem







 

if __name__=='__main__':

    while   1 :

        




#####if t +1/20< time.time():  
                
            t = time.time()
            tt+= 1
            #print(tt)iiiiiiiiii
            if  state[currState] .ischange == True:
                currState = state[currState].nextStare
        
            state[currState].updata(dm,f,ci,evo)
        

 

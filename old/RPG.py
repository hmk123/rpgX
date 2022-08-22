# coding:utf-8
from cmath import e
import win32com.client
import  time
import threading
import random
import win32con

import win32gui,win32api

import time

dm = win32com.client.Dispatch('dm.dmsoft')



print(dm.ver())#输出版本号

#dm.SetDict(0,"d:\\Desktop\\3.1233\\num.txt")
#dm.UseDict(0)

hwnd = dm.FindWindow("","Digimon RPG")
if (hwnd != 0 ) :
    dm.SetWindowState(hwnd, 1)
    flag = dm.BindWindow(hwnd,"normal","normal","normal",0)

    print(flag)
    if flag != 1:
        exit()

intX=0
intY=0









def anjian(s):
    time.sleep(0.02)
    dm.KeyPressChar (s)
    time.sleep(0.02)
    dm.KeyUpChar (s)
    time.sleep(0.02)


battleTga = "6bef7b","-2|8|84fb63,10|0|6bef7b,13|8|84fb63"
Tp = "efb629","2|-6|214d84,8|-2|f7e339,3|-3|f7ef4a"
R = "007994","-3|2|6bebff,-1|-6|6bebff,-5|-2|007994"

R0 = "08457b","6|3|00ffff,6|-1|00ffff,4|5|00ffff"
isbattle = False


def daguai (x,y):
    dm.moveto(x, y)
    time.sleep(0.06)
    dm.leftclick()


def zhaohuan ():
    ret, Rx, Ry = dm.FindMultiColor(0, 0, 800, 600, R[0], R[1], 1.0, 1, intX, intY)
    if ret == 1:
        dm.moveto(Rx, Ry)
        time.sleep(0.05)
        dm.leftclick()
        time.sleep(0.2)
        ret, x, y = dm.FindMultiColor(0, 0, 800, 600, R0[0], R0[1], 1.0, 1, intX, intY)
        if ret == 1:
            dm.moveto(x, y)
            time.sleep(0.1)
            dm.leftclick()

            NoTP()
            # print("TP")

        else:
            dm.moveto(Rx, Ry)
            time.sleep(0.05)
            dm.leftclick()
            time.sleep(0.1)


def TP():
    while 1:
        if (dm.FindMultiColor(0, 0, 800, 600, Tp[0], Tp[1], 1.0, 1, intX, intY)[0] == 1):
            break
def NoTP():
    while 1:
        if (dm.FindMultiColor(0, 0, 800, 600, Tp[0], Tp[1], 1.0, 1, intX, intY)[0] == 0):
            break


ch = "e72c52","-1|14|ffd7d6,1|31|ffdfde,4|4|e72c39,-8|24|4a9642,-12|15|397d31"
at = "00e3f7","-14|17|00e3f7,4|31|00e3f7,17|8|00e3f7,14|4|006d9c,-11|28|006d9c"

def bt():
    isbattle = False
    while 1 :
        if (dm.FindMultiColor(0, 0, 800, 600, battleTga[0],battleTga[1], 1.0, 1, intX, intY)[0] == 1):

            if (isbattle == False):

                TP()
                if 0 :
                    #zhaohuan()
                    TP()
                    #zhaohuan()
                    TP()

               # print("TP")

                print( u"上卡" )
                anjian("1")
                anjian("2")
                anjian("3")
                anjian("1")
                anjian("2")
                anjian("3")

                anjian("F3")
                daguai(228,187)
                isbattle = True
            else:
                continue

                if (dm.FindMultiColor(0, 0, 800, 600, Tp[0], Tp[1], 1.0, 1, intX, intY)[0] == 1):
                    if (dm.FindMultiColor(0, 0, 800, 600, ch[0], ch[1], 1.0, 1, intX, intY)[0] == 1):
                        anjian("Tab")
                        time .sleep(0.05)
                    else:
                        if (dm.FindMultiColor(4,0,522,454, at[0], at[1], 1.0, 1, intX, intY)[0] == 0):

                            anjian("F3")
                            # 228,187  102,250   357,117 232,123 103,185
                            #TP()
                            daguai(228,187)

                            if 0:
                                daguai(102,250)
                                daguai( 357,117)
                                daguai(232,123)
                                daguai(103,185)

                else:
                    if 0:
                        anjian("Tab")

        else:
            isbattle = False

def ling():
    while 1:

        dm.SetWindowState(hwnd, 1)
        time.sleep(1 )
        daguai(405,368)

        time .sleep( 1*10*60)
bt()


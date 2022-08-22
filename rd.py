from locale import currency
import math
import threading
import time ,_FindMost,path
import tkinter
import win32com.client
dm = win32com.client.Dispatch('dm.dmsoft')







print(dm.ver())#输出版本号

hwnd = dm.FindWindow("","Digimon RPG")
value = dm.ReadInt(hwnd,"BBBBBB",0)
print(value)


while   1 :


    dm.RightClick()
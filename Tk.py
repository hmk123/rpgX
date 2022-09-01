from ast import Break
from cgitb import text
from tkinter import *
from tkinter import messagebox
import threading

root =  Tk()

Label(root,text='账号:').place(x=10,y=10)
a_L=Entry(root)
a_L.place(x=50,y=10)

Label(root,text='密码:').place(x=10,y=40)
p_L= Entry(root)
p_L.place(x=50,y=40)

isStart = False
t1 = None




def helloCallBack():
    global t1 , isStart
    if    a_L .get() != '123'   or     p_L .get() != '123' :
        msg()
        isStart = False
        t1 = None
        return

    
    b['text'] ="停止"
    while 1:
        if isStart != True:

            b['text'] ="开始"
            break
        
        pass

def startFun(event):
    global isStart , t1
    if t1 == None  :
        isStart = True
        t1=threading.Thread(target=helloCallBack)
        t1.setDaemon(True)
        t1.start()

    else:
        isStart = False
        t1 = None

    
    

b = Button ( root, text ="点我" )
b.place ( x = 160, y = 70 )
b.bind ( "<Button-1>", startFun )

b = Button ( root, text ="点我" )
b.place ( x = 160, y = 130 )
b.bind ( "<Button-1>", startFun )




def msg ():
    messagebox.showinfo("error","erroe")


# <KeyPress-A> <Control-V> <F1>

menuBar= Menu(root)
Amenu= Menu(menuBar)
fg= Menu(menuBar)
for item in ["加钱",'充值']:
    Amenu.add_command ( label = item )

menuBar.add_cascade ( label= "设置", menu= Amenu  )
menuBar.add_cascade ( label= "设置", menu= Amenu  )



def pop(event):
    menuBar.post(event.x_root, event.y_root)
root.bind( "<Button-3>",pop)


root['menu'] = menuBar


root.geometry('300x300+500+200')
root.mainloop()
 




 
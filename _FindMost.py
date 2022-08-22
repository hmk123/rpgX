 
 
import time



ts= "0096ef","26|7|0092de,0|8|422c6b,35|2|0096e7,42|5|000818"

b= "fffbd6","5|0|fffbd6,5|6|310000,-2|7|182c5a,7|4|ad9263"
v = "ce75de","5|-2|efaeff,0|-5|f7d3ff,4|0|b565bd,-1|-2|d696de"


b_mian = "29a2ce","27|1|6bef7b,31|7|31c3e7,25|-5|84a66b,14|16|31c3e7"

card = "de9e84,-8|29|006584,29|29|006584,66|29|2182a5,37|6|ce9684"



slot1 = "efa284","-13|30|006584,3|40|00bace,-11|38|218aad,2|26|217d9c"
slot2 ="ffa67b","0|26|006584,16|35|0096ad,8|23|21829c,6|22|005d84"
slot3 = "ce927b","-6|0|ffa67b,17|34|08bece,4|20|217d9c,15|38|10cbd6"


m="0086b5","9|15|2196b5,-33|-3|0075ad,-77|13|00c7e7,11|-11|088ec6"

 
mo= [   ["ffff94","2|-18|944539,4|-27|944539,8|2|d6b663,3|8|c6aa5a"],
    
]

tp="efb629","7|-5|a57910,2|3|a57910,-1|-1|f7c329,2|2|efb629"


class findM:
    def __init__(self,dm) :

        self. ischange = False
        self. nextStare =""

        self.intX=300
        self.intY=0
        self.dm=dm
        
        self.carf = 0
        self.time=0

        self.nid = 0


    def skill(self,dm) :
        intX=0
        intY=0
        t = time.time()
        while 1:
            if t + 1 < time.time():  
                break
            
            if dm.FindMultiColor(0, 0, 800, 600, b_mian[0], b_mian[1], 1.0, 1,intX,intY)[0]!=1:
                
                break
            isI, px, py =dm. FindPic(0, 0, 799, 599, "F3.bmp","000000",0.9,0,intX,intY)
            if isI == -1:       
                dm.KeyPressChar("F3") 
            else:
                break
            

    issm1 = False 

    def sum(self,dm):
        return
        t = time.time()
        while 1:
            if t + 6 < time.time():  
                break
            if  dm.CmpColor(469,486,"f7e339",1) == 0:
                dm.KeyPressChar("R") 
                time.sleep(0.02*6)
                dm.moveto(291,43)
                time.sleep(0.02*6)
                dm.leftclick()
                time.sleep(0.5*6)
#291,43


    def shiftCard(self,dm) :

        t = time.time()
        while 1:
            if t + 6 < time.time():  
                break
   
            x=0
            y=0
   
            if dm.FindMultiColor(0, 0, 800, 600, slot1[0], slot1[1], 1.0, 1, x, y)[0]==1:


                dm.KeyPressChar("1")
                continue             
            elif dm.FindMultiColor(0, 0, 800, 600, slot2[0], slot2[1], 1.0, 1, x, y)[0]==1:
                dm.KeyPressChar("2")               
                continue                             
            elif dm.FindMultiColor(0, 0, 800, 600, slot3[0], slot3[1], 1.0, 1, x, y)[0]==1:
                dm.KeyPressChar("3")                
                continue  
            else:
                break
                #if dm.FindMultiColor(0, 0, 800, 600, tp[0], tp[1], 1.0, 1, x, y)[0]==1:
            
 

    def c (self,dm):
        intX=0
        intY=0
        isI, px, py =dm. FindPic(0, 0, 799, 599, "start.bmp","000000",0.9,0,intX,intY)
        time.sleep(0.2)
        if isI != -1: 
            dm.KeyPressChar("esc")
            time.sleep(0.5)



    def updata(self,dm , ff,ci,evo):
        x=0
        y=0
        isI=0
        px=0
        py=0

        self.c(dm)

        if dm.FindMultiColor(0, 0, 800, 600, m[0], m[1], 1.0, 1, x, y)[0]==1:
            self.hevp(dm)
            
            ci()
            ci()
            ci()
            ff() 
 
 
    

 
       
        if dm.FindMultiColor(0, 0, 800, 600, b_mian[0], b_mian[1], 1.0, 1, x, y)[0]==1:
                evo()
            #dm.FindMultiColor(0, 0, 800, 600, card[0], card[1], 1.0, 1, x, y)[0]==1:
                self.sum(dm)
                self.shiftCard(dm)
                self.skill(dm)
                self.act(dm)

                 
            
        else:
            self.carf = 0

    def daguai(self,x,y,dm):
        dm.moveto(x,y)
        time.sleep(0.02)
        dm.leftclick()


    def act(self,dm):
        t = time.time()
        x=0
        y=0
        while 1:
            if t + 60 < time.time():  
                break
            if dm.FindMultiColor(0, 0, 800, 600, b_mian[0], b_mian[1], 1.0, 1, x, y)[0]==1:
               
            #dm.FindMultiColor(0, 0, 800, 600, card[0], card[1], 1.0, 1, x, y)[0]==1:

                if dm.FindMultiColor(0, 0, 800, 600, tp[0], tp[1], 1.0, 1, x, y)[0]==1:
 
                    self.daguai(228,187,dm)
                    self.daguai(102,250,dm)
                    self. daguai( 357,117,dm)
                    self.daguai(232,123,dm)
                    self.daguai(103,185,dm)
            else:
                break


    def hevp(self ,dm):
        intX=0
        intY=0
        isI, px, py =dm. FindPic(0, 0, 799, 599, "evp.bmp","000000",0.9,0,intX,intY)
        time.sleep(0.2)
        if isI == -1: 
            dm.KeyPressChar("i")
            time.sleep(0.2)
                  
             
            isI, px, py =dm. FindPic(0, 0, 799, 599, "bag.bmp","000000",0.9,0,intX,intY)
            if isI != -1: 
                isI, px, py =dm. FindPic(0, 0, 799, 599, "evpF.bmp","000000",0.9,0,intX,intY)
                if isI != -1: 
                    dm.moveto(px,py)
                    time.sleep(0.5)
                    dm.RightClick()
                    time.sleep(0.5)
                    dm.KeyPressChar("i")
                    time.sleep(0.5)



                   



                self.closebag(dm)
                  
    def closebag(dm)    :   

                    isI=-1
                    while   
                    intX=0
                    intY=0       
                    isI, px, py =dm. FindPic(0, 0, 799, 599, "bag.bmp","000000",0.9,0,intX,intY)
                    if isI != -1: 
                        dm.KeyPressChar("i")
                        time.sleep(0.5) 
 
 
 
 
 
 
 
 

                    

                 




 




            

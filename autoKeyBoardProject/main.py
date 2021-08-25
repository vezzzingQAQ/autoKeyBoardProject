import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from time import sleep
from timer import Timer
cap=cv2.VideoCapture(0)
#设置宽高
cap.set(3,1280)
cap.set(4,720)
#创建一个手势检测器
detector=HandDetector(detectionCon=0.8)#检测精度

keys=[["Q","W","E","R","T","Y","U","I","O","P"],
    ["A","S","D","F","G","H","J","K","L",";"],
    ["Z","X","C","V","B","N","M",",",".","/"]]
textOutput=""
#绘制所有按钮
def drawAllButton(img,buttonList):
    for button in buttonList:
        x,y=button.position
        w,h=button.size
        cv2.rectangle(img,button.position,(x+w,y+h),(0,255,0),2)
        cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
    return(img)

#显示键盘类
class Button():
    def __init__(self,position,text,size=(85,85)):
        self.position=position
        self.text=text
        self.size=size        

buttonList=[]
for i in range(len(keys)):
    for j,key in enumerate(keys[i]):
        buttonList.append(Button([100*j+50,100*i+50],key))

def postImg():
    global textOutput
    success,img=cap.read()
    #找到手
    if success:
        img = cv2.flip(img,180)
    img=detector.findHands(img)
    #绘制图形
    lmList,boundingBoxInfo=detector.findPosition(img)
    #绘制键盘
    img=drawAllButton(img,buttonList)

    #检测点击
    if lmList:#检测到手
        for button in buttonList:
            x,y=button.position
            w,h=button.size
            #lmList[8][0]#食指x坐标【https://google.github.io/mediapipe/solutions/hands】
            if x<lmList[8][0]<x+w and y<lmList[8][1]<y+h:
                cv2.rectangle(img,button.position,(x+w,y+h),(0,255,0),5)
                cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
                l,_,_=detector.findDistance(4,6,img,draw=False)
                print(l)
                if l<70:
                    #点击
                    cv2.rectangle(img,button.position,(x+w,y+h),(0,255,0),cv2.FILLED)
                    cv2.putText(img,button.text,(x+20,y+65),cv2.FONT_HERSHEY_PLAIN,4,(255,255,255),4)
                    textOutput+=button.text
                    sleep(0.2)

    cv2.rectangle(img,(50,350),(700,450),(175,0,175),cv2.FILLED)
    cv2.putText(img,textOutput,(60,425),cv2.FONT_HERSHEY_PLAIN,5,(255,255,255),5)
    #显示画面
    #cv2.imshow("Image",img)
    cv2.waitKey(1)
    return(img)

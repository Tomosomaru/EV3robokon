#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks import ev3brick as brick
import time

def display ():
    brick.display.text("0:TimePeriod",(0,20))
    brick.display.text(timePeriod,(120,20))
    brick.display.text("1:Proportion",(0,30))
    brick.display.text(constantProportional,(120,30))
    brick.display.text("2:Integral",(0,40))
    brick.display.text(constantIntegration,(120,40))
    brick.display.text("3:Differential",(0,50))
    brick.display.text(constantdifferential,(120,50))
    brick.display.text("",(0,60))
    

ev3 = EV3Brick()
ColorSensor = ColorSensor(Port.S2)
timer = StopWatch()
seconds = timer.time()/1000
timesNow = 1

# 値の新旧データ[旧、新]
deviationVal = [0,0]

# Initialize two motors and a drive base
left = Motor(Port.B)
right = Motor(Port.C)
robot = DriveBase(left, right, 100, 143)

# 時間偏差
timePeriod = 0.2 

# 内部タイマを確認するたイミンぐ
settingTime = timePeriod

# 制御定数
constantIntegration = 0.1
constantdifferential = 0.8
constantProportional = 5

display ()

loop = 0
item = 0
cnt1 = 70
cnt2 = 0
while True :
    brick.display.text(item,(0,cnt1))
    if Button.LEFT in brick.buttons() :
        cnt1+=10
        if item==0 :
            item += 3
            brick.display.text(item,(0,cnt1))
        elif item >0 :
            item -= 1
            brick.display.text(item,(0,cnt1))
        time.sleep(0.2)
    elif Button.RIGHT in brick.buttons() :
        cnt1+=10
        if item == 3 :
            item -= 3
            brick.display.text(item,(0,cnt1))
        elif item <3 :
            item += 1
            brick.display.text(item,(0,cnt1))
        time.sleep(0.2)
    elif Button.CENTER in brick.buttons() :
        cnt1 = 70
        time.sleep(0.2)

        if(item==0) :
            brick.display.clear()
            brick.display.text("[TimePeriod]",(0,20))
            brick.display.text("",(0,30))
            brick.display.text("TimePeriod=",(0,40))
            brick.display.text(timePeriod,(120,40))
            loop=0
            cnt2=50
            while loop==0 :
                if Button.UP in brick.buttons():
                    timePeriod += 0.1 
                    brick.display.text("TimePeriod=",(0,cnt2))
                    brick.display.text(timePeriod,(120,cnt2))
                    time.sleep(0.2)
                    cnt2+=10
                elif Button.DOWN in brick.buttons():
                    timePeriod -= 0.1
                    brick.display.text("TimePeriod=",(0,cnt2))
                    brick.display.text(timePeriod,(120,cnt2))
                    time.sleep(0.2)
                    cnt2+=10
                elif Button.CENTER in brick.buttons():
                    while loop==0 :
                        brick.display.clear()
                        brick.display.text("Set Value!",(0,20))
                        time.sleep(0.2)
                        if Button.CENTER in brick.buttons():
                            brick.display.clear()
                            display ()
                            loop=1
                            time.sleep(0.2)
        elif(item==1) :
            brick.display.clear()
            brick.display.text("[Proportion]",(0,20))
            brick.display.text("",(0,30))
            brick.display.text("Proportion=",(0,40))
            brick.display.text(constantProportional,(120,40))
            loop=0
            cnt2=50
            while loop==0 :
                if Button.UP in brick.buttons():
                    constantProportional += 0.1 
                    brick.display.text("Proportion=",(0,cnt2))
                    brick.display.text(constantProportional,(120,cnt2))
                    time.sleep(0.2)
                    cnt2+=10
                elif Button.DOWN in brick.buttons():
                    constantProportional -= 0.1
                    brick.display.text("Proportion=",(0,cnt2))
                    brick.display.text(constantProportional,(120,cnt2))
                    time.sleep(0.2)
                    cnt2+=10
                elif Button.CENTER in brick.buttons():
                    while loop==0 :
                        brick.display.clear()
                        brick.display.text("Set Value!",(0,20))
                        time.sleep(0.2)
                        if Button.CENTER in brick.buttons():
                            brick.display.clear()
                            display ()
                            loop=1
                            time.sleep(0.2)
        elif(item==2) :
            brick.display.clear()
            brick.display.text("[Integral]",(0,20))
            brick.display.text("",(0,30))
            brick.display.text("Integral=",(0,40))
            brick.display.text(constantIntegration,(120,40))
            loop=0
            cnt2=50
            while loop==0 :
                if Button.UP in brick.buttons():
                    constantIntegration += 0.1 
                    brick.display.text("Integral=",(0,cnt2))
                    brick.display.text(constantIntegration,(120,cnt2))
                    time.sleep(0.2)
                    cnt2+=10
                elif Button.DOWN in brick.buttons():
                    constantIntegration -= 0.1
                    brick.display.text("Integral=",(0,cnt2))
                    brick.display.text(constantIntegration,(120,cnt2))
                    time.sleep(0.2)
                    cnt2+=10
                elif Button.CENTER in brick.buttons():
                    while loop==0 :
                        brick.display.clear()
                        brick.display.text("Set Value!",(0,20))
                        time.sleep(0.2)
                        if Button.CENTER in brick.buttons():
                            brick.display.clear()
                            display ()
                            loop=1
                            time.sleep(0.2)
        else :
            brick.display.clear()
            brick.display.text("[Differential]",(0,20))
            brick.display.text("",(0,30))
            brick.display.text("Differential=",(0,40))
            brick.display.text(constantdifferential,(120,40))
            loop=0
            cnt2=50
            while loop==0 :
                if Button.UP in brick.buttons():
                    constantdifferential += 0.1 
                    brick.display.text("Differential=",(0,cnt2))
                    brick.display.text(constantdifferential,(120,cnt2))
                    time.sleep(0.2)
                    cnt2+=10
                elif Button.DOWN in brick.buttons():
                    constantdifferential -= 0.1
                    brick.display.text("Differential=",(0,cnt2))
                    brick.display.text(constantdifferential,(120,cnt2))
                    time.sleep(0.2)
                    cnt2+=10
                elif Button.CENTER in brick.buttons():
                    while loop==0 :
                        brick.display.clear()
                        brick.display.text("Set Value!",(0,20))
                        time.sleep(0.2)
                        if Button.CENTER in brick.buttons():
                            brick.display.clear()
                            display ()
                            loop=1
                            time.sleep(0.2)
        item = 0
    # 1秒1000ステップ
    seconds = timer.time()/1000

    if seconds > timesNow :

        deviationVal[timesNow % 2] = ColorSensor.reflection ()

        # 液晶出力
        # brick.display.text(seconds)

        # beforVal = ColorSensor.reflection ()
        timesNow = timesNow+1
        settingTime = settingTime + timePeriod
    # 偏差見る
    proportional = (ColorSensor.reflection () - 30 )
    # 傾き見る
    differential = (deviationVal[0] - deviationVal[1])/ timePeriod
    # 積分する
    integration = (deviationVal[0] + deviationVal[1]) * timePeriod / 2

    opv = proportional * constantProportional + differential * constantdifferential + integration * constantIntegration
    robot.drive(180, opv)

    # brick.display.text(ColorSensor.reflection ())
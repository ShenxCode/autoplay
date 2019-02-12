#!/usr/bin/pyhton3
#-*- coding:utf-8 -*-


"""
    目的：
        实现制作脚本简单化
        如果失控了，需要中断PyAutoGUI函数，就把鼠标光标在屏幕左上角。
"""
import os
import time
import random
import numpy
import image
import pyautogui
from op import *

DEBUG = False
bulefont='\033[34;1m'
fontend='\033[0m'
redfont="\033[1;31m"

def log(text,show=0):
    def decorator(func):
        def wrapper(*args, **kw):
            if show:
                for x in args:
                    for j in kw :
                        print('%s[%s]%s[%s] %s(%s,%s)' % (bulefont,text,fontend,time.asctime( time.localtime(time.time()) ), func.__name__,x,j))
            elif show==0:
                print('%s[%s]%s[%s] %s' % (bulefont, text, fontend, time.asctime(time.localtime(time.time())), func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator




def hunshi():

    tiaozhan=PartOfTheScreen("挑战","tmp/挑战.bmp",20)
    shengli = PartOfTheScreen("胜利", "tmp/胜利.bmp", 50)
    shengli2=PartOfTheScreen("胜利2","tmp/胜利2.bmp",50)
    while True:
        # dm.MoveWindow(hwnd, 10, 10)
        # a=dm.GetWindowRect(hwnd)
        # print(a)
        tiaozhan.tap(1)
        shengli.tap(1)
        shengli2.tap(1)

        # tap(tiaozhan.x,tiaozhan.y,clicks=3,xOffset=20,yOffset=20,delay3=0.2)
        time.sleep(2)
@log("开始副本")
def fuben():
    ##############
    #状态标志设置区
    manji=0

    #############
    ############
    # 设置图片区
    zhaoguai=PartOfTheScreen("找怪中","tmp/找怪中.bmp",10)
    tansuo=PartOfTheScreen("探索","tmp/探索.bmp",40)
    zhang =PartOfTheScreen("二十五章","tmp/二十五章.bmp",10)
    shengli = PartOfTheScreen("胜利", "tmp/胜利.bmp", 50)
    shengli2 = PartOfTheScreen("胜利2", "tmp/胜利2.bmp", 50)
    guai = PartOfTheScreen("小怪", "tmp/小怪.bmp", 5)
    boss = PartOfTheScreen("boss", "tmp/boss.bmp", 5)
    zhunben = PartOfTheScreen("准备", "tmp/准备.bmp", 30)
    zhiren = PartOfTheScreen("纸人", "tmp/纸人.bmp", 5)
    dangtian=PartOfTheScreen("当天不用提醒", "tmp/当天不用提醒.bmp", 3)
    quxiao = PartOfTheScreen("取消", "tmp/取消.bmp", 10)
    kuang= PartOfTheScreen("奖励框", "tmp/奖励框.bmp", 10)
    find_manji=PartOfTheScreen("狗粮满级1","tmp/满级.bmp",5)
    find_manji2 = PartOfTheScreen("狗粮满级2", "tmp/满级2.bmp", 5)
    all = PartOfTheScreen("全部", "tmp/全部.bmp", 5)
    nka= PartOfTheScreen("N卡", "tmp/N.bmp", 5)
    ji = PartOfTheScreen("1级", "tmp/级1.bmp", 5)
    ###############
    while True:
        if find_manji.get_centerxy(1): manji=1
        if find_manji2.tap(1): manji=1
        dangtian.tap(1)
        quxiao.tap(1)
        tansuo.tap(1)
        zhang.tap(1)
        shengli2.tap(1)
        # shengli.tap(1)
        boss.tap(1)
        guai.tap(1)
        zhiren.tap(1)
        kuang.tap(1)
        if zhaoguai.tap(guai.get_centerxy(1) == 0 ):time.sleep(1.5)
        zhunben.tap(manji==0)
        ji.swipe(1,155,316)
        ji.swipe(1, 655, 342)
        nka.tap(manji)
        all.tap(manji)
        # time.sleep(2)

@log("开始读取配置文件")
def readini():
    CMD={}
    while True:
        with open("cmd.txt", "r", encoding="utf-8") as fp:
            lines = [x for x in fp.readlines() if x.split(" ")[0] != "#"]
        fp.close()
        for tmp in lines :
            CMD_list=tmp.split(" ")
            CMD[CMD_list[0]]=PartOfTheScreen(CMD_list[0], "tmp/"+CMD_list[0]+".bmp", int(CMD_list[2]))
            if CMD_list[1]=="点击":
                if CMD_list[3].split(":")[0] == "{始终":
                    CMD[CMD_list[0]].tap(1)
                elif CMD_list[3].split(":")[0]=="{未发现":
                    CMD[CMD_list[0]].tap(CMD[CMD_list[3].split(":")[1].split("}")[0]].get_centerxy(1)==0)
                elif CMD_list[3].split(":")[0]=="{发现":
                    CMD[CMD_list[0]].tap(CMD[CMD_list[3].split(":")[1].split("}")[0]].get_centerxy(1)==1)

                if CMD_list[4].split(":")[0]=="{延时":
                    time.sleep(int(CMD_list[4].split(":")[1].split("}")[0]))
def main():
    # print(scereen)
    fuben()
if __name__== '__main__':
    # pyautogui.alert('开始吧')
    readini()
    # main()
    # dm.SetWindowState(hwnd, 8)
    # dm.SetWindowState(hwnd, 1)
    # dm.MoveWindow(hwnd, 0, 0)
    # print(dm.BindWindow(hwnd, "normal", "dx2", "normal", 0))
    # print(a)
    # main()


def test():

    a=PartOfTheScreen("file","tmp/file.bmp")
    start =time.clock()
    # x,y=pyautogui.locateCenterOnScreen("tmp/file.bmp",grayscale=True)
    # x=dm.FindPic(0, 0, 2000, 2000, "tmp/file.bmp", "000000", 0.9, 0)
    a.get_centerxy(1)
    end =time.clock()
    print("找图花费%sS"%(end-start),a.x,a.y)
    # pyautogui.screenshot("hello.bmp")
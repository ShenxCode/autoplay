#-*- coding:utf-8 -*-



import time

from ini import *


def huan_gouliang():
    log.info("开始换狗粮")
    MAX_levl=''
    while True:
        huan_over= yield MAX_levl
        if not huan_over:
            return
        #换狗粮操作
        print("开始换狗粮")
        # time.sleep(5)
        MAX_levl='ok!'

def hunshi(n,c):
    log.info("开始挑战魂十")
    
    # t1=threading.Thread(target=tiaozhan.tap,name=tiaozhan,kwargs={'condition':1})
    c.send(None)
    while n>=1:
        # change=1
        if 920<n<=930:
                yeyuanhuo.tap(1)
                # change=0
                n=920

        shibai.tap(1)
        tiaozhan.tap(1)
        shengli1.tap(1)

        if liaotian.tap(1):time.sleep(0.3)
        if shenle.tap(1):time.sleep(0.3)
        if yuhun.tap(1):time.sleep(0.3)
        if dashe.tap(1):time.sleep(0.3)
        # diban.tap(1)
        # if diban2.tap(1):time.sleep(0.3)
        if diban3.tap(1):time.sleep(0.3)
        if boyuanya1.tap(1):time.sleep(0.3)
        if boyuanya2.tap(1):time.sleep(0.3)
        # if boyuanya3.tap(1):time.sleep(0.3)
        if jujue.tap(1):time.sleep(0.3)
        
        if shengli2.tap(1):n=n-1
        # if gouliang.get_centerxy(1):
        #     huan_over=c.send(1)
        #     print("换狗粮%s"%huan_over)
        time.sleep(2)


def juqing():
    log.info("开始剧情")
    while True:
        shibai.tap(1)
        shengli1.tap(1)
        shengli2.tap(1)
        juqing_rukou.tap(1)
        juqing_skip.tap(1)
        juqing_skip2.tap(1)
        xiaoguai.tap(1)
        zhubei.tap(1)
        time.sleep(2)
def fuben(n):
    log.info("开始探索副本")
    while n>=0:
        if tansuo.tap(1):
            n-=1
            time.sleep(2)
        zhang28.tap(1)
        shibai.tap(1)
        shengli1.tap(1)
        shengli2.tap(1)
        xiaoguai.tap(1)
        zhubei.tap(1)
        boss.tap(1)
        zhiren.tap(1)
        jiangli.tap(1)
        jujue.tap(1)
        time.sleep(2)
if __name__ == "__main__":
    hunshi(1000,huan_gouliang())
#     fuben(100)

    # logging.info("挑战魂十结束")

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
        zhunbei.tap(1)
        time.sleep(2)
def fuben(n):
    log.info("开始探索副本")
    flag_tansuing=0
    flag_no_swipe=1
    flag_findbox=0
    move_count=0
    move2_count=0
    manji_flag=0
    huan_status=0
    while n>=0:
        if baoxiang.get_centerxy(1) or baoxiang2.get_centerxy(1):
            flag_findbox=1
        if flag_findbox==1:
            if baoxiang2.tap(1):
                flag_findbox=0
            close_tansuo.tap(1)
        if tansuo.tap(flag_findbox==0):
            n-=1
            flag_tansuing=1
            move_count = 0
            move2_count = 0
            time.sleep(2)
        if zhang28.tap(flag_findbox==0):
            flag_tansuing = 1
        kunnan.tap(1)
        shibai.tap(1)
        shengli1.tap(1)
        shengli2.tap(1)
        if zhiren.tap(1):
            flag_no_swipe = 1
            move_count = 0
            move2_count = 0
        elif zhiren2.tap(1):
            flag_no_swipe = 1
            move_count = 0
            move2_count = 0
        if boss.tap(1):
            flag_tansuing=0
            flag_no_swipe = 1
            move_count = 0
            move2_count = 0
        elif boss2.tap(1):
            flag_tansuing = 0
            flag_no_swipe = 1
            move_count = 0
            move2_count = 0
        elif boss3.tap(1):
            flag_tansuing = 0
            flag_no_swipe = 1
            move_count = 0
            move2_count = 0
        elif xiaoguai.tap(1):
            flag_no_swipe = 1
        elif xiaoguai2.tap(1):
            flag_no_swipe = 1
        elif xiaoguai3.tap(1):
            flag_no_swipe = 1
        elif xiaoguai4.tap(1):
            flag_no_swipe = 1


        elif jiangli.tap(1):
            flag_no_swipe = 1
        elif manji.get_centerxy(1):
            manji_flag=1
            flag_no_swipe = 1
        elif manji2.get_centerxy(1):
            manji_flag=1
            flag_no_swipe = 1
        else:
            flag_no_swipe = 0


        if manji_flag==0:

            zhunbei2.tap(1)
            zhunbei.tap(1)
            zhunbei3.tap(1)
        elif manji_flag==1:
            if qingmingtou.tap(1) or qingminglong2.tap(1):
                #or qingminglong.tap(1)
                huan_status=1
            if huan_status==1:
                if all_ka.longtap(1, 0.2):
                    huan_status=2
                elif n_ka_find.get_centerxy(1):
                # else :
                    huan_status=3
            elif huan_status==2:
                if n_ka.longtap(1,0.2):
                    huan_status=3
            elif huan_status==3:
                if gouliang_nka.get_centerxy(1)or gouliang_nka3.get_centerxy(1) or gouliang_nka4.get_centerxy(1) or  gouliang_nka5.get_centerxy(1) or  gouliang_nka2.get_centerxy(1):
                    huan_status = 4

                huakuai.get_centerxy(1)
                huakuai.swipe(1, huakuai.x + 40, huakuai.y)
                time.sleep(0.5)

            elif huan_status==4:
                if gouliang_nka.swipe(1, 220, 300)or gouliang_nka2.swipe(1, 220, 300)or gouliang_nka3.swipe(1, 220, 300)or gouliang_nka4.swipe(1, 220, 300)or gouliang_nka5.swipe(1, 220, 300):
                    time.sleep(1)
                    if gouliang_nka.swipe(1, 650, 350)or gouliang_nka2.swipe(1, 650, 350)or gouliang_nka3.swipe(1, 650, 350)or gouliang_nka4.swipe(1, 650, 350)or gouliang_nka5.swipe(1, 650, 350):
                        time.sleep(1)
                        huan_status=5


            elif huan_status==5:
                manji_flag = 0
                huan_status=0

            # time.sleep(2)
            # if huakuai.swipe(1,557,730):
            #     time.sleep(1)
            # if gouliang_nka.swipe(1,220,300):
            #     time.sleep(1)
            # if gouliang_nka.swipe(1, 650, 350):
            #     time.sleep(1)

            print("发现满级","status is ",huan_status)
            log.info("发现满级"+"status is "+str(huan_status))


        jujue.tap(1)
        close.tap(1)
        if flag_no_swipe == 0:
            if move_count<8:
                if move_.tap(1):
                    move_count+=1
                    flag_no_swipe = 1
                    time.sleep(1.5)
            elif move2_count<8 :
                if move_2.tap(1):
                    move2_count+=1
                    flag_no_swipe = 1
                    time.sleep(1.5)
            elif move_count>=8:
                move2_count=0
            elif  move2_count>=8:
                move_count =0
        time.sleep(0.5)

def over():
    #todo:收尾工作
    log.info("结束脚本")
    close_ld.tap(1)

    pass
if __name__ == "__main__":
    #hunshi(1000,huan_gouliang())
    fuben(1000)
    over()

    # logging.info("挑战魂十结束")

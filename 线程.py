#-*- coding:utf-8 -*-



from ini import *
import time
import threading

lock=threading.Lock()
#狗粮满级标志位
LEVL_MAX=0
def hunshi(n):
    # t1=threading.Thread(target=tiaozhan.tap,name=tiaozhan,kwargs={'condition':1})
    while n>=1 and LEVL_MAX==0:
        shibai.tap(1)
        tiaozhan.tap(1)
        shengli1.tap(1)
        if shengli2.tap(1):n=n-1
        time.sleep(2)

def huan_gouliang():
    LEVL_MAX=0
    pass
def see_gouliang_levl_max():
    lock.acquire()
    try:
        pass
    finally:
        lock.release()
if __name__ == "__main__":
    log.info("开始挑战魂十")
    T_hun=threading.Thread(target=hunshi,name=hunshi,kwargs={'n':10})
    T_gouliang=threading.Thread(target=see_gouliang_levl_max(),name=see_gouliang_levl_max)
    T_gouliang.start()
    T_hun.start()
    T_hun.join()
    T_gouliang.join()

    # logging.info("挑战魂十结束")
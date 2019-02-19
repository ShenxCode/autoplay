#-*- coding:utf-8 -*-
import op
from log import log


PHOTOPATH="photo/"
##########################################
#魂十
yuhun = op.PartOfTheScreen("挑战御魂", PHOTOPATH + "yuhun.bmp")
dashe = op.PartOfTheScreen("挑战大蛇", PHOTOPATH + "dashe.bmp", 70)
yeyuanhuo=op.PartOfTheScreen("挑战业原火", PHOTOPATH + "yeyuanhuo.bmp")

tiaozhan = op.PartOfTheScreen("挑战图片", PHOTOPATH + "tiaozhan.bmp")
gouliang= op.PartOfTheScreen("狗粮满级图片", PHOTOPATH + "gouliang.bmp")
# diban = op.PartOfTheScreen("魂十地板", PHOTOPATH + "杂项_diban.bmp", 100)
# diban2 = op.PartOfTheScreen("魂十地板", PHOTOPATH + "diban2.bmp", 70)
diban3 = op.PartOfTheScreen("魂十地板", PHOTOPATH + "diban3.bmp", 70)
boyuanya1= op.PartOfTheScreen("源博雅", PHOTOPATH + "yuanboya1.bmp", 100)
boyuanya2= op.PartOfTheScreen("源博雅", PHOTOPATH + "yuanboya2.bmp", 100)
# boyuanya3= op.PartOfTheScreen("源博雅", PHOTOPATH + "yuanboya3.bmp", 100)

liaotian=op.PartOfTheScreen("聊天", PHOTOPATH + "liaotian.bmp")

#############################################
#公共
shengli1 = op.PartOfTheScreen("胜利图片1", PHOTOPATH + "shengli1.bmp")
shengli2 = op.PartOfTheScreen("胜利图片2", PHOTOPATH + "shengli2.bmp")
shibai=op.PartOfTheScreen("失败图片", PHOTOPATH + "shibai.bmp")
xiaoguai=op.PartOfTheScreen("小怪", PHOTOPATH + "xiaoguai.bmp", 10)
zhubei=op.PartOfTheScreen("准备", PHOTOPATH + "zhunbei.bmp")
shenle=op.PartOfTheScreen("神乐", PHOTOPATH + "shenle.bmp")

#######################
#todo:New!!
close=op.PartOfTheScreen("关闭", PHOTOPATH + "close.bmp")
back=op.PartOfTheScreen("返回", PHOTOPATH + "back.bmp")
tilibuzu=op.PartOfTheScreen("体力不足", PHOTOPATH + "tilibuzu.bmp")


#########################################
#剧情
# juqing_rukou=op.PartOfTheScreen("剧情入口", PHOTOPATH + "剧情入口2.bmp", 10)
juqing_rukou=op.PartOfTheScreen("剧情入口", PHOTOPATH + "juqingrukou.bmp", 10)
juqing_skip=op.PartOfTheScreen("跳过", PHOTOPATH + "tiaoguo.bmp", 10)
juqing_skip2=op.PartOfTheScreen("快进", PHOTOPATH + "kuaijin.bmp", 10)
######################################
#探索
zhang28=op.PartOfTheScreen("二十八章", PHOTOPATH + "zhang28.bmp", 20)
tansuo=op.PartOfTheScreen("探索", PHOTOPATH + "tansuo.bmp", 20)
boss=op.PartOfTheScreen("boss", PHOTOPATH + "boss.bmp", 10)
zhiren=op.PartOfTheScreen("小纸人", PHOTOPATH + "zhiren.bmp", 10)
jiangli=op.PartOfTheScreen("奖励", PHOTOPATH + "jiangli.bmp", 10)

jujue=op.PartOfTheScreen("协作拒绝", PHOTOPATH + "jujue.bmp", 10)
jieshou=op.PartOfTheScreen("协作接受", PHOTOPATH + "jieshou.bmp", 10)











log.info("图片初始化完成")


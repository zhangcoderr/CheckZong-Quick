# coding=utf-8
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import time
import pyHook
import pythoncom
import  pyperclip
from pynput import mouse,keyboard
import re


def copy():
    k.press_key(k.control_l_key)
    k.tap_key("c")  # 改小写！！！！ 大写的话由于单进程会触发shift键 ctrl键就失效了
    k.release_key(k.control_l_key)


def getCopy(maxTime=1.2):
    # maxTime = 3  # 3秒复制 调用copy() 不管结果对错
    while (maxTime > 0):
        maxTime = maxTime - 0.3
        time.sleep(0.3)
        # print('doing')
        copy()

    result = pyperclip.paste()
    return result


def tapkey(key, count=1, waitTime=0.2):
    for i in range(0, count):
        k.tap_key(key)
        time.sleep(waitTime)
def copy():

    k.press_key(k.control_l_key)
    k.tap_key("c")
    k.release_key(k.control_l_key)

def tapkey(key,count=1):
    for i in range(0,count):
        k.tap_key(key)
        time.sleep(0.05)





def onpressed(key):
    if(key==keyboard.Key.caps_lock):


        print('开始检测综合单价')

        zong = float(getCopy())
        tapkey(k.down_key)
        tapkey(k.escape_key)
        tapkey(k.right_key)
        tapkey(k.up_key)
        kong = float(getCopy())
        swimValue = abs((kong) - (zong)) / (kong)

        lowest = kong * 0.85

        lowest = kong * 0.85
        arg = 1
        if (lowest > 5000):
            arg = 20
        elif (lowest > 2000):
            arg = 15
        elif (lowest > 1000):
            arg = 10
        elif (lowest > 500):
            arg = 5
        elif (lowest > 100):
            arg = 2
        elif (lowest > 10):
            arg = 0.5
        elif (lowest > 0):
            arg = 0.2
        else:
            print('负数')

        condition1 = zong <= lowest - 0.05  # 误差0.05不处理
        condition2 = zong > lowest + arg + 0.05  # 误差0.05不处理

        # for lowest


        if (condition2 or condition1):
            # print(swimValue)
            # print(zong)
            # print(kong)
            tapkey(k.escape_key)
            tapkey(k.left_key)
            tapkey(k.down_key, 2)

            nowValue = float(getCopy())
            value = ''


            if (nowValue == kong):
                print('空空空')
                # print(projectCharactor)
                if (zong > lowest):
                    print('无主材价，综合>控制,减不动')
                else:
                    value = float(abs((lowest) - (zong))) + arg
                    # print(value)
            else:

                if (zong > lowest + arg):  # TODDODODODODODO
                    minus = (zong - lowest - arg)
                    if (minus > 0):
                        # value=nowValue-minus/1.15#TODDODODODODODO
                        value = nowValue - minus

                    else:
                        print('材料价太少，少到最低价都不够减')
                else:
                    if (zong < lowest):
                        add = lowest + arg - zong
                        # value = nowValue +add / 1.15#TODDODODODODODO
                        value = nowValue + add

                    else:
                        print('满足条件')
            # 比最低价高一点 end


            if (value == ''):
                print('不处理')
                tapkey(k.escape_key)
                tapkey(k.left_key, 4)
                tapkey(k.down_key, 2)
            else:
                # if(value>80):
                # value=int(value)  #不取整了
                k.type_string(str(value))
                print(value)
                tapkey(k.enter_key)

                time.sleep(2)

                # 工程量系数 1.03 1.01
                tapkey(k.escape_key)
                tapkey(k.right_key, 6)
                tapkey(k.up_key, 3)
                changed_zong = float(getCopy())

                # temppppppppppppppppppppppppppppppppppppppp
                minus_zong = changed_zong - zong  # 合价
                if (nowValue == kong):
                    minus_value = value - 0
                else:
                    minus_value = value - nowValue
                changed_arg = minus_zong / minus_value
                print(changed_arg)
                changed_value = value
                if (changed_arg != 1 and changed_arg != 0):

                    if (nowValue == kong):
                        print('空空空22')
                        # print(projectCharactor)
                        if (zong > lowest):
                            print('无主材价，综合>控制,减不动22')
                        else:
                            changed_value = (float(abs((lowest) - (zong))) + arg) / changed_arg



                            # print(value)
                    else:

                        if (zong > lowest + arg):  # TODDODODODODODO
                            minus = (zong - lowest) - arg
                            if (minus > 0):
                                # value=nowValue-minus/1.15#TODDODODODODODO
                                changed_value = nowValue - minus / changed_arg

                            else:
                                print('材料价太少，少到最低价都不够减22')
                        else:
                            if (zong < lowest):
                                add = lowest + arg - zong
                                # value = nowValue +add / 1.15#TODDODODODODODO
                                changed_value = nowValue + add / changed_arg

                            else:
                                print('满足条件22')
                    # temp end

                    if (changed_value < 0):
                        print('负数 价格 wrong index::' + str(index_count))
                        print('负数 价格::' + str(changed_value))

                        changed_value = 0

                    tapkey(k.down_key, 2)
                    k.type_string(str(changed_value))
                    # print(changed_arg)
                    print('改系数')
                    print(changed_value)
                    tapkey(k.enter_key)
                    time.sleep(2)

                # 工程量系数 1.03 1.01  end
                else:
                    tapkey(k.down_key, 2)
                    tapkey(k.enter_key)

                # 下一个
                tapkey(k.escape_key)
                tapkey(k.right_key, 2)
                tapkey(k.down_key)

        else:
            print('满足条件，不处理')
            tapkey(k.escape_key)
            tapkey(k.left_key, 5)
            tapkey(k.down_key, 4)

k=PyKeyboard()
m=PyMouse()

print('start')
with keyboard.Listener(on_press=onpressed) as listener:
    listener.join()

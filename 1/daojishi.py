import time

def countdown(seconds):
    """
    倒计时程序
    :param seconds: 倒计时的秒数
    """
    while seconds > 0:
        print("倒计时：", seconds, "秒")
        time.sleep(1)
        seconds -= 1
    print("倒计时结束！")

# 调用倒计时函数，传入需要倒计时的秒数
countdown(10)

#
import threading
import time


def Sing():
    while True:
        print("我在唱歌,啦啦啦啦啦")
        time.sleep(1)


def Dance():
    while True:
        print("我在跳舞,哒哒哒哒哒")
        time.sleep(1)


def Sing2(msg):
    while True:
        print(msg)
        time.sleep(1)


def Dance2(msg):
    while True:
        print(msg)
        time.sleep(1)


if __name__ == '__main__':
    # Sing()
    # Dance()

    # sing_thread = threading.Thread(target=Sing())
    # dance_thread = threading.Thread(target=Dance())
    # 注意此时是没有()括号的 否则还是单线程
    # sing_thread = threading.Thread(target=Sing)
    # dance_thread = threading.Thread(target=Dance)

    # args通过 元组的形式传参 记得要加逗号
    # kwargs通过字典的形式传参
    sing_thread = threading.Thread(target=Sing2, args=("小河流水哗啦啦",))
    dance_thread = threading.Thread(target=Dance2, kwargs={"msg": "读书好开心"})

    sing_thread.start()
    dance_thread.start()

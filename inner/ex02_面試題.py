"""
创建2个分支线程,一个打印 1--52 这个数字
一个打印 A--Z这26个字母,两个分支线程启动后
要求打印出来的顺序是 12A34B...5152Z
"""
from threading import Thread, Lock, Event
from time import sleep

lock = Lock()


def text():
    for i in range(1, 27):
        lock.acquire()
        alph = chr(i + 64)
        print(f"{alph}", end="")
        lock.release()
        sleep(0.1)


def num():
    for i in range(1, 53, 2):
        lock.acquire()
        print(f"{i}{i + 1}", end="")
        lock.release()
        sleep(0.1)


t1 = Thread(target=num)
t1.start()
sleep(0.01)
t2 = Thread(target=text)
t2.start()

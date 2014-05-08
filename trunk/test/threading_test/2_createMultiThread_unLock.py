#-*- coding:utf-8 -*-

"""
    执行测试：
        两个类定义的两个线程， 并且不适用锁机制， 所以是各自执行的。
"""
import threading
import time

class Test1(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global count, mutext
        threadname = threading.currentThread().getName()
        for x in xrange(0, 5):
            #mutext.acquire()
            count = count + 1
            #mutext.release()
            print threadname, x, count
            print '----------------------, ', '11111111111111'
            time.sleep(1)

class Test2(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global count, mutext
        threadname = threading.currentThread().getName()
        for x in xrange(0, 5):
            #mutext.acquire()
            count = count + 1
            #mutext.release()
            print threadname, x, count
            print '----------------------, ', '22222222222222222222'
            time.sleep(2)

if __name__ == '__main__':
    global count, mutext
    count = 0
    mutext = threading.Lock()
    test1 = Test1()
    test2 = Test2()
    test1.start()
    test2.start()
    test1.join()
    test2.join()


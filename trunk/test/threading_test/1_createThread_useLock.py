#-*- coding:utf-8 -*-

"""
    执行测试:
        启动4个线程， 用类的方式。  
        这种事带锁的线程， 效果就是， 一个一个的执行， 很有顺序
"""
import threading
import time

class Test(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self._run_num = num
    def run(self):
        global count, mutext
        threadname = threading.currentThread().getName()
        
        for x in xrange(0, int(self._run_num)):
            mutext.acquire()
            count = count + 1
            mutext.release()
            print threadname, x, count
            print '----------------------, ', '11111111111111'
            time.sleep(1)

if __name__ == '__main__':
    global count, mutext
    threads = []
    count = 1
    # Create lock
    mutext = threading.Lock()
    # 创建线程对象
    for x in xrange(0, 4):
        threads.append(Test(10))
    # 启动线程
    for t in threads:
        t.start()
    # 等待子线程结束
    for t in threads:
        t.join()


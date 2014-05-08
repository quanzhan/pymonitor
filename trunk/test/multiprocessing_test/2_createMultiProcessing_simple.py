#!/usr/bin/env python

""" A basic fork in action """

from multiprocessing import Process
import os
import time

def myprocess1():

    print 'starting child process with pid: ', os.getpid()
    print 'Parent process: ', os.getppid()
    print '---------------------------------------1'

    global count
    for i in range(10):
        count += 1
        print 'pid = %s, count= %s' % (str(os.getpid()), str(count))
        time.sleep(1)
    print 'process %s Done' % str(os.getpid())

def myprocess2():
    print 'starting child process with pid: ', os.getpid()
    print 'Parent process: ', os.getppid()
    print '---------------------------------------2'

    global count
    for i in range(10):
        count += 1
        print 'pid = %s, count= %s' % (str(os.getpid()), str(count))
        time.sleep(3)
    print 'process %s Done' % str(os.getpid())


if __name__ == "__main__":
    global count
    count = 0
    p = Process(target=myprocess1, args=())
    p.start()
    p = Process(target=myprocess2, args=())
    p.start()
    p.join()

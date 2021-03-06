
import multiprocessing
import time

def func(msg):
    for i in xrange(3):
        print msg
        print 'xrange i = ', i
        time.sleep(1)
    return "done " + msg

if __name__ == "__main__":
    pool = multiprocessing.Pool(processes=4)
    result = []
    for i in xrange(10):
        msg = "Process %d" %(i)
        result.append(pool.apply_async(func, (msg, )))
    pool.close()
    pool.join()
    for res in result:
        print res.get()
    print "Sub-process(es) done."

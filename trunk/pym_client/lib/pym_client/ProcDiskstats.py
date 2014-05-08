#!/usr/bin/env python
#-*- coding:utf-8 -*-

""" pymonitor client module: 获取IO数据， 从/proc/diststats 文件 """
""" @Author: xcluo.mr@gmail.com
    @Site: www.pythoner.cn
    @Date: 2013-04-09
    @Version: v0.2
    @Note:
        需要一个缓冲文件 /tmp/last_diskstats 来保存上一次的数据(是一个带时间戳的数据)
        本次计算的时候， 用本次数据和上一次数据做减法的值,与两个时间戳的减法的值 做除法求得最终结果 

        /proc/disktats 中单行数据的解释：

[root@thinkpad ~]# cat /proc/diskstats | grep sda\ 
   8       0 sda 3479 5666 288738 199185 496 957 11624 11944 0 19732 211125
第1个域：读磁盘的次数，成功完成读的总次数；
第2个域：合并读次数；
第3个域：读扇区的次数，成功读过的扇区总次数；
第4个域：读花费的毫秒数，这是所有读操作所花费的毫秒数；//基准
第5个域：写完成的次数，成功写完成的总次数；
第6个域：合并写次数，为了效率可能会合并相邻的读和写。从而两次4K的读在它最终被处理到磁盘上之前可能会变成一次8K的读，才被计数（和排队），因此只有一次I/O操作，这个域使你知道这样的操作有多频繁；
第7个域：写扇区的次数，成功写扇区总次数；
第8个域：写花费的毫秒数，这是所有写操作所花费的毫秒数；//基准
第9个域：I/O的当前进度，只有这个域应该是0。当请求被交给适当的request_queue_t时增加和请求完成时减小；
第10个域：花在I/O操作上的毫秒数，这个域会增长只要field 9不为0；
第11个域：加权，花在I/O操作上的毫秒数，在每次I/O开始，I/O结束，I/O合并时这个域都会增加。这可以给I/O完成时间和存储那些可以累积的提供一个便利的测量标准。
        
"""

import re
import time
import simplejson as json
import pyssh

def get_ProcDiskstats(devices):
    """ 获取IO监控数据
        @Params: devices = LIST # 物理硬盘的设备名, 例如 devices=['sda', 'sdb', 'hda', 'scisi']
        @Return: (status, msgs, results)
                status = INT, Fuction execution status, 0 is normal, other is failure.
		msgs = STRING, If status equal to 0, msgs is '', otherwise will be filled with error message.
                results = DICT {
                        'sda': { # 设备sda的读写能力
                            'reading': 50032, # 单位都是  KB/s
                            'writing': 20,
                        },
                        'sdb': {
                            'reading': 50032, # 单位都是  KB/s
                            'writing': 20,
                        }
                    }

        @Note: 
            获取数据的效果， 和 #vmstat -n 1 一致
    """

    status=0; msgs=''; results='';
    if devices == []:
        return (-1, 'Error: Params is None.', '')
        

    now_data = {} # 当前 /proc/diskstats  的值
    last_data = {} # 上一次 /proc/diskstats  的值, 时间跨度由调用程序决定

    # 获取当前数据
    cmd = "cat /proc/diskstats | egrep '%s'"  % (len(devices)==1 and devices[0]+' ' or ' |'.join(devices)+' ')  # 只获取到物理硬盘的数据
    (status, msgs, results) = pyssh.getcmd(cmd=cmd)
    if status == 0:
        now_data['timestamp'] = time.time()
        temps = results.split('\n')
        for temp in temps:
            tmp = re.split('[ ]+', temp)
            now_data[tmp[3]] = {
                    'number_of_issued_reads':tmp[4], # Field 1  
                    'number_of_reads_merged':tmp[5], # Field 2
                    'number_of_sectors_read':tmp[6], # Field 3
                    'number_of_milliseconds_spent_reading':tmp[7],    # Field 4    
                    'number_of_writes_completed':tmp[8],      # Field 5
                    'number_of_writes_merged':tmp[9],         # Field 6
                    'number_of_sectors_written':tmp[10],       # Field 7
                    'number_of_milliseconds_spent_writing':tmp[11],    # Field 8
                    'number_of_IOs_currently_in_progress':tmp[12],    # Field 9
                    'number_of_milliseconds_spent_doing_IOs':tmp[13],    # Field 10
                    'number_of_milliseconds_spent_doing_IOs_2':tmp[13],    # Field 11
                }
    else:
        return (status, msgs, 'Error: Can not get data from file /proc/diskstats.')

    # 获取历史数据
    (status, msgs, results) = pyssh.getcmd(cmd='cat /tmp/proc_diskstats')
    if status == 0 and results!= '':
        last_data = json.loads("%s" % results.strip())
    else:
        status = 0; msgs = ''; results = {}
        last_data = now_data

    # 保存当前数据到历史数据表中
    #cmd = """echo \"%s\" > /tmp/proc_diskstats""" % json.dumps(now_data)
    #(status, msgs, results) = pyssh.getcmd(cmd=cmd)
    fp = file('/tmp/proc_diskstats', 'w')
    fp.write(json.dumps(now_data))
    fp.close()

    # 处理两个数据，得到要计算的值
    results = {}
    timecut = float(now_data['timestamp']) - float(last_data['timestamp'])
    if timecut > 0:
        for key in devices:
            reading = (int(now_data[key]['number_of_sectors_read']) - int(last_data[key]['number_of_sectors_read']))/2/timecut
            writing = (int(now_data[key]['number_of_sectors_written']) - int(last_data[key]['number_of_sectors_written']))/2/timecut
            results[key] = {'reading':int(reading), 'writing':int(writing)}
    else:
        # 第一次加载的时候，历史数据为空, 无法计算，所以初始化为0
        for key in devices:
            results[key] = {'reading':0, 'writing':0}

    return (status, msgs, results)


if __name__ == "__main__":
    # 用于测试
    while True:
        print get_ProcDiskstats(devices=['sda',])
        print get_ProcDiskstats(devices=['sda','sda1','sdc'])
        time.sleep(1)


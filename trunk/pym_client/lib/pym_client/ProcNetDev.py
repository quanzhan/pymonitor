#!/usr/bin/env python
#-*- coding:utf-8 -*-

""" pymonitor client module: 获取网络数据，从/proc/net/dev 文件 """
""" @Author: jlli@csvt.net
    @Site: www.pythoner.cn
    @Date: 2013-04-10
    @Version: v0.2
    @Note:
        需要一个缓存文件 /tmp/proc_net_dev 来保存上一次的数据（是一个带时间戳的数据）
        本次计算的时候，用本次数据和上一次数据做减法的值,与两个时间戳的减法的值做除法求得最终结果(kb/s)
        /proc/net/dev 中数据的解释：
    [root@hpcstack ~]# cat /proc/net/dev
Inter-|   Receive                                                |  Transmit
 face |bytes    packets errs drop fifo frame compressed multicast|bytes    packets errs drop fifo colls carrier compressed
    lo:664087762 3663780    0    0    0     0          0         0 664087762 3663780    0    0    0     0       0          0
  eth0:  651822    6311    0    0    0     0          0         0   553421    6076    0    0    0     0       0          0
  eth1:  663326    6060    0    0    0     0          0         0   962066    4571    0    0    0     0       0          0
interface:网卡名
Receive(接受):
    第一个域(bytes)：字节数
    第二个域(packets)：包数
    第三个域(errs)：错误包数
    第四个域(drop)：丢弃包数
    第五个域(fifo)：(First in first out)包数/FIFO缓存错误数
    第六个域(frame)：帧数
    第七个域(compressed)：压缩(compressed)包数
    第八个域(multicast)：多播（multicast, 比如广播包或者组播包)包数
Transmit(发送):
    第一个域(bytes)：字节数
    第二个域(packets)：包数
    第三个域(errs)：错误包数
    第四个域(drop)：丢弃包数
    第五个域(fifo)：(First in first out)包数/FIFO缓存错误数
    第六个域(colls): 接口检测到的冲突数
    第七个域(carrier): 连接介质出现故障次数，如：网线接触不良
    第八个域(compressed)：压缩(compressed)包数

"""

import re
import time
import pyssh

import simplejson as json
#try:
#    import simplejson as json
#except:
#    import json

def get_ProcNetDev(devices, bandwidth):
    """获取网络监控数据
        @Params: devices = LIST # 物理网卡的设备名，例如 devices=['eth0', 'eth1', 'eth2', 'eth3']
                 bandwidth = DICT # 对应物理网卡的带宽,例如 bandwidth={'eth0':1000, 'eth1':10000})
        @Return: (status, msgs, results) 
            status = INT, Fuction execution status, 0 is normal , other is failure.
            msgs = STRING, If status equal to 0, msgs is '', otherwise will be filled with error message.
            results = DICE {
                    'eth0': { #网卡eth0的传输能力
                        'transmit': 1024, #单位无特殊说明都是 KB/s
                        'receive': 10240, 
                        'bandwidth':1000, #单位是 M/s
                    },
                    'eth1': { #网卡eth1的传输能力
                        'transmit': 1024, #单位无特殊说明都是 KB/s
                        'receive': 10240, 
                        'bandwidth':1000, #单位是 M/s
                    }
                }
        @Note:
    """

    status=0; msgs=''; results='';
    if devices == []:
        return (-1, 'Error: Params is None.', '')
    now_data = {} # 当前 /proc/net/dev 的值
    last_data = {} # 上一次 /proc/net/dev 的值，时间跨度由调用程序决定

    # 获取当前数据
    cmd = "cat /proc/net/dev | egrep '%s'"  % (len(devices)==1 and devices[0]+':' or ':|'.join(devices)+':') #获取物理网卡的数据
    (status, msgs, results) = pyssh.getcmd(cmd=cmd)
    if status == 0:
        now_data['timestamp'] = time.time()
        temps = results.split('\n')
        for temp in temps:
            tmp_main = temp.split(':')
            tmp=tmp_main[1].split()
            now_data[tmp_main[0].strip()] = {
                'receive_bytes': tmp[0],
                'receive_packets': tmp[1],
                'receive_errs': tmp[2],
                'receive_drop': tmp[3],
                'receive_fifo': tmp[4],
                'receive_frame': tmp[5],
                'receive_compressed': tmp[6],
                'receive_multicast': tmp[7],
                'transmit_bytes': tmp[8],
                'transmit_packets': tmp[9],
                'transmit_errs': tmp[10],
                'transmit_drop': tmp[11],
                'transmit_fifo': tmp[12],
                'transmit_colls': tmp[13],
                'transmit_carrier': tmp[14],
                'transmit_compressed': tmp[15]
            }
    else:
        return (status, msgs, 'Error: Can not get data from file /proc/net/dev.')
    
    # 获取历史数据
    (status, msgs, results) = pyssh.getcmd(cmd="cat /tmp/proc_net_dev")
    if status == 0:
        last_data = json.loads("%s" % results.strip())
    else:   # 第一次加载，没有历史数据的情况
        status=0; msgs = ''; results = {}
        last_data = now_data
    fp = file('/tmp/proc_net_dev', 'w')
    fp.write(json.dumps(now_data))
    fp.close()

    # 处理两个数据，得到要计算的值
    results = {}
    timecut = float(now_data['timestamp']) - float(last_data['timestamp'])
    if timecut > 0:
        for key in devices:
            receive = (int(now_data[key]['receive_bytes']) - int(last_data[key]['receive_bytes']))/1024/timecut 
            transmit = (int(now_data[key]['transmit_bytes']) - int(last_data[key]['transmit_bytes']))/1024/timecut 
            results[key] = {'receive':int(receive), 'transmit':int(transmit), 'bandwidth':bandwidth[key]}
    else:
        # 第一次加载的时候，历史数据为空，无法计算，所以初始化为0
        for key in devices:
            results[key] = {'receive':0, 'transmit':0, 'bandwidth':bandwidth[key]}
    return (status,msgs,results)
if __name__ == "__main__":
    while True:
        print get_ProcNetDev(devices=['eth0','eth2'], bandwidth={'eth0':1000, 'eth2':10000})
        time.sleep(1)


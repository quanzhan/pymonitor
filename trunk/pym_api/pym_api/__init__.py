#-*- coding:utf-8 -*-

import sys
import redis
#import json
import simplejson as json

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

r1 = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=1)    # 保存以IP为KEY，300个点的数据
r2 = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=2)

try:
    r1['foo'] = 'bar'
    r2['foo'] = 'bar'
    r1.delete('foo')
    r2.delete('foo')
except:
    print 'Error: Redis is not connected.'
    sys.exit(0)

def get_nodes_name():
    """ 获取被监控节点的IP地址列表
        @Return: (status, msgs, result)
                status = INT    # 执行状态
                msgs = STRING   # 如果status等于0, msgs is '', 否则将包含错误信息的字符串.
                results = LIST  # Example: ['172.16.10.11', '172.16.10.254', '172.16.10.12'] 
    """
    status, msgs, results = 0, '', ''
    try:
        results = r1.keys()
    except Exception, e:
        status = -1
        msgs = e
    return (status, msgs, results)
    
def get_nodes_all(count=1):
    """ 获取集群对应所有数据的平均值 """
    """ @Note: 获取集群中对应所有数据的平均值 
               数据由pym_server将数据存储到redis数据库中提供 
    """
    """ @Params: count = INT #取点：从当前时间往前取count个点，默认为当前时间点的数据，最大不会超过server配置项DATA_SIZE个点
        @Return: (status, msgs, result)
                status = INT #执行状态
                msgs = STRING #如果status等于0, msgs is '', 否则将包含错误信息的字符串.
                results =[ 
                '{"cpuload": {"cpuuse": 6}, "network": {"receive": 0, "transmit": 0}, "devices": {"reading": 0, "writing": 38}, "memorys": {"cached": 260036, "memused": 409532, "memtotal": 1017812, "buffers": 51268}}', 
                '{"cpuload": {"cpuuse": 5}, "network": {"receive": 0, "transmit": 0}, "devices": {"reading": 0, "writing": 11}, "memorys": {"cached": 260040, "memused": 409528, "memtotal": 1017812, "buffers": 51268}}'
                ] #此为count为2的结果，即为俩时刻的数据
                
    """
    
    status, msgs, results = 0, '', ''
    try:
        results= [i for i in r2.lrange('average_data',-count,-1)]
    except Exception,ex:
        msgs = ex
        status = 1
    return (status, msgs, results)

def get_node_all(ip='', count=1):
    """ 获取单个节点的所有数据 """ 
    """ @Note: 获取对应节点的所有数据
               数据由pym_server的redis数据库2提供"""
    """ @Params: count = INT #取点：从当前时间往前取count个点，默认为当前时间点的数据，最大不会超过server配置项DATA_SIZE个点
                 ip = STRING #对应取值节点的ip
        @Return: (status, msgs, result)
                status = INT #执行状态.
                msgs = STRING #如果status等于0, msgs is '', 否则将包含错误信息的字符串.
                results = [
                    '{"cpuload": {"cpuuse": 2}, "network": {"eth1": {"receive": 1, "transmit": 0, "bandwidth": "1000Mb/s"}, "eth0": {"receive": 0, "transmit": 0, "bandwidth": "1000Mb/s"}}, "devices": {"sda": {"reading": 0, "writing": 11}}, "memorys": {"cached": 260120, "memtotal": 1017812, "memused": 409244, "buffers": 52876}}', 
                    '{"cpuload": {"cpuuse": 0}, "network": {"eth1": {"receive": 0, "transmit": 0, "bandwidth": "1000Mb/s"}, "eth0": {"receive": 0, "transmit": 0, "bandwidth": "1000Mb/s"}}, "devices": {"sda": {"reading": 0, "writing": 13}}, "memorys": {"cached": 260120, "memtotal": 1017812, "memused": 409352, "buffers": 52876}}'
                ] #此为count为2的结果，即为俩时刻的数据
    """
    status, msgs, results = 0,'',''
    try:
        results = [i for i in r1.lrange(ip,-count,-1)]
    except Exception,ex:
        msgs=ex
        status=1
    return (status, msgs, results)

def get_nodes_cpu(count=1):
    """ 返回所有被监控节点的CPU负载数据， 数据选取前count秒的数据
        @Params: count = INT        # 要返回的数据量，最大不超过redis记录集, 默认返回最新的一个数据
        @Return: (status, msgs, results)
                status = INT    # 执行状态. 0正常执行， 非零， 表示发生错误， 错误消息在msgs
                msgs = STRING   # 如果status等于0, msgs is '', 否则将包含错误信息的字符串.
                results = []    # result为存储数据列表，长度为count的值  ,  数据格式， 参看下面的 Example.
        @Example: 
                In [6]: import pym_api

                In [45]: pym_api.get_nodes_cpu(count=1) # 返回最新一秒(count=1)的数据
                Out[45]: (0, '', [('192.168.112.189', [18]), ('192.168.112.190', [28])])  # 节点1的负载是 18%, 节点2的是 28%

                In [45]: pym_api.get_nodes_cpu(count=3) # 返回最新三秒(count=3)的数据
                Out[45]: (0, '', [('192.168.112.189', [18,12,14]), ('192.168.112.190', [28,22,49])])    # [18, 12, 14]: 其中14%是最新前一秒，12%是最新前两秒的，18%是最新前三秒的

    """
    status, msgs, results = 0, '', ''

    try:
        results = [{key:[node and json.loads(node)['cpuload']['cpuuse'] or node for node in r1.lrange(key, -count, -1)]} for key in r1.keys()]
    except Exception, e:
        status = -1; msgs = e;

    return (status, msgs, results)

def get_nodes_mem(count=1):
    """ 返回所有被监控节点的内存负载数据， 数据选取前count秒的数据, count=1的时候， 获取最新一秒的数据
        @Params: count = INT        # 要返回的数据量，最大不超过redis记录集, 默认返回最新的一个数据
        @Return: (status, msgs, results)
                status = INT    # 执行状态. 0正常执行， 非零， 表示发生错误， 错误消息在msgs
                msgs = STRING   # 如果status等于0, msgs is '', 否则将包含错误信息的字符串.
                results = []    # result为存储数据列表，长度为count的值  ,  数据格式， 参看下面的 Example.
        @Example: 
                In [6]: import pym_api

                In [34]: pym_api.get_nodes_mem(count=1)
                Out[34]: (0, '', [('192.168.112.189',
                                    [{'buffers': 5732,   # 缓冲大小，单位KB
                                      'cached': 439968,  # 缓存大小，单位KB
                                      'memtotal': 703996,   # 内存总容量， 单位KB
                                      'memused': 208524}])])    # 以使用内存， 单位KB

    """
    status, msgs, results = 0, '', ''

    try:
        results = [(key, [node and json.loads(node)['memorys'] or node for node in r1.lrange(key, -count, -1)]) for key in r1.keys()] 
    except Exception, e:
        status = -1; msgs = e;

    return (status, msgs, results)

def get_nodes_net(count=1):
    """ 返回所有被监控节点的网络负载数据， 数据选取前count秒的数据
        @Params: count = INT        # 要返回的数据量，最大不超过redis记录集, 默认返回最新的一个数据
        @Return: (status, msgs, results)
                status = INT    # 执行状态. 0正常执行， 非零， 表示发生错误， 错误消息在msgs
                msgs = STRING   # 如果status等于0, msgs is '', 否则将包含错误信息的字符串.
                results = []    # result为存储数据列表，长度为count的值  ,  数据格式， 参看下面的 Example.
        @Example: 
                In [6]: import pym_api
                
                In [7]: pym_api.get_nodes_net(count=1) # 返回最新一秒(count=1)的数据
                Out[7]: (0, '', {'192.168.112.189': [{'receive': 55, 'transmit': 2912}]})   # 单位KB/s, 其中 receive是节点的网络接收速度，transmit是网络的发送速度
                
                In [8]: pym_api.get_nodes_net(count=3)
                Out[8]: (0, '', {'192.168.112.189': [{'receive': 70, 'transmit': 3578}, {'receive': 84, 'transmit': 4352}, {'receive': 78, 'transmit': 4110}]})  # 单位KB/s, 其中 receive是节点的网络接收速度，transmit是网络的发送速度
    """
    status, msgs, results = 0, '', ''

    try:
        results = [(key, [node and json.loads(node)['network'] or node for node in r1.lrange(key, 0, -1)][-count:]) for key in r1.keys()]
        tmp = {}
        for (ip,nets) in results:
            temp = []
            for net in nets:
                receive = 0
                transmit = 0
                if net:
                    for key, values in net.items():
                        receive += values['receive'] 
                        transmit += values['transmit']
                temp.append({'receive': receive, 'transmit': transmit})
            tmp[ip] = temp
        results = tmp
    except Exception, e:
        status = -1; msgs = e; results = '';

    return (status, msgs, results)

def get_nodes_io(count=1):
    """ 返回所有被监控节点的IO负载数据， 数据选取前count秒的数据
        @Params: count = INT        # 要返回的数据量，最大不超过redis记录集, 默认返回最新的一个数据
        @Return: (status, msgs, results)
                status = INT    # 执行状态. 0正常执行， 非零， 表示发生错误， 错误消息在msgs
                msgs = STRING   # 如果status等于0, msgs is '', 否则将包含错误信息的字符串.
                results = []    # result为存储数据列表，长度为count的值  ,  数据格式， 参看下面的 Example.
        @Example: 
    """
    status, msgs, results = 0, '', ''

    try:
        results = [(key, [node and json.loads(node)['devices'] or node for node in r1.lrange(key, 0, -1)][-count:]) for key in r1.keys()]
        tmp = {}
        for (ip,ios) in results:
            temp = []
            for io in ios:
                reading = 0
                writing = 0
                if io:
                    for key, values in io.items():
                        reading += values['reading'] 
                        writing += values['writing']
                temp.append({'reading': reading, 'writing': writing})
            tmp[ip] = temp
        results = tmp
    except Exception, e:
        status = -1; msgs = e;

    return (status, msgs, results)


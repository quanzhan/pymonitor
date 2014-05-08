#-*- coding:utf-8 -*-
import redis
import json

def get_cpu_all(redishost='127.0.0.1', redisport=6379, count=1):
    """ 获取集群CPU负载的均值 """
    """ @Note: 获取集群中所有服务器负载的均值
               选取uptime 1分钟的负载值计算， 数据由pym_server的redis数据库提供，已经处理成百分比了 """ 
    """ @Params: count = INT #取点： 从当前时间往前取count个点， 默认去当前时间点的数据(数据库本身每秒产生一个新的数据值), 最大不超过300个点
                 redishost = IP #redis服务器的地址
                 redisport = INT #redis服务器的服务端口
        @Return: (status, msgs, result)
                status = INT #执行状态.
                msgs = STRING #如果status等于0, msgs is '', 否则将包含错误信息的字符串.
                results = [] # result为存储数据列表，长度为count的值 
    """
    status, msgs, results = 1,'',''
    try:
        data_all_redis = redis.Redis(host=redishost, port=redisport, db=3)
        results = data_all_redis.lrange('listtme',-count,-1)  
        status=0
    except Exception,ex:
        msgs=ex
        status=1
    return (status, msgs, results)

def get_cpu(redishost='127.0.0.1', redisport=6379, ip_address='127.0.0.1', count=1):
    """ 获取单个节点CPU负载的值"""
    """ @Note: 获取单个服务器负载
       选取uptime 1分钟的负载值计算， 数据由pym_server的redis数据库提供，已经处理成百分比了 """
    """ @Params: ip_address = STRING #节点的IP地址字串
                 count = INT #取点： 从当前时间往前取count个点， 默认去当前时间点的数据(数据库本身每秒产生一个新的数据值), 最大不超过300个点
                 redishost = IP #redis服务器的地址
                 redisport = INT #redis服务器的服务端口
        @Return: (status, msgs, results)
                status = INT #执行状态.
                msgs = STRING #如果status等于0, msgs is '', 否则将包含错误信息的字符串.
                results = [] # result为存储数据列表，长度为count的值 
    """
    status, msgs, results = 1, '', ''
    try:
        dbdata=int(ip_address.split('.')[-1])+10
        data_all_redis = redis.Redis(host=redishost, port=redisport, db=dbdata)
        results = data_all_redis.lrange('listtme',-count,-1)  
        status=0
    except Exception,ex:
        msgs=ex
        status=1
    return (status, msgs, results)
def get_network_all(redishost='127.0.0.1', redisport=6379, listname="listnetworkrx", count=1):
    """ 获取集群网络负载的均值"""
    """ @Params: redishost = IP #redis服务器的地址
                 redisport = INT #redis服务器的服务端口
                 listname = 'listnetworkrx' or 'listnetworktx'#对应于网络的下载和上传的速度
                 count = INT #取点： 从当前时间往前取count个点， 默认去当前时间点的数据(数据库本身每秒产生一个新的数据值), 最大不超过300个点
        @Return: (status, msgs, results)
                status = INT #执行状态.
                msgs = STRING #如果status等于0, msgs is '', 否则将包含错误信息的字符串.
                results = [] # result为存储数据列表，长度为count的值 
    """
    status, msgs, results = 1,'',''
    try:
        data_all_redis = redis.Redis(host=redishost, port=redisport, db=3)
        results = data_all_redis.lrange(listname,-count,-1)  
        status=0
    except Exception,ex:
        msgs=ex
        status=1
    return (status, msgs, results)

def get_network(redishost='127.0.0.1', redisport=6379, listname='listnetworkrx', count=1, ip_address='127.0.0.1'):
    """ 获取单台服务器网络负载的均值 """
    """ @Params: ip_address = STRING #节点的IP地址字串
                 redishost = IP #redis服务器的地址
                 redisport = INT #redis服务器的服务端口
                 listname = 'listnetworkrx' or 'listnetworktx'#对应于网络的下载和上传的速度
                 count = INT #取点： 从当前时间往前取count个点， 默认去当前时间点的数据(数据库本身每秒产生一个新的数据值), 最大不超过300个点
        @Return: (status, msgs, results)
                status = INT #执行状态.
                msgs = STRING #如果status等于0, msgs is '', 否则将包含错误信息的字符串.
                results = [] # result为存储数据列表，长度为count的值 
    """
    status, msgs, results = 1,'',''
    try:
        dbdata=int(ip_address.split('.')[-1])+10
        data_all_redis = redis.Redis(host=redishost, port=redisport, db=dbdata)
        results = data_all_redis.lrange(listname,-count,-1)  
        status=0
    except Exception,ex:
        msgs=ex
        status=1
    return (status, msgs, results)

def get_io_all(redishost='127.0.0.1', redisport=6379, count=1):
    """ 获取集群读写负载的均值"""
    """ @Params: count = INT #取点： 从当前时间往前取count个点， 默认去当前时间点的数据(数据库本身每秒产生一个新的数据值), 最大不超过300个点
                 redishost = IP #redis服务器的地址
                 redisport = INT #redis服务器的服务端口
        @Return: (status, msgs, results)
                status = INT #执行状态.
                msgs = STRING #如果status等于0, msgs is '', 否则将包含错误信息的字符串.
                results = [] # result为存储数据列表，长度为count的值 
    """
    status, msgs, results = 1,'',''
    try:
        data_all_redis = redis.Redis(host=redishost, port=redisport, db=3)
        results = data_all_redis.lrange('listio',-count,-1)  
        status=0
    except Exception,ex:
        msgs=ex
        status=1
    return (status, msgs, results)

def get_io(redishost='127.0.0.1', redisport=6379, ip_address='127.0.0.1', count=1):
    """ 获取集群读写负载的均值"""
    """ @Params: ip_address = STRING #节点的IP地址字串
                 count = INT #取点： 从当前时间往前取count个点， 默认去当前时间点的数据(数据库本身每秒产生一个新的数据值), 最大不超过300个点
                 redishost = IP #redis服务器的地址
                 redisport = INT #redis服务器的服务端口
        @Return: (status, msgs, results)
                status = INT #执行状态.
                msgs = STRING #如果status等于0, msgs is '', 否则将包含错误信息的字符串.
                results = [] # result为存储数据列表，长度为count的值 
    """
    status, msgs, results = 1, '', ''
    try:
        dbdata=int(ip_address.split('.')[-1])+10
        data_all_redis = redis.Redis(host=redishost, port=redisport, db=dbdata)
        results = data_all_redis.lrange('listio',-count,-1)  
        status=0
    except Exception,ex:
        msgs=ex
        status=1
    return (status, msgs, results)

def get_memory_all(redishost='127.0.0.1', redisport=6379, count=1):
    """ 获取集群内存负载的均值"""
    """ @Params: count = INT #取点： 从当前时间往前取count个点， 默认去当前时间点的数据(数据库本身每秒产生一个新的数据值), 最大不超过300个点
                 redishost = IP #redis服务器的地址
                 redisport = INT #redis服务器的服务端口
        @Return: (status, msgs, results)
                status = INT #执行状态.
                msgs = STRING #如果status等于0, msgs is '', 否则将包含错误信息的字符串.
                results = [] # result为存储数据列表，长度为count的值 
    """
    status, msgs, results = 1,'',''
    try:
        data_all_redis = redis.Redis(host=redishost, port=redisport, db=3)
        results = data_all_redis.lrange('listmemory',-count,-1)  
        status=0
    except Exception,ex:
        msgs=ex
        status=1
    return (status, msgs, results)

def get_memory(redishost='127.0.0.1', redisport=6379, ip_address='127.0.0.1', count=1):
    """ 获取单台服务器内存负载的均值"""
    """ @Params: ip_address = STRING #节点的IP地址字串
                 count = INT #取点： 从当前时间往前取count个点， 默认去当前时间点的数据(数据库本身每秒产生一个新的数据值), 最大不超过300个点
                 redishost = IP #redis服务器的地址
                 redisport = INT #redis服务器的服务端口
        @Return: (status, msgs, results)
                status = INT #执行状态.
                msgs = STRING #如果status等于0, msgs is '', 否则将包含错误信息的字符串.
                results = [] # result为存储数据列表，长度为count的值 
    """
    status, msgs, results = 1, '', ''
    try:
        dbdata=int(ip_address.split('.')[-1])+10
        data_all_redis = redis.Redis(host=redishost, port=redisport, db=dbdata)
        results = data_all_redis.lrange('listmemory',-count,-1)  
        status=0
    except Exception,ex:
        msgs=ex
        status=1
    return (status, msgs, results)

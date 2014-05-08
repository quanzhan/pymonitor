#coding:utf-8
# Create your views here.
# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
import models
import random
import redis
import json
def nodedatacluster(request):
	listname=request.GET.get('listname','') 
	files=file("/etc/monitor/node.conf")
	files=files.read()
	files=files.split('\n')
	files.pop()
	nodelist=[]
	for i in files:
		nodelist.append(i.split('.')[-1])
	print nodelist
	return render_to_response('monitor/nodedatacluster.html',locals())
def nodedatascluster(request):
	listname=request.GET.get('listname','') 
	listname1=request.GET.get('listname1','') 
	files=file("/etc/monitor/node.conf")
	files=files.read()
	files=files.split('\n')
	files.pop()
	nodelist=[]
	for i in files:
		nodelist.append(i.split('.')[-1])
	print nodelist
	return render_to_response('monitor/nodedatascluster.html',locals())
def cluster(request):
    return render_to_response('monitor/cluster.html',locals())
def clusterhuitu(request):
    return render_to_response('monitor/clusterhuitu.html',locals())
def clusterhuitu5(request):
    return render_to_response('monitor/clusterhuitu5.html',locals())
def clusterhuitu15(request):
    return render_to_response('monitor/clusterhuitu15.html',locals())
def memory(request):
    return render_to_response('monitor/memory.html',locals())
def io(request):
    return render_to_response('monitor/io.html',locals())
def network(request):
    return render_to_response('monitor/network.html',locals())

def uptime1(request):
    r=redis.Redis(host="127.0.0.1",port=6379,db=3)
    listt=r.lrange('listtme',0,-1)
    for i in range(len(listt)): 
        listt[i]=[i,listt[i]]
    listt=json.dumps(listt)
    return HttpResponse(listt)
def nodedata(request):
    listname=request.GET.get('listname','')
    dbname=request.GET.get('dbname','')
    r=redis.Redis(host="127.0.0.1",port=6379,db=int(dbname)+10)
    listt=r.lrange(listname,0,-1)
    listt=json.dumps(listt)
    return HttpResponse(listt)
def uptimenetwork(request):
    rx=request.GET.get('network','')
    r=redis.Redis(host="127.0.0.1",port=6379,db=3)
    if rx=='':
        listt=r.lrange('listnetworktx',0,-1)
        for i in range(len(listt)): 
            listt[i]=[i,listt[i]]
    else:
        listt=r.lrange('listnetworkrx',0,-1)
        for i in range(len(listt)): 
            listt[i]=[i,listt[i]]
    listt=json.dumps(listt)
    return HttpResponse(listt)
def uptimememory(request):
    r=redis.Redis(host="127.0.0.1",port=6379,db=3)
    listt=r.lrange('listmemory',0,-1)
    for i in range(len(listt)): 
        listt[i]=[i,listt[i]]
    listt=json.dumps(listt)
    return HttpResponse(listt)
def uptimeio(request):
    tt = random.random() * 100
    return HttpResponse(tt)
def uptime5(request):
    r=redis.Redis(host="127.0.0.1",port=6379,db=3)
    listt=r.lrange('listtme5',0,-1)
    listt=json.dumps(listt)
    for i in range(len(listt)): 
        listt[i]=[i,listt[i]]
    return HttpResponse(listt)
def uptime15(request):
    r=redis.Redis(host="127.0.0.1",port=6379,db=3)
    listt=r.lrange('listtme15',0,-1)
    listt=json.dumps(listt)
    for i in range(len(listt)): 
        listt[i]=[i,listt[i]]
    return HttpResponse(listt)
def memstat(request):   # 内容
    pass
def iostat(request):   # IO
    pass

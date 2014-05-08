import pyssh
import time
import re
INTERFACE='br0'
STATS=[]
def rx():
	ifstat=open('/proc/net/dev').readlines()
	for interface in ifstat:
		if INTERFACE in interface:
			stat=float(interface.split(":")[1].split()[0])
			STATS[0:]=[stat]
def tx():
	ifstat=open('/proc/net/dev').readlines()
	for interface in ifstat:
		if INTERFACE in interface:
			stat=float(interface.split()[8])
			STATS[1:]=[stat]
def network():
	dic={}
	rx()
	tx()
	dic['rx']=STATS[0]
	dic['tx']=STATS[1]
	return dic
def memory():
    dic={}
    (status,msg,memory)=pyssh.getcmd(cmd='/usr/bin/free -m|/bin/grep buffers/cache')
    memory=re.split(' +',memory)
    dic['total']=str(int(memory[2])+int(memory[3]))
    dic['used']=memory[2]
    dic['free']=memory[3]
    dic['use%']=str(round(float(dic['used'])*100/float(dic['total']),1))
    return dic
def load():
    dic={}
    (status,msg,load)=pyssh.getcmd(cmd='/usr/bin/uptime')
    load=load.strip()
    load=load.split('  ')
    load=load[-1].split(': ')
    load[1]=load[1].split(', ')
    for i in range(len(load[1])):
        if 0<float(load[1][i]) and float(load[1][i])<=1:
            load[1][i]=str(float(load[1][i])*0.6*100)
        elif 1<float(load[1][i]) and float(load[1][i])<=3:
            load[1][i]=str((float(load[1][i])+2)*20)
        elif float(load[1][i])>3:
            load[1][i]=str(100)
	load[0]=load[0].replace(" ","")
    dic[load[0]]=load[1]
    return dic
def rootsize():
    dic={}
    (status,msg,rootsize)=pyssh.getcmd(cmd='/bin/df -h|/bin/grep "/$"')
    rootsize=rootsize.strip() 
    rootsize=re.split(' +',rootsize)
    dic['size']=rootsize[0]
    dic['used']=rootsize[1]
    dic['avail']=rootsize[2]
    dic['use%']=rootsize[3]
    return dic
def all():
    networ=network()
    memor=memory()
    loa=load()
    bootsiz=rootsize()
    dic={}
    dic['network']=networ
    dic['memory']=memor
    dic['load']=loa
    dic['rootsize']=bootsiz
    return dic

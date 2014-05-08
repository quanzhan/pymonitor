
import time
import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)


dict1 = {
		'192.168.3.1':{'memery':{'used':10, 'total':20}, 'cpu':{'used':30}, 'network':{'in': 100, 'out':200}, 'io':{'in':100, 'out':200} }, 
}



try:
    import simplejson as json
except:
    import json

tmp = json.dumps(dict1)

r.delete('list1')
[r.rpush('list1', i) for i in range(500) ]


last_time = 0
while True:

	now_time = int(time.time())
	if now_time  == last_time:
		time.sleep(1)
		print 'lasttime, =' , now_time
	else:
		for i in range(10000):
                    r.lpop('list1')
                    r.rpush('list1', i)
		print '---------------------- now data: ', now_time
		last_time = now_time



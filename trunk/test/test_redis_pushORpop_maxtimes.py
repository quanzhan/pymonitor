
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




count = 0
end_c = 100 * 10000

start = time.time()
while count <= end_c:
	
        r.lpop('list1')
        #r.rpush('list1', 1000)

	count += 1

print end_c/(time.time() - start)


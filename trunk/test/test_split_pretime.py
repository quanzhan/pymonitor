import time

#import json
import simplejson as json

dict1 = {
		'192.168.3.10':{'memery':{'used':10, 'total':20}, 'cpu':{'used':30}, 'network':{'in': 100, 'out':200}, 'io':{'in':100, 'out':200} }, 
	}
tmp = json.dumps(dict1)

tt = "aaaaaaa$$" + tmp

print 'ttttttt= ', tt


count = 0
end_c = 100000000

start = time.time()
print 'start --------------'
while count <= end_c:

        tmp = tt.split('$$')[0]
	
	count += 1

print 'the times / pre time : ', int(end_c/(time.time() - start))


import time

dict1 = {
		'192.168.3.1':{'memery':{'used':10, 'total':20}, 'cpu':{'used':30}, 'network':{'in': 100, 'out':200}, 'io':{'in':100, 'out':200} }, 
		'192.168.3.2':{'memery':{'used':10, 'total':20}, 'cpu':{'used':30}, 'network':{'in': 100, 'out':200}, 'io':{'in':100, 'out':200} }, 
		'192.168.3.3':{'memery':{'used':10, 'total':20}, 'cpu':{'used':30}, 'network':{'in': 100, 'out':200}, 'io':{'in':100, 'out':200} }, 
		'192.168.3.4':{'memery':{'used':10, 'total':20}, 'cpu':{'used':30}, 'network':{'in': 100, 'out':200}, 'io':{'in':100, 'out':200} }, 
		'192.168.3.5':{'memery':{'used':10, 'total':20}, 'cpu':{'used':30}, 'network':{'in': 100, 'out':200}, 'io':{'in':100, 'out':200} }, 
		'192.168.3.6':{'memery':{'used':10, 'total':20}, 'cpu':{'used':30}, 'network':{'in': 100, 'out':200}, 'io':{'in':100, 'out':200} }, 
		'192.168.3.7':{'memery':{'used':10, 'total':20}, 'cpu':{'used':30}, 'network':{'in': 100, 'out':200}, 'io':{'in':100, 'out':200} }, 
		'192.168.3.8':{'memery':{'used':10, 'total':20}, 'cpu':{'used':30}, 'network':{'in': 100, 'out':200}, 'io':{'in':100, 'out':200} }, 
		'192.168.3.9':{'memery':{'used':10, 'total':20}, 'cpu':{'used':30}, 'network':{'in': 100, 'out':200}, 'io':{'in':100, 'out':200} }, 
		'192.168.3.10':{'memery':{'used':10, 'total':20}, 'cpu':{'used':30}, 'network':{'in': 100, 'out':200}, 'io':{'in':100, 'out':200} }, 
	}


count = 0
end_c = 1000000

start = time.time()
while count <= end_c:

	total = len(dict1)
	mem = 0
	cpu = 0
	net_in = 0
	net_out = 0
	io_in = 0
	io_out = 0
	for key, value in dict1.items():
		mem += value['memery']['used']
		cpu += value['cpu']['used']
		net_in += value['network']['in']
		net_out += value['network']['out']
		io_in += value['io']['in']
		io_out += value['io']['out']
	
	avg_memery =  mem/total
	avg_cpu = cpu/total
	avg_network_in = net_in/total
	avg_network_out = net_out/total
	avg_io_in =  io_in/total
	avg_io_out = io_out/total
	
	count += 1

print end_c/(time.time() - start)


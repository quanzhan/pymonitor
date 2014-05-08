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

#import json
import simplejson as json
tmp = json.dumps(dict1)

last_time = 0
while True:

	now_time = int(time.time())
	if now_time  == last_time:
		time.sleep(1)
		print 'lasttime, =' , now_time
	else:
		for i in range(10000):
			total = len(dict1)
			mem = 0
			cpu = 0
			net_in = 0
			net_out = 0
			io_in = 0
			io_out = 0
			dict1 = json.loads(tmp)
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

		print '---------------------- now data: ', now_time
		last_time = now_time



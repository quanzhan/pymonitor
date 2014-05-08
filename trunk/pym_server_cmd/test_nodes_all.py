
import time
import pym_api

while True:
    print pym_api.get_nodes_all()[2]

    time.sleep(1)



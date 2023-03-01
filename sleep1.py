import time 

stopp = time.time()+ 200
while time.time() < stopp:
	print(time.ctime())
	time.sleep(10)

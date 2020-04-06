import threading, time

def sleepandprint():
	# time.sleep(18)
	print('Hello from both of us')

def threadcode():
	print('Hello from new thread: My name is {} '.format(threading.currentThread().getName()))
	sleepandprint()
  

def main():
	print('Before starting a new thread My name is {}'.format(threading.currentThread().getName()))
	t = threading.Thread(target=threadcode, name='Childthread')
	daemon = False
	t.start()
	print ('Hello from main thread: My name is {}'.format(threading.currentThread().getName()))
	sleepandprint()
	t.join()
  
  
if __name__=='__main__':
	main()	


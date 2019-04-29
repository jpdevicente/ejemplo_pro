from threading import Thread, Lock
from time import sleep

mi_lock = Lock()
lock_2 = Lock()

def contador_a():
	while True:
		with mi_lock:
			print("lechuga")

		with lock_2:
			sleep(1)
		
			
					
def contador_b():
	while True:
		with mi_lock:
			print(" jamon")
		with lock_2:
			sleep(2)

t1 = Thread(target=contador_a)
t2 = Thread(target=contador_b)

t1.start()
t2.start()

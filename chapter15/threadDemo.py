import threading, time

print('Start Of Program.')
def takeANap():
	time.sleep(5)
	print('Wake Up.')

threadObj = threading.Thread(target=takeANap)
threadObj.start()

print('End Of Program.')
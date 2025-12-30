import time
stop = False
while not stop:
    print("enter s to stop the timer")
    time.sleep(1)
    press_stop = input("enter s to stop")


    if press_stop.lower() == 's' :
        stop = True
    
print("timer stopped")

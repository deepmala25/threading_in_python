import threading
import time

def cooking():
    time.sleep(5)
    print("food is cooked")

def washing_clothes(done):
    time.sleep(2)
    print(f"clothes washed {done}")

chore1 = threading.Thread(target=cooking)
chore1.start()
chore2 = threading.Thread(target=washing_clothes,args=("today",))
chore2.start()

chore1.join() #these both line will keep upcoming print line waiting till above functions are done
chore2.join()

print("all work done")

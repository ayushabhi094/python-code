import threading
from concurrent.futures import ThreadPoolExecutor
import time

def func(seconds):
    print(f"this will run in {seconds} seconds.")
    time.sleep(seconds)

# normal function
# func(4)
# func(2)
# func(1)
    
# threading function

# t1 = threading.Thread(target=func , args=[4])
# t2 = threading.Thread(target=func , args=[2])
# t3 = threading.Thread(target=func , args=[1])

# t1.start()
# t2.start()
# t3.start()

# # join([time])  − The join() waits for threads to terminate.
# t1.join()
# t2.join()
# t3.join()
def poolingdef():
    with ThreadPoolExecutor() as executor:
        future1 = executor.submit(func, 3)
        future2 = executor.submit(func, 2)
        future3 = executor.submit(func, 5)
        future4 = executor.submit(func, 7)
        print(future1.result())
        print(future2.result())
        print(future3.result())
        print(future4.result())


poolingdef()



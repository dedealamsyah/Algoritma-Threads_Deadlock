import threading
import time

# Membuat dua locks
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    print("Thread 1: mencoba mengunci lock1...")
    lock1.acquire()
    print("Thread 1: lock1 terkunci.")
    
    time.sleep(1)  # Menunggu sejenak untuk memastikan thread 2 mendapatkan lock2
    
    print("Thread 1: mencoba mengunci lock2...")
    lock2.acquire()
    print("Thread 1: lock2 terkunci.")
    
    # Melakukan sesuatu dengan kedua locks
    print("Thread 1: mengerjakan tugas dengan lock1 dan lock2...")
    
    lock2.release()
    print("Thread 1: lock2 dilepaskan.")
    
    lock1.release()
    print("Thread 1: lock1 dilepaskan.")

def thread2():
    print("Thread 2: mencoba mengunci lock2...")
    lock2.acquire()
    print("Thread 2: lock2 terkunci.")
    
    time.sleep(1)  # Menunggu sejenak untuk memastikan thread 1 mendapatkan lock1
    
    print("Thread 2: mencoba mengunci lock1...")
    lock1.acquire()
    print("Thread 2: lock1 terkunci.")
    
    # Melakukan sesuatu dengan kedua locks
    print("Thread 2: mengerjakan tugas dengan lock1 dan lock2...")
    
    lock1.release()
    print("Thread 2: lock1 dilepaskan.")
    
    lock2.release()
    print("Thread 2: lock2 dilepaskan.")

# Membuat thread
t1 = threading.Thread(target=thread1)
t2 = threading.Thread(target=thread2)

# Memulai thread
t1.start()
t2.start()

# Menunggu kedua thread selesai
t1.join()
t2.join()

print("Selesai.")

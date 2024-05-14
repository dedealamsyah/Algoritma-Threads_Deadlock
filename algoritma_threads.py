import threading
import time

# Fungsi yang akan dijalankan oleh setiap thread
def print_numbers(name, count):
    for i in range(count):
        print(f"Thread {name}: {i}")
        time.sleep(1)

# Membuat list untuk menyimpan thread
threads = []

# Jumlah thread yang akan dibuat
num_threads = 5
count = 10

# Membuat dan memulai thread
for i in range(num_threads):
    # Membuat thread
    thread = threading.Thread(target=print_numbers, args=(f'Thread-{i+1}', count))
    # Menambahkan thread ke dalam list
    threads.append(thread)
    # Memulai thread
    thread.start()

# Menunggu semua thread selesai
for thread in threads:
    thread.join()

print("Semua thread telah selesai.")

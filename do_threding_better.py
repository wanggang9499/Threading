# encoding:utf-8
import time
import threading

start = time.perf_counter()

def do_something(seconds):
    print("--------do something1---------\n")
    time.sleep(seconds)
    print("-------程序执行完毕-----------\n")


the_pool_of_threads = []
how_many_threads_do_you_want = 100
for _ in range(how_many_threads_do_you_want):
    every_thread = threading.Thread(target=do_something, args=[5])
    every_thread.start()
    the_pool_of_threads.append(every_thread)

    # print(the_pool_of_threads)

for thread in the_pool_of_threads:
    thread.join()

finish = time.perf_counter()

print(f'整个项目花费的 [{round(finish - start, 2)}]秒完成')

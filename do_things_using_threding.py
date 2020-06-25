# encoding:utf-8
import time
import threading

start = time.perf_counter()


def do_something():
    print("--------do something1---------\n")
    time.sleep(1)
    print("-------程序执行完毕-----------\n")


threading_1 = threading.Thread(target=do_something)
threading_2 = threading.Thread(target=do_something)
threading_3 = threading.Thread(target=do_something)
threading_4 = threading.Thread(target=do_something)
threading_5 = threading.Thread(target=do_something)

threading_1.start()
threading_2.start()
threading_3.start()
threading_4.start()
threading_5.start()

# 这里必须加上让每个线程完全运行完毕后在继续执行下方代码的命令
threading_1.join()
threading_2.join()
threading_3.join()
threading_4.join()
threading_5.join()

finish = time.perf_counter()

print(f'整个项目花费的 [{round(finish - start, 2)}]秒完成')

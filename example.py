import time 
start = time.perf_counter()

def do_something():
	print("--------do something1---------")
	time.sleep(1)
	print("-------程序执行完毕-----------")


do_something()
do_something()
do_something()
do_something()
do_something()

finish = time.perf_counter()


print(f'整个项目花费的 [{round(finish - start,2)}]秒完成')
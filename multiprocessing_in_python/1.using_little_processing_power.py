# encoding:utf-8
import time

start_time = time.perf_counter()


def do_what_you_want_the_computer_to_do():
    print("----开始运行某一个程序-----")
    time.sleep(1)
    print("----程序运行结束----")


do_what_you_want_the_computer_to_do()
do_what_you_want_the_computer_to_do()
do_what_you_want_the_computer_to_do()
do_what_you_want_the_computer_to_do()
do_what_you_want_the_computer_to_do()

end_time = time.perf_counter()
print(f'整个项目花费的时间{round(end_time-start_time,2)}秒完成')
# encoding:utf-8
import time
import multiprocessing

start_time = time.perf_counter()


def do_what_you_want_the_computer_to_do():
    print("----开始运行某一个程序-----\n")
    time.sleep(1)
    print("----程序运行结束----\n")


if __name__ == '__main__':
    processes = []
    for _ in range(10):
        every_process = multiprocessing.Process(target=do_what_you_want_the_computer_to_do)
        every_process.start()
        processes.append(every_process)

    for process in processes:
        process.join()

    end_time = time.perf_counter()
    print(f'整个项目花费的时间{round(end_time - start_time, 2)}秒完成')

import time
import multiprocessing

start_time = time.perf_counter()


def do_what_you_want_the_computer_to_do():
    print("----开始运行某一个程序-----\n")
    time.sleep(1)
    print("----程序运行结束----\n")


if __name__ == '__main__':
    processing_1 = multiprocessing.Process(target=do_what_you_want_the_computer_to_do)
    processing_2 = multiprocessing.Process(target=do_what_you_want_the_computer_to_do)
    processing_3 = multiprocessing.Process(target=do_what_you_want_the_computer_to_do)
    processing_4 = multiprocessing.Process(target=do_what_you_want_the_computer_to_do)
    processing_5 = multiprocessing.Process(target=do_what_you_want_the_computer_to_do)

    processing_1.start()
    processing_2.start()
    processing_3.start()
    processing_4.start()
    processing_5.start()

    processing_1.join()
    processing_2.join()
    processing_3.join()
    processing_4.join()
    processing_5.join()

    end_time = time.perf_counter()
    print(f'整个项目花费的时间{round(end_time - start_time, 2)}秒完成')

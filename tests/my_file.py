from threading import Thread

prev_thread = None
thread_1_executes_first = True


def thread_1_func():
    """
    Assign the value 1 to global variable my_var

    :return:
    """
    global prev_thread
    for i in range(10):
        # if the 2nd thread has ran then thread 1 task does not always run first
        if prev_thread == 2:
            global thread_1_executes_first
            thread_1_executes_first = False
        prev_thread = 1
        print(prev_thread)


def thread_2_func():
    """
    Assign the value 2 to global variable prev_thread

    :return:
    """
    global prev_thread
    for i in range(10):
        prev_thread = 2
        print(prev_thread)


def my_main():
    global prev_thread
    global thread_1_executes_first
    # create threads
    t1 = Thread(target=thread_1_func)
    t2 = Thread(target=thread_2_func)
    # run threads
    t1.start()
    t2.start()
    # wait for threads to finish
    t1.join()
    t2.join()
    return thread_1_executes_first


if __name__ == "__main__":
    my_main()

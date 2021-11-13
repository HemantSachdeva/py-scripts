from threading import *


def threaded_func():
    print('Current Thread being used:', current_thread().name)
    print('Thread ID being used:', current_thread().ident)


t = Thread(name="test", target=threaded_func)
t.start()

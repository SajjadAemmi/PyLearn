import threading
import time


def A(name, family):
    for i in range(40):
        print("Hello", name, family)


def B(name):
    for i in range(40):
        print("Bye Bye", name)
        time.sleep(1.5)


t1 = threading.Thread(target=A, args=['ali', 'hosseionzade'])
t2 = threading.Thread(target=B, args=['mamad'])

t1.start()
t2.start()

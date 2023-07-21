from threading import Thread
import time
import requests
from queue import Queue

start_time = time.time()

def scrapper(url):
    result = requests.get(url)
    my_queue.put(result.text)


urls = ['https://google.com',
        'https://apple.com',
        'https://microsoft.com',
        'https://sajjadaemmi.ir',
        'http://w3schools.com',
        'https://yahoo.com',
        'https://bing.com']

my_queue = Queue()
threads = []
for url in urls:
    new_thread = Thread(target=scrapper, args=[url])
    threads.append(new_thread)

for t in threads:
    t.start()

for t in threads:
    t.join()

while not my_queue.empty():
    print(my_queue.get())

end_time = time.time()

print(end_time - start_time)

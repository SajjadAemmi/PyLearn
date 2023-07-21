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

for url in urls:
    scrapper(url)


end_time = time.time()

print(end_time - start_time)

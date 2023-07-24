from threading import Thread
from time import time
import requests


def download(url, name):
    result = requests.get(url)

    f = open(name, "wb")
    f.write(result.content)
    f.close()


urls = [
    ["https://sajjadaemmi.ir/static/images/avatar.jpg", "output/test_image.jpg"],
    ["https://dkstatics-public.digikala.com/digikala-adservice-banners/a468d534b0489d6d6f05e1c1ef4b338677a740fc_1677678336.jpg?x-oss-process=image/quality,q_95", "output/image1.jpg"],
    ["https://dkstatics-public.digikala.com/digikala-adservice-banners/224406015b320b36e6c92fc57ad99891bcb5a435_1677676202.jpg?x-oss-process=image/quality,q_95", "output/image2.jpg"],
    ["https://dkstatics-public.digikala.com/digikala-products/f76850fe8a03750dbafa2758b733d58af991d1b5_1666239898.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90", "output/rande.jpg"],
        ["https://sajjadaemmi.ir/static/images/avatar.jpg", "output/test_image5.jpg"],
    ["https://dkstatics-public.digikala.com/digikala-adservice-banners/a468d534b0489d6d6f05e1c1ef4b338677a740fc_1677678336.jpg?x-oss-process=image/quality,q_95", "output/image6.jpg"],
    ["https://dkstatics-public.digikala.com/digikala-adservice-banners/224406015b320b36e6c92fc57ad99891bcb5a435_1677676202.jpg?x-oss-process=image/quality,q_95", "output/image7.jpg"],
    ["https://dkstatics-public.digikala.com/digikala-products/f76850fe8a03750dbafa2758b733d58af991d1b5_1666239898.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90", "output/rande8.jpg"],
        ["https://sajjadaemmi.ir/static/images/avatar.jpg", "output/test_image9.jpg"],
    ["https://dkstatics-public.digikala.com/digikala-adservice-banners/a468d534b0489d6d6f05e1c1ef4b338677a740fc_1677678336.jpg?x-oss-process=image/quality,q_95", "output/image10.jpg"],
    ["https://dkstatics-public.digikala.com/digikala-adservice-banners/224406015b320b36e6c92fc57ad99891bcb5a435_1677676202.jpg?x-oss-process=image/quality,q_95", "output/image11.jpg"],
    ["https://dkstatics-public.digikala.com/digikala-products/f76850fe8a03750dbafa2758b733d58af991d1b5_1666239898.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90", "output/rande12.jpg"],
        ["https://sajjadaemmi.ir/static/images/avatar.jpg", "output/test_image13.jpg"],
    ["https://dkstatics-public.digikala.com/digikala-adservice-banners/a468d534b0489d6d6f05e1c1ef4b338677a740fc_1677678336.jpg?x-oss-process=image/quality,q_95", "output/image14.jpg"],
    ["https://dkstatics-public.digikala.com/digikala-adservice-banners/224406015b320b36e6c92fc57ad99891bcb5a435_1677676202.jpg?x-oss-process=image/quality,q_95", "output/image15.jpg"],
    ["https://dkstatics-public.digikala.com/digikala-products/f76850fe8a03750dbafa2758b733d58af991d1b5_1666239898.jpg?x-oss-process=image/resize,m_lfit,h_800,w_800/quality,q_90", "output/rande16.jpg"],
        ["https://sajjadaemmi.ir/static/images/avatar.jpg", "output/test_image.jpg"]
]

start_time = time()

threads = []
for url, name in urls:
    threads.append(Thread(target=download, args=[url, name]))

for t in threads:
    t.start()

for t in threads:
    t.join()

end_time = time()

print(end_time - start_time)

import os
import requests
import cv2
import numpy as np


def add_noise_to_image(image):
    noise = np.random.normal(loc=0.0, scale=50, size=image.shape)
    noisy_image = image + noise
    noisy_image = np.clip(noisy_image, 0, 255)
    noisy_image = noisy_image.astype(np.uint8)
    return noisy_image


# Download the image from github
try:
    os.makedirs("input", exist_ok=True)
    url = "https://raw.githubusercontent.com/sajjadaemmi/pylearn/master/4_image_processing/session2_basic_operations/input/black_hole.jpg"
    r = requests.get(url)
    with open("input/black_hole.jpg", "wb") as f:
        f.write(r.content)
except Exception as e:
    print(e)

# Read the image
img = cv2.imread("input/black_hole.jpg")
height, width = img.shape[:2]

# Divide image into 4 parts
top_left = img[0:int(height/2), 0:int(width/2)]
top_right = img[0:int(height/2), int(width/2):width]
bottom_left = img[int(height/2):height, 0:int(width/2)]
bottom_right = img[int(height/2):height, int(width/2):width]
parts = [top_left, top_right, bottom_left, bottom_right]

for i, part in enumerate(parts):
    os.makedirs(os.path.join("input/black_hole/", str(i)), exist_ok=True)
    for j in range(5):
        noisy_image = add_noise_to_image(part)
        cv2.imwrite(os.path.join("input/black_hole/", str(i), f"{j}.jpg"), noisy_image)

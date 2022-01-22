import imageio
import os

images = []
for file_name in os.listdir('images'):
    img = imageio.imread('images' + '/' + file_name)
    images.append(img)

imageio.mimsave('walk.gif', images)

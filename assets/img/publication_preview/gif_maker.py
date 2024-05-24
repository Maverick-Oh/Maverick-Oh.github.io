import matplotlib.pyplot as plt
import imageio
import cv2

file_list = ['fig01.png',
             'fig02.png',
             'fig03.png']

images = []
size = (750,500)
for file in file_list:
    im = imageio.imread(file)
    im_resized = cv2.resize(im, size)
    images.append(im_resized)

imageio.mimsave('./movie.gif', images, format='GIF', duration=1)
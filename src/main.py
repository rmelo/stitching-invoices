import cv2
import numpy as np
from matplotlib import pyplot as plt
import time
import os

IMAGE_PATH = os.path.join(os.path.abspath(os.pardir), 'resources/images')

def showTime(t):
    return "%8.2f" % t

def resizeByWidth(img, new_width):
    (h, w, r) = img.shape
    if(w > new_width):
        h2 = int((new_width * h) / w)
        return cv2.resize(img, (new_width, h2))
    return img

def stitch(imgs):
    stitcher = cv2.createStitcher()
    ret, pano = stitcher.stitch(imgs)
    if ret == cv2.STITCHER_OK:
        return pano
    else:
        print('Error during stiching %d' % ret)


time1 = time.time()

images_count = 10
names = [os.path.join(os.path.join(IMAGE_PATH, "invoice-"+str(i)+".jpeg")) for i in range(1, images_count+1)]
images = [cv2.imread(x) for x in names]

time2 = time.time()

print("(%d) images loaded in %s secs" % (images_count, showTime(time2-time1)))

timeResize = time.time()

images = [resizeByWidth(img, 1024) for img in images]

finalTimeResize = time.time()

print("Images reduced in %s secs" % showTime(finalTimeResize-timeResize))


def imageSize(img):
    try:
        return len(img)
    except:
        return 0


def tryStitch(images, attempts=1, maxAttempts=3):
    if(attempts <= maxAttempts):
        print('Trying stitch images... (%d/%d).' % (attempts, maxAttempts))
        try:
            result = images[0]
            for i in range(1, images_count):
                result = stitch([result, images[i]])
            return result
        except:
            attempts += 1
            return tryStitch(images, attempts)
    else:
        print('Numbers of attempts exceeded.')

result = tryStitch(images)

cv2.imwrite('images/result.jpeg', result)

time3 = time.time()

print('Images stitched in %s secs' % showTime(time3-time2))

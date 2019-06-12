import cv2
from matplotlib import pyplot as plt


def resizeByWidth(img, new_width):
    (h, w, r) = img.shape
    if(w > new_width):
        h2 = int((new_width * h) / w)
        return cv2.resize(img, (new_width, h2))
    return img

img = cv2.imread('images/invoice-1.jpeg')
img2 = resizeByWidth(img, 5000)

print(img2.shape)
cv2.imwrite("test.jpeg", img2)

# plt.imshow(img2)
# plt.show()

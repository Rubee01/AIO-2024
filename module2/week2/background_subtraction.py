# Read Images
import numpy as np
import cv2
import os

dir_path = os.path.dirname(os.path.abspath(__file__))

bg_path = os.path.join(dir_path, 'images', 'GreenBackground.png')
bg1_image = cv2.imread(bg_path, 1)

ob_path = os.path.join(dir_path, 'images', 'Object.png')
ob_image = cv2.imread(ob_path, 1)

bg2_path = os.path.join(dir_path, 'images', 'NewBackground.jpg')
bg2_image = cv2.imread(bg2_path, 1)

# Resize image
IMAGE_SIZE = (678, 381)

bg1_image = cv2.resize(bg1_image, IMAGE_SIZE)
ob_image = cv2.resize(ob_image, IMAGE_SIZE)
bg2_image = cv2.resize(bg2_image, IMAGE_SIZE)

# Compute difference from background and object


def compute_difference(bg_img, input_img):
    difference_three_channel = cv2.absdiff(bg_img, input_img)
    difference_single_channel = np.sum(difference_three_channel, axis=2) / 3.0
    difference_single_channel = difference_single_channel.astype('uint8')

    return difference_single_channel

# convert to binary image


def compute_binary_mask(difference_single_channel):
    difference_binary = np.where(difference_single_channel >= 15, 255, 0)
    difference_binary = np.stack((difference_binary,)*3, axis=-1)
    return difference_binary

# Replace background


def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image, ob_image)
    binary_mask = compute_binary_mask(difference_single_channel)

    output = np.where(binary_mask == 255, ob_image, bg2_image)
    return output


output = replace_background(bg1_image, bg2_image, ob_image)
cv2.imshow('window', output)
cv2.waitKey(10000)

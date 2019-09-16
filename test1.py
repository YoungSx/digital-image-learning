import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image

def get_color_channels(img):
	img = img.copy()
	channels_num = len(img.shape)
	result = []
	
	channels = np.split(img, channels_nul, axis = 2)
	for i in channels:
		result.append(i.sum(axis = 2))
	return result
from skimage import io, color, filters
import numpy as np

image = io.imread('image_name.jpg')

gray_image = color.rgb2gray(image)

edges = filters.sobel(gray_image)

traffic_score = np.sum(edges > 0.1)

print(f"Traffic score: {traffic_score}")

THRESHOLD = 5000

if traffic_score > THRESHOLD:
    print("There is a traffic jam")
else:
    print("No traffic jam detected")
# 5-4  Yolo 이미지
# pip insatll ultralytics
from ultralytics import YOLO
import cv2
from matplotlib import pyplot as plt

model = YOLO('yolov8n.pt')

image_path = 'cat.jpeg'

results = model(image_path)

result = results[0]

img_with_boxes = result.plot()

plt.imshow(cv2.cvtColor(img_with_boxes, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()
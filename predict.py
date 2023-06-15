from ultralytics import YOLO

import cv2


model_path = 'C:/Users/Sahil Sahu/Desktop/Smart-Water-Quality-Monitoring-System/runs/segment/train4/weights/last.pt'
model_path2 = 'C:/Users/Sahil Sahu/Desktop/Smart-Water-Quality-Monitoring-System/runs/segment/train4/weights/best.pt'
image_path = 'C:/Users/Sahil Sahu/Desktop/Smart-Water-Quality-Monitoring-System/data/images/val/ALGAE11.png'

img = cv2.imread(image_path)
H, W, _ = img.shape

model = YOLO(model_path)
model2 = YOLO(model_path2)

results = model(img)
result2 = model2(img)

for result in results:
    for j, mask in enumerate(result.masks.data):

        mask = mask.numpy() * 255

        mask = cv2.resize(mask, (W, H))

        cv2.imwrite('./output.png', mask)

for result in result2:
    for j, mask in enumerate(result.masks.data):

        mask = mask.numpy() * 255

        mask = cv2.resize(mask, (W, H))

        cv2.imwrite('./output2.png', mask)


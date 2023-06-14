from ultralytics import YOLO

import cv2


model_path = 'model path after train'

image_path = '/Users/muntazirjahangir/Smart-Water-Quality-Monitoring-System/data/images/val/WaterAlgae_8717.png'

img = cv2.imread(image_path)
H, W, _ = img.shape

model = YOLO(model_path)

results = model(img)

for result in results:
    for j, mask in enumerate(result.masks.data):

        mask = mask.numpy() * 255

        mask = cv2.resize(mask, (W, H))

        cv2.imwrite('./output.png', mask)


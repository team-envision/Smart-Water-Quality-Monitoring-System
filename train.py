import os
from ultralytics import YOLO

model = YOLO('yolov8n-seg.pt') 

model.train(data='config.yaml', epochs=10, imgsz=640)

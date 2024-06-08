from ultralytics import YOLO
import cv2

model = YOLO('../yolo weights/yolov8n.pt')

results = model("images/gettyimages-185208032-612x612.jpg", show=True)

cv2.waitKey(0)

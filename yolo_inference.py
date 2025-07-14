#Import All the Required Libraries
from ultralytics import YOLO

#Load the YOLO Model
model = YOLO("model/best.pt")

#Object Detection
#results = model.predict(source = "input_videos/15sec_input_720p.mp4", save=True)

#Tracking
results = model.track(source = "input_video/15sec_input_720p.mp4", save=True, persist=True)
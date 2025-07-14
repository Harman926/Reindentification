# Player & Referee Detection – Football Match (YOLOv8 + Roboflow)

## 📌 Objective
Detect and differentiate between **football players** and **referees** from a match video using YOLOv8. This project prepares data for potential future **player re-identification** and **multi-object tracking** tasks.

---

## 🎯 Project Overview

- **Video Source**: `15sec_input_720p.mp4`
- **Total Frames Used**: 375
- **Classes Detected**: `player`, `referee`
- **Labeling Tool**: Roboflow (Auto Label)

---

## 🧠 Dataset Details

- Created a dataset of 375 images extracted from the match video.
- Used Roboflow's **Auto Labeling** with custom class descriptions:
  - `player`: Football player not referee.
  - `referee`: Player in yellow shirt.
- Dataset Version: v1
- Format: YOLOv8

## 🛠️ Tech Stack

- **YOLOv8** (Ultralytics)
- **Roboflow** – Dataset management and annotation
- **OpenCV** – Frame-level visualization
- **Python** – Detection pipeline
- **Google Colab** – Optional for training

---

## ⚙️ Model

Used an existing trained YOLOv8 model (`best.pt`) for detecting players and referees.  
*Training from the labeled dataset is optional and can be done later.*

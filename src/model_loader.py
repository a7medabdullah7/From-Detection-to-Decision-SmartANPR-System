
from ultralytics import YOLO

def load_model(weights_path="models/best.pt"):
    try:
        model = YOLO(weights_path)
        return model
    except Exception as e:
        print("Error loading model:", e)
        return None

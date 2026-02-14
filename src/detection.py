
import cv2

def run_detection(model, frame):
    results = model(frame)[0]
    return results

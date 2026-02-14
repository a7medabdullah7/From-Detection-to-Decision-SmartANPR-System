
import cv2
import argparse
from model_loader import load_model
from detection import run_detection

def main(source):
    model = load_model()
    if model is None:
        return

    cap = cv2.VideoCapture(source)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        results = run_detection(model, frame)
        annotated = results.plot()

        cv2.imshow("SmartANPR", annotated)

        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True, help="Image or video path")
    args = parser.parse_args()
    main(args.source)

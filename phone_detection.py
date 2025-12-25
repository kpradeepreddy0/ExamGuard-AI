from ultralytics import YOLO
import cv2

# Load YOLO model (COCO pretrained)
model = YOLO("yolov8n.pt")

def detect_phone(frame):
    """
    Returns (phone_found, box)
    box = [x1, y1, x2, y2] or None
    """
    results = model(frame, conf=0.25, imgsz=640, verbose=False)

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            if label in ["cell phone", "mobile phone"]:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                return True, [x1, y1, x2, y2]

    return False, None

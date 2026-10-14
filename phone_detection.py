
from ultralytics import YOLO

# Load the lightweight YOLO model once
model = YOLO("yolov8n.pt")


def detect_phone(frame):
    if frame is None:
        return False, None

    results = model(
        frame,
        conf=0.25,
        imgsz=640,
        verbose=False,
        device="cpu"
    )

    best_phone = None
    best_conf = 0.0

    for result in results:
        if result.boxes is None:
            continue

        for box in result.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            confidence = float(box.conf[0])

            if label != "cell phone" or confidence < 0.25:
                continue

            x1, y1, x2, y2 = map(int, box.xyxy[0])
            width = x2 - x1
            height = y2 - y1

            if width < 24 or height < 24:
                continue

            if confidence > best_conf:
                best_conf = confidence
                best_phone = [x1, y1, x2, y2]

    if best_phone is not None:
        print(f"PHONE DETECTED: confidence={best_conf:.2f}")
        return True, best_phone

    print("NO PHONE")
    return False, None

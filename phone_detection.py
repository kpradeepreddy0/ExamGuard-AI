from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

def detect_phone(frame):
    results = model(
        frame,
        conf=0.15,      # 🔴 LOWER confidence (IMPORTANT)
        imgsz=640,
        verbose=False
    )

    for r in results:
        if r.boxes is None:
            continue

        for box in r.boxes:
            cls_id = int(box.cls[0])
            label = model.names[cls_id]

            # ✅ ONLY valid COCO label
            if label == "cell phone":
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                return True, [x1, y1, x2, y2]

    return False, None

from ultralytics import YOLO

# Stronger model
model = YOLO("yolov8s.pt")


def detect_phone(frame):

    results = model(
        frame,
        conf=0.03,
        imgsz=1280,
        verbose=False
    )

    best_phone = None
    best_conf = 0

    for r in results:

        if r.boxes is None:
            continue

        for box in r.boxes:

            cls_id = int(box.cls[0])
            label = model.names[cls_id]
            confidence = float(box.conf[0])

            print(label, confidence)

            if label == "cell phone":

                if confidence > best_conf:

                    best_conf = confidence

                    x1, y1, x2, y2 = map(
                        int,
                        box.xyxy[0]
                    )

                    best_phone = [x1, y1, x2, y2]

    if best_phone:
        print("PHONE DETECTED")
        return True, best_phone

    print("NO PHONE")
    return False, None
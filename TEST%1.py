import cv2
import numpy as np

import time

# Load Yolo
net = cv2.dnn.readNet("yolov3-tiny.weights", "yolov3-tiny.cfg")
classes = []
with open("coco.names", "r") as f:
    classes = [line.strip() for line in f.readlines()]
layer_names = net.getLayerNames()
output_layers = [layer_names[i[0] - 1] for i in net.getUnconnectedOutLayers()]
colors = np.random.uniform(0, 255, size=(len(classes), 3))
font = cv2.FONT_HERSHEY_PLAIN
x_ = cv2.CAP_PROP_FRAME_WIDTH
y_ = cv2.CAP_PROP_FRAME_HEIGHT
# Loading image
cap = cv2.VideoCapture(0)

time_start = time.time()
frame_id = 0
while True:
    # print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    _, frame = cap.read()
    # frame = cv2.resize(frame, None, fx=2, fy=2)
    frame_id += 1
    height, width, channels = frame.shape

    # cv2.line(image, start_point, end_point, color, thickness)

    cv2.line(frame, (320, 0), (320, width), (0, 255, 0), 2)
    cv2.line(frame, (0, int(height / 2)), (640, int(height / 2)), (0, 255, 0), 2)
    # Detecting objects
    blob = cv2.dnn.blobFromImage(frame, 0.00392, (224, 224), (0, 0, 0), True, crop=False)

    net.setInput(blob)
    outs = net.forward(output_layers)

    # HUD
    class_ids = []
    confidences = []
    boxes = []
    for out in outs:
        for detection in out:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.001:
                # Object detected

                # if confiede

                center_x = int(detection[0] * width)
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                # Rectangle coordinates
                x = int(center_x - w / 2)
                y = int(center_y - h / 2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    # print(indexes)

    for i in range(len(boxes)):
        if i in indexes:
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = confidences[i]
            color = colors[class_ids[i]]
            # cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
            # cv2.circle(frame,(center_x,center_y),5, color,-1)
            cv2.line(frame, (320, 240), (center_x, center_y), color, 5)
            cv2.putText(frame, label + " " + str(round(confidence * 100)) + "%", (x, y + 30), font, 3, color, 3)

    elapsed_time = time.time() - time_start
    fps = frame_id / elapsed_time
    cv2.putText(frame, "FPS:" + str(round(fps, 2)), (10, 30), font, 2, (0, 0, 255), 2)
    cv2.putText(frame, "Press 'Q' to close the window", (380, 30), font, 1, (0, 0, 255), 2)
    cv2.imshow("Image", frame)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
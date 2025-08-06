from ultralytics import YOLO
import cv2

def predict(chosen_model, img, classes=[], conf=0.25):
    if classes:
        results = chosen_model.predict(img, classes=classes, conf=conf)
    else:
        results = chosen_model.predict(img, conf=conf)

    return results


def predict_and_detect(chosen_model, img, classes=[], conf=0.25, rectangle_thickness=2, text_thickness=1):
    results = predict(chosen_model, img, classes, conf=conf)
    for result in results:
        for box in result.boxes:
            cv2.rectangle(img, (int(box.xyxy[0][0]), int(box.xyxy[0][1])),
                          (int(box.xyxy[0][2]), int(box.xyxy[0][3])), (255, 255, 255), rectangle_thickness)      
            cv2.putText(img, f"{result.names[int(box.cls[0])]}",
                        (int(box.xyxy[0][0]), int(box.xyxy[0][1]) - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), text_thickness)
    return img, results

model = YOLO("best.pt")

# read the image
image = cv2.imread("1.jpg")
result_img, _ = predict_and_detect(model, image, classes=[], conf=0.25)

cv2.imshow("Image", result_img)
cv2.imwrite("12.jpg", result_img)
cv2.waitKey(0)

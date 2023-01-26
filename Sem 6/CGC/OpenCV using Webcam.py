import cv2 as cv
import time

video = cv.VideoCapture(0)

first_frame = None

while True:
    check, frame = video.read()  # check is a boolean value, frame is the image

    font = cv.FONT_HERSHEY_SIMPLEX

    cv.putText(frame, "S20200010042", (350, 80), cv.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 3)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    cv.putText(frame, "BOPPEY ROHITH", (350, 40), cv.FONT_HERSHEY_SIMPLEX,
                1, (0, 0, 255), 3)
    gray = cv.GaussianBlur(gray, (21, 21), 0)
    if first_frame is None:
        first_frame = gray
        continue
    delta_frame = cv.absdiff(first_frame, gray)
    threshold_frame = cv.threshold(delta_frame, 70, 255, cv.THRESH_BINARY)[1]
    threshold_frame = cv.dilate(threshold_frame, None, iterations=2)

    (cntr, _) = cv.findContours(threshold_frame.copy(),
                                 cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    for contour in cntr:
        if cv.contourArea(contour) < 1000:
            continue
        (x, y, w, h) = cv.boundingRect(contour)
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv.imshow("Capturing", frame)
    key = cv.waitKey(1)
    if key == ord('q'):
        break

video.release()
cv.destroyAllWindows()

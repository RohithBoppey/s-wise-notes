import cv2

# Initialize webcam
cap = cv2.VideoCapture(0)

while True:
    # Read first frame
    ret, frame1 = cap.read()
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    # Read next frame
    ret, frame2 = cap.read()
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    # Calculate difference between frames
    diff = cv2.absdiff(gray1, gray2)

    # Apply CLAHE to increase contrast
    clahe = cv2.createCLAHE(clipLimit=2, tileGridSize=(2, 2))
    final_frame = clahe.apply(diff)

    # Threshold the difference to identify motion
    thresh = cv2.threshold(final_frame, 60, 255, cv2.THRESH_BINARY)[1]

    # Dilate the thresholded image to fill in holes
    dilated = cv2.dilate(thresh, None, iterations=2)

    # Find contours in the dilated image
    cnts, _ = cv2.findContours(
        dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours on the original frame
    for c in cnts:
        if cv2.contourArea(c) < 11000:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        # print(x, y, w, h)
        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame1, "Name: {}".format('BOPPEY ROHITH'),
                    (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)
        cv2.putText(frame1, "Roll Number: {}".format('S20200010042'),
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (215, 10, 10), 3)

    # Show the frame
    cv2.imshow("Motion Detection", frame1)

    # Update the previous frame
    gray1 = gray2

    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
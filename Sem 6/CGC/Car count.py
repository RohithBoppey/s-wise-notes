'''
    PERSONAL DETAILS:
    NAME: BOPPEY ROHITH
    ROLL NUMBER: S20200010042
    CV ASSIGNMENT: 3
'''

import cv2

# Load the video file or stream
cap = cv2.VideoCapture("video.mp4")

# Initialize the background subtraction model
subtractor = cv2.createBackgroundSubtractorMOG2(history=100, varThreshold=50)

# Initialize the vehicle count for each direction
count_left = 0
count_right = 0

# Initialize a list to store the IDs of tracked vehicles
tracked_ids = []

while True:
    # Read a frame from the video
    ret, frame = cap.read()

    # If no frame is returned, break the loop
    if not ret:
        break

    # Apply background subtraction to extract moving objects
    fg_mask = subtractor.apply(frame)

    # Apply thresholding to remove noise
    thresh = cv2.threshold(fg_mask, 200, 255, cv2.THRESH_BINARY)[1]

    # Apply morphological operations to further remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    thresh = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

    # Find contours of the moving objects
    contours, hierarchy = cv2.findContours(
        thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Loop over the contours to detect and track vehicles
    for contour in contours:
        # Compute the area of the contour
        area = cv2.contourArea(contour)

        # If the area is too small or too large, ignore the contour
        if area < 100 or area > 10000:
            continue

        # Draw a bounding box around the contour
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Compute the center of the bounding box
        center = (int(x + w / 2), int(y + h / 2))

        # If the center is within a certain distance of a tracked vehicle, skip it
        for id in tracked_ids:
            if abs(center[0] - id[0]) < 20 and abs(center[1] - id[1]) < 20:
                break

        # Otherwise, add it to the tracked IDs and increment the count for the appropriate direction
        else:
            tracked_ids.append(center)
            if center[0] < frame.shape[1] / 2:
                count_left += 1
            else:
                count_right += 1

    # Display the frame and vehicle count for each direction
    cv2.putText(frame, "Left: " + str(count_left//5), (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.putText(frame, "Right: " + str(count_right//5),
                (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    cv2.imshow("Frame", frame)

    # Wait for a key press
    key = cv2.waitKey(1)

    # If the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break

# Release the video file or stream and close all windows
cap.release()
cv2.destroyAllWindows()

'''
    PERSONAL DETAILS:
    NAME: BOPPEY ROHITH
    ROLL NUMBER: S20200010042
    CV ASSIGNMENT: 3
'''

import cv2

cap = cv2.VideoCapture('video.mp4')

while True:
    ret, frame1 = cap.read()
    gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    ret, frame2 = cap.read()
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(gray1, gray2)
    thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]
    dilated = cv2.dilate(thresh, None, iterations=2)
    cnts, _ = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    gp_cnt = []
    for c in cnts:
        cv2.putText(frame1, "BOPPEY ROHITH", (1200, 80), cv2.FONT_HERSHEY_SIMPLEX,
                       1, (227, 97, 16), 3)
        cv2.putText(frame1, "S20200010042", (1200, 125), cv2.FONT_HERSHEY_SIMPLEX,
                       1, (227, 97, 16), 3)
        if cv2.contourArea(c) < 2000:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        if len(gp_cnt) == 0:
            gp_cnt.append([x, y, w, h])
        else:
            found_group = False
            for gp in gp_cnt:
                if abs(x - gp[0]) < 100 and abs(y - gp[1]) < 100:
                    gp[0] = min(gp[0], x)
                    gp[1] = min(gp[1], y)
                    gp[2] = max(gp[2], x + w - gp[0])
                    gp[3] = max(gp[3], y + h - gp[1])
                    found_group = True
                    break
            if not found_group:
                gp_cnt.append([x, y, w, h])
    for gp in gp_cnt:
        x, y, w, h = gp
        if w > 100:
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 0, 255), 2)
        else:
            cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow("Motion Detection", frame1)
    gray1 = gray2
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

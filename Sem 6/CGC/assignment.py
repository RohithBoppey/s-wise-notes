import cv2

cap = cv2.VideoCapture('video2.mp4')
car_cascade = cv2.CascadeClassifier('cars.xml')

while True:
    ret, frames = cap.read()
    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.1, 9)
    # if str(np.array(cars).shape[0]) == '1':
    #     i += 1
    #     continue
    count = 0;
    for (x,y,w,h) in cars:
        plate = frames[y:y + h, x:x + w]
        cv2.rectangle(frames,(x,y),(x +w, y +h) ,(51 ,51,255),2)
        cv2.rectangle(frames, (x, y - 40), (x + w, y), (51,51,255), -2)
        cv2.putText(frames, 'Car', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.imshow('car',plate)
        count += 1
        
        
    print(count)
    cv2.putText(frames, "Count: {}".format(count),
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 3)   

    # lab1 = "Car Count: " + str(i)
    # cv2.putText(frames, lab1, (40, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (147, 20, 255), 3)
    frames = cv2.resize(frames,(1000,700))
    cv2.imshow('Car Detection System', frames)
    # cv2.resizeWindow('Car Detection System', 600, 600)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cv2.destroyAllWindows()
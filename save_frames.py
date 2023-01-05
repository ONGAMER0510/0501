import cv2
room=15
cap=cv2.VideoCapture()
cap.open(f'rtsp://admin:sgis12345@172.16.16.132:554/Streaming/Channels/{room}01/')
success,frame=cap.read()
count=30000
font = cv2.FONT_HERSHEY_SIMPLEX
org = (50, 50)
fontScale = 1
color = (255, 0, 0)
thickness = 2
check=False
while success:
    # print(check)
    success,frame=cap.read()
    if check==True:
        cv2.imwrite(fr"C:\Science\extra\extra{count}.jpg", frame)
        # if count>=26000:
            # break
        count+=1
    cv2.namedWindow("Violence Detection", cv2.WINDOW_NORMAL)
    cv2.resizeWindow("Violence Detection", 1600, 900)
    frame = cv2.putText(frame,f"Frames No:{count}", org, font, fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow("Violence Detection",frame)
    if cv2.waitKey(1) == ord('q'):
    #   print("Hey")
      if check==True:
        check=False
      elif check==False:
        check=True
        
    # print(count)
import cv2
import os
import datetime



cap = cv2.VideoCapture(0) # 若傳回的()裡是0、1、2，代表第幾顆視訊鏡頭
picture_num = 1

if not cap.isOpened():
    print("攝影機無法開啟")
    exit()

if os.path.exists("D://hahaha") == False:
    os.makedirs("D://hahaha")

while picture_num < 10:
    loc_dt = datetime.datetime.today() 
    loc_dt_format = loc_dt.strftime("%Y_%m_%d__%H_%M_%S")
    
    ret, frame = cap.read() #會存兩個參數，(第一個是bool值，若有下一幀圖片，回傳true)，(第二個是讀圖片)
    if ret:
        frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5) # 縮放圖片
        cv2.imwrite(f"D://hahaha/picture{loc_dt_format}.png", frame)
        picture_num += 1
        cv2.imshow("frame", frame)
        cv2.waitKey(100)
    

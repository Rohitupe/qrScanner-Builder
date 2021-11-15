import cv2
from pyzbar.pyzbar import decode
import ast
import cvzone

video = cv2.VideoCapture(0)

# Show Information Message as Image
correct_img = cv2.imread('correct.png', cv2.IMREAD_UNCHANGED)
incorrect_img = cv2.imread('remove.png', cv2.IMREAD_UNCHANGED)

while True:
    _, frame = video.read()
    cv2.imshow('Frame', frame)   # Show video Frame
    scanned_data = decode(frame)   # Scan qr code from Video Frame
    try:
        # If information is in correct format
        for info in scanned_data:
            if type(info[0]) == bytes:
                a = ast.literal_eval(info[0].decode('utf-8'))   # Get only required information
                print(a)
                imgResult = cvzone.overlayPNG(frame, correct_img, [20, 20])   # Overlay Correct image if success
                cv2.imshow('Frame', imgResult)

    except Exception as e:
        # if information is not in correct format or failed while scanning
        # print(e)
        imgResult = cvzone.overlayPNG(frame, incorrect_img, [20, 20])   # Overlay InCorrect image if failure
        cv2.imshow('Frame', imgResult)


    if cv2.waitKey(1) & 0xFF == ord('q'):   # press q to quit
        break

video.release()
cv2.destroyAllWindows()
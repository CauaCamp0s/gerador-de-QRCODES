import cv2
import webbrowser

cap = cv2.VideoCapture(cv2.CAP_DSHOW + 0)  # use o ID da sua câmera em vez de 0
detector = cv2.QRCodeDetector()
while True:
    ret, img = cap.read()
    if ret:
        data, one, _ = detector.detectAndDecode(img)
        if data:
            a = data
            break
        cv2.imshow('QRcodescanner.exe', img)
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

b = webbrowser.open(str(a))
cap.release()
cv2.destroyAllWindows()



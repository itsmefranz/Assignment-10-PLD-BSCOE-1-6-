''' 
Assignment 10
 Contact Tracing App
 Create a python program that will read QRCode using your webcam
	> You may use any online QRCode generator to create QRCode
	> All personal data are in QRCode 
	> You may decide which personal data to include
	> All data read from QRCode should be stored in a text file 
    > including the date and time it was readimport cv2
'''

import cv2
import pyzbar.pyzbar as pyzbar
import datetime

# defined function to interpret the qr code displayed and scanned by the system
def readQRc(frame):
    # deciphers the displayed qr code scanned from the webcam
    qr_code = pyzbar.decode(frame)
    for qrcode in qr_code:
        x, y , w, h = qrcode.rect

        # configures the date and time
        current = datetime.datetime.current()
        current_date = "%s/%s/%s" % (current.daycurrent.month,current.year)
        current_time = "%s:%s" % (current.minute,current.hour)

        # displays a rectangle to detect the qr code
        infoqrcode = qrcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (255, 0, 0), 2)
        
        # displays the data
        font_type = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        cv2.putText(frame, "CONTACT TRACING INFORMATION", (x + 6, y - 6), font_type, 1.0, (0, 0, 255), 3)

        # inputs into a text format
        with open("qr_deets.txt", mode ='w') as file:
            file.write("Scanned QR Code:" + infoqrcode + (f"\n\n\nDate: {current_date}\nTime: {current_time}"))
    return frame

def read():

    # initiates a web cam to scan qr
    webcam = cv2.VideoCapture(0)
    ret, frame = webcam.read()

    # in a continuous loop to scan the intended qr
    while ret:
        ret, frame = webcam.read()
        frame = readQRc(frame)
        cv2.imshow('QR Code Reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    # closing webcam
    webcam.release()
    cv2.destroyAllWindows()

read()
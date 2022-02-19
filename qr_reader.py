''' 
Assignment 10
 Contact Tracing App
 Create a python program that will read QRCode using your webcam
	- You may use any online QRCode generator to create QRCode
	- All personal data are in QRCode 
	- You may decide which personal data to include
	- All data read from QRCode should be stored in a text file 
   - including the date and time it was readimport cv2
'''

import cv2
import pyzbar.pyzbar as pyzbar
import datetime

# function to read QR Code
def readQRc(frame):
    # decoding the QR code from webcam
    qr_code = pyzbar.decode(frame)
    for qrcode in qr_code:
        x, y , w, h = qrcode.rect

        # the date and time configuration
        current = datetime.datetime.current()
        datecurrent = "%s/%s/%s" % (current.daycurrent.month,current.year)
        timecurrent = "%s:%s" % (current.minute,current.hour)

        # drawing a rectangle to see if code is detected
        qrcodeInfo = qrcode.data.decode('utf-8')
        cv2.rectangle(frame, (x, y),(x+w, y+h), (255, 0, 0), 2)
        
        # text to show decoded data
        font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX
        cv2.putText(frame, "CONTACT TRACING INFORMATION", (x + 6, y - 6), font, 1.0, (0, 0, 255), 3)

        # writing it into a text file
        with open("qr_deets.txt", mode ='w') as file:
            file.write("Scanned QR Code:" + qrcodeInfo + (f"\n\n\nDate: {datecurrent}\nTime: {timecurrent}"))
    return frame

def read():

    # initializing web cam 
    webcam = cv2.VideoCapture(0)
    ret, frame = webcam.read()

    # loop to continuously scan for QR and not close
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
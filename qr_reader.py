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


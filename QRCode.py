#We are Going to Make a Application 
#Using which we can generate QRCode using our python code

#Let's say you want to Create a QRCode for a particular website
#So, You can just pass the URL of that website ,And Our Code will Generate QRCode for that...
#and when that QRCode is Scanned , it'll Redirect to that Particular Website.

#First, we need install package 'PyQRCode'

#pip install PyQRCode
#run this on your Cmd/Terminal, and install the library

#also, Install 'pypng' library
#pip install pypng

#import the PyQRCode library
# to use its Functionalities in the Code
import pyqrcode

#a variable named 'url', used to store the URL of the website
# for which the QR is to be generated
url = input("Enter a URL To Generate a QRCode: \n")

#The create() function from pyqrcode generates a QR code 
#based on the input provided, which in this case is the URL.
#This function takes the URL as an argument and generates 
#the QR code in an internal format, storing it in the 'QR' variable.
QR = pyqrcode.create(url)

#The png() method is called on the QR object 
# to save the generated QR code as a PNG image.
#The scale=8 argument controls the size of the image.
QR.png("Webqr.png",scale=8)

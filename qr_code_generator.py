!pip install qrcode
!pip install pillow

import qrcode
data = input("Enter URL to Make QR: ")
qr = qrcode.make(data)
qr.save("Generated_QR.png")
print("QR code created successfully!")

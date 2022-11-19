import qrcode

data = 'My first QR Code in Python'
qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)

qr.add_data(data)

qr.make(fit = True)
img = qr.make_image(fill_color = "grey", back_color = "white")

img.save("C:/Users/Patricio/Desktop/proyectos/QR Generator/img/myqrcode2.png")
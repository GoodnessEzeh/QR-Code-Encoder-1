import qrcode

data = 'Goodness Ezeh loves coding with Python'

img = qrcode.make(data)

img.save('C:/Users/user/Documents/QR-Code/myqrcode.png')
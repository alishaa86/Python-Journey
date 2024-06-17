#   QR CODE GENERATOR
  #   FIRST METHOD
# import qrcode as qr

# img = qr.make("Hello I am PYTHON here")
# img.save("Hello_World.png")


           # SECOND METHOD

import qrcode
from PIL import Image
import qrcode.constants

qr = qrcode.QRCode(version = 1,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size=10, border=4,)

qr.add_data("https://www.google.com/")
qr.make(fit=True)
img = qr.make_image(fill_color="green",back_color="black")
img.save("google.png")
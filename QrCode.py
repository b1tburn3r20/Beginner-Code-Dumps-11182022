import qrcode
from PIL import Image
img = qrcode.make('Your input text')
qr = qrcode.QRCode( 
    version = 1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4)

qr.add_data('https://www.linkedin.com/company/yoozoogames?trk=public_profile_topcard-current-company')
qr.make(fit=True)
img = qr.make_image(fill_color="black",
back_color="white").convert('RGB')
img.save("sample.png")
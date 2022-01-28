import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.clear()
qr.add_data('1@lTZbAjBj2IGh0hZx7nnw46fuWqEvfQ9sq88Ax60GG+FZ9CUa72/zclxW,RwVmMD4+FOOll6Y5L4YxCG4wj2UXEHJ4ChbAoOLIr2k=,5i3aeN9kL2GnS5HtK69Xww==')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save('qrcode.png')
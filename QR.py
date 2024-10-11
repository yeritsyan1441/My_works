import qrcode


def CREATE_QR(path="Learn python", image_name="qr"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2
    )
    qr.add_data(path)
    qr.make(fit=True)
    image = qr.make_image(fill_color="red", back_color="white")
    image.save(f"{image_name}.png")


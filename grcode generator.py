import qrcode
print('This is qrcode generator.')
user_url = input('Please enter your url:\n')
user_png_name = input('Write what your .png file will be called:\n')

def generate_qrcode(text):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save(user_png_name)

generate_qrcode(user_url)
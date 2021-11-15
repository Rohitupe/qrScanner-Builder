import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

information = {
    'Name': 'Rohit Dayanand Tupe',
    'EMP ID': 12345,
    'Email': 'rohit.tupe21@gmail.com',
    'Phone Number': 9326350663,
    'Age': 25
}


def generate_code(in_information):
    qr.add_data(in_information)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('code.png')


generate_code(information)

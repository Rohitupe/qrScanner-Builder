from PIL import Image
from pyzbar.pyzbar import decode
import ast

data = decode(Image.open('code.png'))

for info in data:
    print(info)
    if type(info[0]) == bytes:
        a = ast.literal_eval(info[0].decode('utf-8'))
        print(a)

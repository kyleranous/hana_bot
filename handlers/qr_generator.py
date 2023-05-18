"""
Will generate a QR Code and send it as a png to the user
"""
import os
import qrcode


def generate_qr_code(data):
    '''
    Function takes in a string and generates a QR Code image
    '''
    img = qrcode.make(data)
    type(img)
    img.save('qr.png')
    
    return os.path.abspath('qr.png')
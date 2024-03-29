from PIL import Image
from painter.binary_helper.binary_helper import *
from cryptography.fernet import Fernet
from painter.key_generator.key_generator import make_key_for_fernet
import base64

def get_secret_message(img_path: str, key: str = "", termination_symbol: str ="///") -> bytes:
    message = _get_message_from_image(img_path=img_path, termination_symbol=termination_symbol)
    if not key == "":
        message = _decode_message(message, key)
    return base64.urlsafe_b64decode(message)
    
def _get_message_from_image(img_path: str, termination_symbol: str) -> any: 
    message: bytearray = bytearray()
    with Image.open(img_path) as img:
        current_part = "0b"
        for y in range(img.height):
            for x in range(img.width):
                red_value = img.getpixel((x,y))[0]
                red_bin = get_eight_digit_binary_of_num(red_value)
                current_part += red_bin[-2:]
                if len(current_part) == 10:
                    if not message.decode("ascii")[-1*len(termination_symbol):] == termination_symbol:
                        cur_as_int = int(current_part, base=0)
                        message.append(cur_as_int)
                        current_part = "0b"
        message = message[0:len(message)-3]
        return message

def _decode_message(message: bytes, key: str):
    key = make_key_for_fernet(key)
    f = Fernet(key)
    return f.decrypt(bytes(message) + b"==")
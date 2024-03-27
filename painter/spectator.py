from PIL import Image
from painter.binary_helper.binary_helper import *
from painter.painter import termination_symbol


def decode_secret(img_path: str):
    message = ""
    with Image.open(img_path) as img:
        current_part = "0b"
        for y in range(img.height):
            for x in range(img.width):
                red_value = img.getpixel((x,y))[0]
                red_bin = get_eight_digit_binary_of_num(red_value)
                current_part += red_bin[-2:]
                if len(current_part) == 10:
                    message += chr(int(current_part, base=0))
                    if message[-3:] == "\\\\\\":
                        return message[:-3]
                    current_part = "0b"
    return message
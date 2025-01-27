from PIL import Image
from painter.binary_helper.binary_helper import *
from cryptography.fernet import Fernet
import base64
from painter.key_generator.key_generator import make_key_for_fernet

def hide_message(img_path: str, message: str = "Hello World!", key: str = "", termination_symbol: str = "///"):
    message = base64.urlsafe_b64encode(bytes(message, "utf-8"))
    if key == "":
        print("ERROR: No key was given!")
        return
    message = _encrypt_message(message=message, key=key)
    message += bytes(termination_symbol, "ascii")
    with Image.open(img_path) as img:
        newimg = Image.new(img.mode, img.size)
        x = 0
        y = 0
        for c in message:
            c_bin = get_eight_digit_binary_of_num(c)
            for i in range(4):
                if x >= img.width:
                    x = 0
                    y += 1

                org_pixel = img.getpixel((x,y))
                org_pixel_R = org_pixel[0]

                ##Insert the message into the pixel
                org_pixel_bin = get_eight_digit_binary_of_num(org_pixel_R)
                message_part_to_include = c_bin[i*2:i*2+2]
                new_pixel_bin = org_pixel_bin[:-2] + message_part_to_include
                newimg.putpixel(xy=(x,y), value=(int(new_pixel_bin, 2), org_pixel[1], org_pixel[2]))
                x += 1

        _fill_rest_of_image(img=img, newimg=newimg, x=x, y=y)

    newimg.save(img_path[:-4]+"_secret.png")

def _fill_rest_of_image(img: Image, newimg: Image, x, y):
    #fill the rest of the line with the original pixels
    for rest_x in range(x, img.width):
        newimg.putpixel((rest_x,y), img.getpixel((rest_x,y)))
    #fill the rest of the image with the original pixels
    for y in range(y+1, img.height):
        for x in range(0, img.width):
            newimg.putpixel((x,y), img.getpixel((x,y)))
    return newimg

def _encrypt_message(message: str, key: str):
    key = make_key_for_fernet(key)
    f = Fernet(key)
    return f.encrypt(message)
from PIL import Image
from painter.binary_helper.binary_helper import *

termination_symbol = "\\\\\\"

def hide_message(img_path: str, message: str = "Hello World!"):
    message += termination_symbol
    with Image.open(img_path) as img:
        newimg = Image.new(img.mode, img.size)
        x = 0
        y = 0
        for c in message:
            c_bin = get_eight_digit_binary_of_char(c)
            
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

        #fill the rest of the line with the original pixels
        for rest_x in range(x, img.width):
            newimg.putpixel((rest_x,y), img.getpixel((rest_x,y)))
        #fill the rest of the image with the original pixels
        for y in range(y+1, img.height):
            for x in range(0, img.width):
                newimg.putpixel((x,y), img.getpixel((x,y)))

    newimg.save(img_path[:-4]+"_secret.png")
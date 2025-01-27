from painter import painter, spectator
import argparse

termination_symbol = "///"

file = open("result.txt", "w")

parser = argparse.ArgumentParser("Hide messages in images")
parser.add_argument("-m", "--message", action="store", nargs="+", help="Necessary when encrypting a message")
parser.add_argument("-k", "--key", action="store", required=True, help="The key which is/was used for encryption. This field is necessary when encrypting and decrypting")
parser.add_argument("-d", "--decode", action="store_true", required=False, help="Switches the mode to ''decoding'' instead of ''encoding''")
parser.add_argument("-o", "--output", action="store_true", required=False, help="When set, writes the output in the result.txt file instead of printing in the console")
parser.add_argument("-i", "--image", action="store", required=True, help="Specifies the image in which the message should be embedded")
args = parser.parse_args()
decode_mode = args.decode
key = ""
output = args.output
if not args.key is None:
    key = args.key
img_path = "images/" + args.image

if decode_mode:
    result = spectator.get_secret_message(img_path=img_path, key=key, termination_symbol=termination_symbol)
    result = result.decode("ascii")
    if output:
        file.write(result)
    else:
        print(result)
else:
    message_to_hide = " ".join(args.message)
    painter.hide_message(img_path=img_path, message=message_to_hide, key=key, termination_symbol=termination_symbol)

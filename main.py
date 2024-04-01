from painter import painter, spectator
import argparse

termination_symbol = "///"

file = open("result.txt", "w")

parser = argparse.ArgumentParser("Hide messages in images")
parser.add_argument("-m", "--message", action="store", nargs="+")
parser.add_argument("-k", "--key", action="store", required=False)
parser.add_argument("-d", "--decode", action="store_true", required=False)
parser.add_argument("-o", "--output", action="store_true", required=False)
parser.add_argument("-i", "--image", action="store_true", required=True)
args = parser.parse_args()
message_to_hide = " ".join(args.message)
decode_mode = args.decode
key = ""
output = args.output
if not args.key is None:
    key = args.key
img_path = args.image

if not decode_mode:
    painter.hide_message(img_path=img_path, message=message_to_hide, key=key, termination_symbol=termination_symbol)
else:
    result = spectator.get_secret_message(img_path=img_path, key=key, termination_symbol=termination_symbol)
    result = result.decode("ascii")
    if output:
        file.write(result)
    else:
        print(result)

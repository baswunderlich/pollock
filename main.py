from painter import painter, spectator
import argparse

img_path = "testing_images/pollock.png"
img_path_secret = "testing_images/pollock_secret.png"
file = open("result.txt", "w")

parser = argparse.ArgumentParser("Hide messages in images")
parser.add_argument("-m", "--message", action="store", nargs="+")
parser.add_argument("-d", "--decode", action="store_true")
args = parser.parse_args()
message_to_hide = " ".join(args.message)
decode_mode = args.decode

if not decode_mode:
    painter.hide_message(img_path=img_path, message=message_to_hide)
else:
    result = spectator.decode_secret(img_path=img_path_secret)
    file.write(result)

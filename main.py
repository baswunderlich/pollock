from painter import painter, spectator

img_path = "testing_images/pollock.png"
img_path_secret = "testing_images/pollock_secret.png"
# painter.blacken_image("testing_images/pollock.png")
# painter.copy_image("testing_images/pollock.png")
file = open("result.txt", "w")

painter.hide_message(img_path=img_path)
result = spectator.decode_secret(img_path=img_path_secret)

file.write(result)
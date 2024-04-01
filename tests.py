import unittest
from painter.painter import hide_message
from painter.spectator import get_secret_message

class TestEncryption (unittest.TestCase):
    def test_embedding(self):
        message = "This is a secret text message which is supposed to be embedded into an image"
        img_path = "./testing_images/pollock.png"
        img_path_secret = "./testing_images/pollock_secret.png"
        hide_message(img_path=img_path, message=message)
        secret_message = get_secret_message(img_path=img_path_secret)
        assert(secret_message.decode("ascii") == message)
        
    def test_encryption(self):
        message = "This is a secret text message which is supposed to be embedded into an image"
        img_path = "./testing_images/pollock.png"
        img_path_secret = "./testing_images/pollock_secret.png"
        key = "not so secret key"
        hide_message(img_path=img_path, message=message, key=key)
        secret_message = get_secret_message(img_path=img_path_secret, key=key)
        assert(secret_message.decode("ascii") == message)

if __name__ == '__main__':
    unittest.main()
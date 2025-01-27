# Overview

With "pollock", you can hide messages in images. It uses cryptography to encrypt the message this message gets then embedded in the specified image (steganography). Therefore you are able to communicate in plain sight without anyone knowing there is a second meaning to what you are saying.

## Encryption

        python .\main.py -m "my secret message" --image "pollock.png" -k "my_secret_key" 

## Decryption

        python .\main.py --image "pollock_secret.png" -k "my_secret_key" -d
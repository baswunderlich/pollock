# Overview

With this tool, you can hide messages in images

## Encryption

        python .\main.py -m "my secret message" --image "pollock.png" -k "my_secret_key" 

## Decryption

        python .\main.py --image "pollock_secret.png" -k "my_secret_key" -d
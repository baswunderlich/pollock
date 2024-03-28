
def get_eight_digit_binary_of_char(character: int):
    c_bin = bin(ord(character))[2:]
    if(len(c_bin) < 8):
        for _ in range(8 - len(c_bin)):
            c_bin = "0" + c_bin
    return c_bin

def get_eight_digit_binary_of_num(number: int):
    c_bin = bin(number)[2:]
    if(len(c_bin) < 8):
        for _ in range(8 - len(c_bin)):
            c_bin = "0" + c_bin
    return c_bin

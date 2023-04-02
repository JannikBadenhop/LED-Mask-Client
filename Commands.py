# wrapping and encryption
def mask_encrypt(value):
    from Crypto.Cipher import AES
    from Crypto.Cipher.AES import MODE_ECB
    key = b'\x32\x67\x2f\x79\x74\xad\x43\x45\x1d\x9c\x6c\x89\x4a\x0e\x87\x64'
    cipher = AES.new(key, MODE_ECB)
    return cipher.encrypt(value)

def wrap_command(command:str, data:int):
    command = command.upper()
    command = command.encode()
    # PLAY command is padded with 1 extra byte
    command = command if command != b'PLAY' else command + b'\x01'

    data = data.to_bytes(1, 'big')
    command = b'\06' + command + data
    command = command.ljust(16, b'\0')
    print(command)
    return command

def wrap_encrypt(command:str, data:int):
    return mask_encrypt(wrap_command(command, data))

# Commands
def light(value):
    # higher values are possible and do make the mask marginally brighter, but the leds begin to flicker
    # seems unsafe
    assert 0 <= value <= 100
    return wrap_encrypt("light", value)

def speed(value):
    return wrap_encrypt("speed", value)

def image(value):
    # note, you can send values higher than 69,
    # this will load parts of the images of the animations with some format mismatch
    assert 0 <= value <= 69
    return wrap_encrypt("imag", value)

def animation(value):
    # same as image, but the mask tries to cycle through further data as well
    assert 0 <= value <= 45
    return wrap_encrypt("anim", value)

def play(value):
    return wrap_encrypt("play", value+1)

def check():
    return wrap_encrypt("chec", 1)

def upload(img_length):
    assert False
    return wrap_encrypt("dats", value)

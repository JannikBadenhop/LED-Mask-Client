from enum import Enum

max_bytes=98

class Color:
    red =   b'\xff\0\0'
    green = b'\0\xff\0'
    blue =  b'\0\0\xff'
    white = b'\xff\xff\xff'
    black = b'\0\0\0'
    _sq = "■"
    _red_sq =   f'\033[91m{_sq}\033[0m'
    _green_sq = f'\033[92m{_sq}\033[0m'
    _blue_sq =  f'\033[94m{_sq}\033[0m'
    _white_sq = f'{_sq}'
    _black_sq = f' '


def pack(data):
    package = []
    idx = 0
    for col in data:
        package.append(col)
        if len(pac) == max_bytes:
            package = len(package+1).to_bytes(1, "big")
            package = idx.to_bytes(1, "big")
            yield package
    yield package

def visualize(data):
    data = [l.replace("R", Color._red_sq) for l in data]
    data = [l.replace("G", Color._green_sq) for l in data]
    data = [l.replace("B", Color._blue_sq) for l in data]
    data = [l.replace("W", Color._white_sq) for l in data]
    data = [l.replace("X", Color._black_sq) for l in data]

    print("\n".join(data))


class Mask():
    def __init__(self):
        self.width=58
        self.height=46
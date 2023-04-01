import asyncio
from time import sleep

from bleak import BleakScanner, BLEDevice, BleakClient




class Commands(Enum):
    _key = b'\x32\x67\x2f\x79\x74\xad\x43\x45\x1d\x9c\x6c\x89\x4a\x0e\x87\x64'

    def mask_encrypt(value):
        from Crypto.Cipher import AES
        from Crypto.Cipher.AES import MODE_ECB
        cipher = AES.new(_key, MODE_ECB)
        return cipher.encrypt(value)

    def get_setimage_command(idx): 
        return mask_encrypt(b'\x06PLAY \x01' + int(idx+1).to_bytes(1,'big') + b';\x97\xf2\xf3U\xa9r\x13\x8b')

    light1=mask_encrypt(b'\x06LIGHT\x01\x01;\x97\xf2\xf3U\xa9r\x13\x8b')
    light100=mask_encrypt(b'\x06LIGHT\x01d;\x97\xf2\xf3U\xa9r\x13\x8b')
    image="IMAG"
    check="CHEC"
    speed="SPEED" 
    animation="ANIM" 
    upload="DATS"

    

async def discover():
    found_dev = []
    while True:
        devices = await BleakScanner.discover(timeout=5, return_adv=True)
        for d, k in devices.items():
            device, advert = k
            if device.name.strip() not in found_dev:
                print(d)
                print(device)
                # print(advert)
                #
                # for prop, value in device._metadata.items():
                #     print(f"{prop}: {value}")
                #
                # for prop, value in device.details["props"].items():
                #     print(f"{prop}: {value}")

            if f"{d}" not in found_dev:
                print(f"{device.name.strip()}: {device.address}")
                print(advert)
                found_dev.append(f"{d}")

class MaskClient(BleakClient):
    def __init__(self):
        super(self).__init__()

async def main():
    # await discover()
    # exit()
    print('Connecting...')
    mask = await BleakScanner.find_device_by_address('CD:DE:49:E1:69:7E')
    # mask = await BleakScanner.find_device_by_address('0000fff0-0000-1000-8000-00805f9b34fb')
    print("Success!")
    print(mask)
    client = BleakClient(mask)
    await client.connect()
    print('select 1')
    await client.write_gatt_char("d44bc439-abfd-45a2-b575-925416129600", msgs[0])
    sleep(2)
    print('select 2')
    await client.write_gatt_char("d44bc439-abfd-45a2-b575-925416129600", msgs[1])
    sleep(2)
    print('select 3')
    await client.write_gatt_char("d44bc439-abfd-45a2-b575-925416129600", msgs[2])
    sleep(2)
    await client.write_gatt_char("d44bc439-abfd-45a2-b575-925416129600", Commands.light1)
    sleep(2)
    await client.write_gatt_char("d44bc439-abfd-45a2-b575-925416129600", Commands.light100)
    sleep(2)
    await client.write_gatt_char("d44bc439-abfd-45a2-b575-925416129600", Commands.light1)

asyncio.run(main())

import asyncio
from enum import Enum
from time import sleep

from bleak import BleakScanner, BLEDevice, BleakClient

from Commands import speed, light, play, image, animation

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

# class MaskClient(BleakClient):
#     def __init__(self):
#         super(self).__init__()

async def send_command(client, command:str):
    await client.write_gatt_char("d44bc439-abfd-45a2-b575-925416129600", command)

async def main():
    # await discover()
    # exit()
    print('Connecting...')
    mask = await BleakScanner.find_device_by_address('CD:DE:49:E1:69:7E')
    print("Success!")
    print(mask)
    client = BleakClient(mask)
    await client.connect()

    # test_commands = [
    #     play(0),
    #     play(1),
    #     play(2),
    #     light(1),
    #     light(25),
    #     light(50),
    #     light(75),
    #     light(100),
    #     light(0),
    #     light(1)
    # ]

    # test_commands = [image(i) for i in range(100)]
    # test_commands = [animation(i) for i in range(80)]
    test_commands = [light(0), light(50)]

    for i, cmd in enumerate(test_commands):
        print(i)
        await send_command(client, cmd)
        sleep(.25)

asyncio.run(main())

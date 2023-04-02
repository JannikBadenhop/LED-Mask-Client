# LED-Mask-Client
This project  allows controlling the [megoo LED mask](https://www.amazon.de/dp/B08P85C5S5) over
Bluetooth Low Energy (BLE).
 Currently it is only possible to switch between different images saved on the mask.

I suspect the mask is the same as many other masks with exactly the same number of LEDs (2074) 
the same dimensions (ca. 22cm x 18cm x 5cm) and the same weight (ca. 303g).  ;)


![SimpleCount](img/count.gif?raw=true "Count up gif.")

## Getting Started

To use this project, you will need a BLE-enabled device that can run python, which not every adapter / OS supports. \
(My Win10 PC with a Bluetooth 5 adapter was unable to find the mask)

In general I would not  recommend testing BLE connections on Windows.

Also, install the requirements txt with\
``
pip install -r requirements.txt
``

## Features

- [x] Switching between images saved on the mask
- [ ] Uploading new images
- [ ] Combining uploaded images into animations
- [ ] Setting and configuring Text / Text slide animations
- [ ] An interface to draw the single Pixels (LEDs) and upload the image (hopefully possible)

## Contributing

If you would like to contribute to this project, please feel free to submit a pull request.
We welcome any contributions that improve the project or add new features.

## Thanks
- mj99 - [BLE commands](https://www.reddit.com/r/ReverseEngineering/comments/lr9xxr/help_me_figure_out_how_to_reverse_engineer_the/h14nm39/)
- shawnrancatore - [Sample code](https://github.com/shawnrancatore/shining-mask)

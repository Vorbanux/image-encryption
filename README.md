# Image encryption
This repository contains two files: a module and a console. The console is only needed for testing. The module itself is free to use. The system uses the LSB method. The module can encrypt and decrypt text from/to images.

## Working method
The module operates using the LSB method. The first pixels of the image are read, their colors (RGB) are converted to binary code, and then the character bits are distributed among them. For the red and green channels, the distribution is on the last three bits, and for the blue channel, the distribution is on the last two bits. This is how each character of the text is encrypted, and decryption proceeds similarly, but in reverse.

## Libs
* python version 3.14+
* module need pillow

### Additional

This is <b>my second public repository</b> on GitHub. Don't judge me too harshly.

Version: 2.0

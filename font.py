#!/usr/bin/env python3

from PIL import Image

im = Image.open("e71d5e896c525b1ce22808458292f0a3.png")

print("static const unsigned char _charmap[256][8] = {")

for ch in range(256):

    x_offset = (ch%16)*9
    y_offset = int(ch/16)*9

    x_offset = x_offset + 1
    y_offset = y_offset + 1 

    # print("(x, y) = (%d, %d)" % (x_offset, y_offset))

    print("\t/* %3d */ { " % ch, end='')
    # print("\t", end='')
    for y_delta in range(8):
        s = 0
        for x_delta in range(8):
            if im.getpixel(xy=(x_offset+x_delta, y_offset+y_delta))[3] == 255:
                # print("*", end='')
                s = s | (1<<(7-x_delta))
            #else:
            #    print(" ", end='')
        # print("\n", end='')
        print("0x%02x, " % s, end='')
    print("},")


print("};")

print("const unsigned char *charmap = &_charmap[0][0];")

from machine import I2C
from writer import Writer
from screen import Display
from time import sleep

# Fonts
import freesans12 as fo1
import freesansbold12 as fo2
import freeserif12 as fo3
import freeserifbold12 as fo4

WIDTH = const(128)
HEIGHT = const(64)

# Create the I2C interface.
i2c = I2C(0)
display = Display(i2c)
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

for font in [fo1, fo2, fo3, fo4]:
    display.reset()
    wri = Writer(display, font)
    # verbose = False to suppress console output
    Writer.set_textpos(display, 12, 28) 
    wri.printstring('Hello World\n')
    Writer.set_textpos(display, 24, 28)
    wri.printstring('How are you\n')
    Writer.set_textpos(display, 36, 28)
    wri.printstring('Hope all OK\n')
    display.show()
    sleep(5)


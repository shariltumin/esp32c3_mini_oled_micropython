from machine import I2C
from screen import Display

i2c = I2C(0)

print("I2C Address : "+hex(i2c.scan()[0]).upper())
print("I2C Configuration: "+str(i2c))

display = Display(i2c)
display.rotate(1)
display.fill(0)
display.contrast(255)
# This is for default 8x8 fonts
display.text("12345678",30,12)
display.text("abcdefgh",30,23)
display.text("ABCDEFGH",30,34)
display.text(">!#%&/()",30,45)
display.show()



freeze("$(PORT_DIR)/modules")
include("$(MPY_DIR)/extmod/asyncio")

# Useful networking-related packages.
require("bundle-networking")

# Require some micropython-lib modules.
require("aioespnow")
require("dht")
require("ds18x20")
require("neopixel")
require("onewire")
require("umqtt.robust")
require("umqtt.simple")
require("upysh")

# Oled 72x40 screen module and fonts
freeze('$(MPY_DIR)/extra/display', 'screen.py')
freeze('$(MPY_DIR)/extra/display', 'writer.py')
freeze('$(MPY_DIR)/extra/display', 'freesans12.py')
freeze('$(MPY_DIR)/extra/display', 'freesansbold12.py')
freeze('$(MPY_DIR)/extra/display', 'freeserif12.py')
freeze('$(MPY_DIR)/extra/display', 'freeserifbold12.py')
freeze('$(MPY_DIR)/extra/display', 'freesans8.py')
freeze('$(MPY_DIR)/extra/display', 'freesansbold8.py')
freeze('$(MPY_DIR)/extra/display', 'freeserif8.py')
freeze('$(MPY_DIR)/extra/display', 'freeserifbold8.py')



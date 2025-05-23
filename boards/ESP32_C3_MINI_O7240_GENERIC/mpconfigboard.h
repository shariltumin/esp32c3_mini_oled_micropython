// This configuration is for a generic ESP32C3 board with 4MiB (or more) of flash.

#define MICROPY_HW_BOARD_NAME               "ESP32C3 Mini Oled72x40"
#define MICROPY_HW_MCU_NAME                 "ESP32C3"

#define MICROPY_HW_I2C0_SCL                 (6)
#define MICROPY_HW_I2C0_SDA                 (5)

#define MICROPY_HW_SPI1_MOSI                (6)
#define MICROPY_HW_SPI1_MISO                (5)
#define MICROPY_HW_SPI1_SCK                 (7)


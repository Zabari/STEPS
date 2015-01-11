# Raspberry Pi Setup

### Software
Download the Raspberry Pi GPIO Drivers:

```
 sudo apt-get update
 sudo apt-get dist-upgrade
 sudo apt-get install python-rpi.gpio python3-rpi.gpio
```

### Pinout

| nrf24l01 | Raspberry Pi |
|----------|--------------|
| 1 `GND`  | 25 `GND`     |
| 2 `VCC`  | 1 `3.3v`     |
| 3 `CE`   | 15 `GPIO 22` |
| 4 `CSN`  | 24 `CE0`     |
| 5 `SCK`  | 23 `SCLK`    |
| 6 `MOSI` | 19 `MOSI`    |
| 7 `MISO` | 21 `MISO`    |
| 8        | --           |

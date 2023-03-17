#!/usr/bin/env python
from gpiozero import LED
from time import sleep
import evdev

GENO = "Genovation"
led_green = LED(8)
led_red = LED(7)



def find_device():
    """
    this function looks through different devices, and selects
    Genovation keypad, to be later used ...
    """

    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for input_port in devices:
        print("searching for keybaord input")
        if GENO in input_port.name:
            print("found genie")
            led_green.on()
            return input_port.path
        else:
            print("missing genie")
            led_red.on()
            return None

#    return None


if find_device() is None:
    print("boo")
    led_red.on()
    sleep(10)
else:
    print("baa")
    led_green.on()
    sleep(10)

#!/usr/bin/env python
from gpiozero import LED
from time import sleep
import evdev

GENO = "Genovation"
led = LED(8)
led1=LED(7)




def find_device():
    """
    this function looks through different devices, and selects
    Genovation keypad, to be later used ...
    """

    devices = [evdev.InputDevice(path) for path in evdev.list_devices()]
    for input_port in devices:
        print("searching for keybaord input")
        if GENO in input_port.name:
            print('found genie')
            led.on()
            return input_port.path
    return None


# while True:
if  find_device()==None:
     print('boo')
     led.on()
     sleep(10)
else:
     print('baa')
     led1.on()
     sleep(10)


#!/usr/bin/env python

import evdev
from evdev import categorize

device = evdev.InputDevice('/dev/input/event4')
print(device)
# device /dev/input/event4, name "Genovation", phys "usb-0000:01:00.0-1.3/input0"

for event in device.read_loop():
     print (event)
     e = categorize(event)
    print(e)
     if event.type == evdev.ecodes.EV_KEY:
         if event.value == 1:
            print('jeden')
            print ("event code", event.code)
#         print ("event value", event.value)
#         print (evdev.categorize(event))

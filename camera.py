#!/usr/bin/python

import blinkt
import config
import subprocess
import time
import gpiozero
from picamera import PiCamera
from time import sleep
from datetime import datetime as dtdatetime
from blinkt import set_pixel, set_clear_on_exit, set_all, show
from signal import pause
from gpiozero import Button

def timelapse():
    while True:
        blinkt.clear()
        blinkt.show()
        blinkt.set_pixel(7, 0, 255, 0, 0.1)
        blinkt.show()
        time.sleep(config.delay)

        blinkt.set_pixel(7, 0, 255, 0, 0.1)
        blinkt.set_pixel(6, 0, 255, 0, 0.1)
        blinkt.show()
        time.sleep(config.delay)

        blinkt.set_pixel(7, 0, 255, 0, 0.1)
        blinkt.set_pixel(6, 0, 255, 0, 0.1)
        blinkt.set_pixel(5, 0, 255, 0, 0.1)
        blinkt.show()
        time.sleep(config.delay)

        blinkt.set_pixel(7, 0, 255, 0, 0.1)
        blinkt.set_pixel(6, 0, 255, 0, 0.1)
        blinkt.set_pixel(5, 0, 255, 0, 0.1)
        blinkt.set_pixel(4, 0, 255, 0, 0.1)
        blinkt.show()
        time.sleep(config.delay)

        blinkt.set_pixel(7, 0, 255, 0, 0.1)
        blinkt.set_pixel(6, 0, 255, 0, 0.1)
        blinkt.set_pixel(5, 0, 255, 0, 0.1)
        blinkt.set_pixel(4, 0, 255, 0, 0.1)
        blinkt.set_pixel(3, 255, 140, 0, 0.1)
        blinkt.show()
        time.sleep(config.delay)        
        
        blinkt.set_pixel(7, 0, 255, 0, 0.1)
        blinkt.set_pixel(6, 0, 255, 0, 0.1)
        blinkt.set_pixel(5, 0, 255, 0, 0.1)
        blinkt.set_pixel(4, 0, 255, 0, 0.1)
        blinkt.set_pixel(3, 255, 140, 0, 0.1)
        blinkt.set_pixel(2, 255, 110, 0, 0.1)
        blinkt.show()
        time.sleep(config.delay)

        blinkt.set_pixel(7, 0, 255, 0, 0.1)
        blinkt.set_pixel(6, 0, 255, 0, 0.1)
        blinkt.set_pixel(5, 0, 255, 0, 0.1)
        blinkt.set_pixel(4, 0, 255, 0, 0.1)
        blinkt.set_pixel(3, 255, 140, 0, 0.1)
        blinkt.set_pixel(2, 255, 110, 0, 0.1)
        blinkt.set_pixel(1, 255, 69, 0, 0.1)
        blinkt.show()
        time.sleep(config.delay)
        
        blinkt.set_pixel(7, 0, 255, 0, 0.1)
        blinkt.set_pixel(6, 0, 255, 0, 0.1)
        blinkt.set_pixel(5, 0, 255, 0, 0.1)
        blinkt.set_pixel(4, 0, 255, 0, 0.1)
        blinkt.set_pixel(3, 255, 140, 0, 0.1)
        blinkt.set_pixel(2, 255, 110, 0, 0.1)
        blinkt.set_pixel(1, 255, 69, 0, 0.1)
        blinkt.set_pixel(0, 255, 0, 0, 0.1)
        blinkt.show()
        time.sleep(config.delay)
        blinkt.set_all(255, 0, 0, 0.1)
        blinkt.show()
        datetime = dtdatetime.now().isoformat()
        camera.capture('/home/pi/timelapse/%s.jpg' % datetime)
        time.sleep(0.5)
        
def hhtimelapse():
    for i in range (120):
        blinkt.clear()
        blinkt.show()
        blinkt.set_pixel(7, 0, 255, 0, 0.1)
        blinkt.show()
        time.sleep(config.hhdelay)

        blinkt.set_pixel(7, 0, 255, 0, 0.1)
        blinkt.set_pixel(6, 0, 255, 0, 0.1)
        blinkt.show()
        time.sleep(config.hhdelay)

        blinkt.set_pixel(7, 0, 255, 0, 0.1)
        blinkt.set_pixel(6, 0, 255, 0, 0.1)
        blinkt.set_pixel(5, 0, 255, 0, 0.1)
        blinkt.show()
        time.sleep(config.hhdelay)

        blinkt.set_pixel(7, 0, 255, 0, 0.1)
        blinkt.set_pixel(6, 0, 255, 0, 0.1)
        blinkt.set_pixel(5, 0, 255, 0, 0.1)
        blinkt.set_pixel(4, 0, 255, 0, 0.1)
        blinkt.show()
        time.sleep(config.hhdelay)

        blinkt.set_pixel(7, 0, 255, 0, 0.1)
        blinkt.set_pixel(6, 0, 255, 0, 0.1)
        blinkt.set_pixel(5, 0, 255, 0, 0.1)
        blinkt.set_pixel(4, 0, 255, 0, 0.1)
        blinkt.set_pixel(3, 255, 140, 0, 0.1)
        blinkt.show()
        time.sleep(config.hhdelay)        
        
        blinkt.set_pixel(7, 0, 255, 0, 0.1)
        blinkt.set_pixel(6, 0, 255, 0, 0.1)
        blinkt.set_pixel(5, 0, 255, 0, 0.1)
        blinkt.set_pixel(4, 0, 255, 0, 0.1)
        blinkt.set_pixel(3, 255, 140, 0, 0.1)
        blinkt.set_pixel(2, 255, 110, 0, 0.1)
        blinkt.show()
        time.sleep(config.hhdelay)

        blinkt.set_pixel(7, 0, 255, 0, 0.1)
        blinkt.set_pixel(6, 0, 255, 0, 0.1)
        blinkt.set_pixel(5, 0, 255, 0, 0.1)
        blinkt.set_pixel(4, 0, 255, 0, 0.1)
        blinkt.set_pixel(3, 255, 140, 0, 0.1)
        blinkt.set_pixel(2, 255, 110, 0, 0.1)
        blinkt.set_pixel(1, 255, 69, 0, 0.1)
        blinkt.show()
        time.sleep(config.hhdelay)
        
        blinkt.set_pixel(7, 0, 255, 0, 0.1)
        blinkt.set_pixel(6, 0, 255, 0, 0.1)
        blinkt.set_pixel(5, 0, 255, 0, 0.1)
        blinkt.set_pixel(4, 0, 255, 0, 0.1)
        blinkt.set_pixel(3, 255, 140, 0, 0.1)
        blinkt.set_pixel(2, 255, 110, 0, 0.1)
        blinkt.set_pixel(1, 255, 69, 0, 0.1)
        blinkt.set_pixel(0, 255, 0, 0, 0.1)
        blinkt.show()
        time.sleep(config.hhdelay)
        blinkt.set_all(255, 0, 0, 0.1)
        blinkt.show()
        datetime = dtdatetime.now().isoformat()
        camera.capture('/home/pi/timelapse/%s.jpg' % datetime)
        time.sleep(0.5)

def snap():
    blinkt.set_all(255, 0, 0, 0.1)
    blinkt.show()
    datetime = dtdatetime.now().isoformat()
    camera.capture('/home/pi/snaps/%s.jpg' % datetime)
    time.sleep(0.5)
    blinkt.set_all(255, 255, 255, 0.1)
    blinkt.show()

camera = PiCamera()
set_clear_on_exit()
tlstart_button = Button(17)
snap_button = Button(22)
tlhh_button = Button(27)

blinkt.set_all(255, 255, 255, 0.1)
blinkt.show()
tlstart_button.when_pressed = timelapse
tlhh_button.when_pressed = hhtimelapse
snap_button.when_pressed = snap
pause()

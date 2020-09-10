#!/usr/bin/env python

# fanTest v.1
# Carboni Corporation 2020- All right reserved https://www.carboni.ch
# Author: Carboni Davide
# @copyright Copyright (c) 2020, Carboni Software, Inc.
# @license AGPL-3.0
#
# This code is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License, version 3,
# as published by the Free Software Foundation.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License, version 3,
# along with this program.  If not, see <http://www.gnu.org/licenses/>

# Fan speed test software for Raspberry Pi

import os
from time import sleep
import signal
import sys
import RPi.GPIO as GPIO
from fanConfig import *

def gpio_setup():
        GPIO.setmode(GPIO.BCM)
	GPIO.setwarnings(False)
	return()

def gpio_clean():
    for fan_gpio_pin in FAN_GPIO_PINS:
        GPIO.setup(fan_gpio_pin, GPIO.OUT)
        GPIO.cleanup(fan_gpio_pin)
    return()

def increase():
        print("----------------------")
        print("STEP 1: FAN INCREASING")
        print("----------------------")

        for fan_level, gpio_pin in enumerate(FAN_GPIO_PINS, start= 1):
                print("Level %s is ON" % fan_level)
                GPIO.setup(gpio_pin, GPIO.OUT)
	        GPIO.output(gpio_pin, 1)
                sleep(3)

	return()

def decrease():
        print("----------------------")
        print("STEP 2: FAN DECREASING")
        print("----------------------")
        for fan_level, gpio_pin in enumerate(FAN_GPIO_PINS, start= 1):
                print("Level %s is OFF" % fan_level)
                GPIO.cleanup(gpio_pin)
                sleep(3)

	return()

gpio_setup()
gpio_clean()

try:
        increase()
        decrease()
except:
	gpio_clean()

#!/usr/bin/python

import time
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

#GPIO Setup
GPIO.setup(16,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(21,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#Pin Setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

#Define Column and Row size (16x2 LCD)
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

def lcdClear():
    for counter in range(5):
        lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
        lcd.clear()

while True:
    if((GPIO.input(16) == True) and (GPIO.input(21) == True)):
        lcdClear()
        lcd.message("Power Consumed:\n%f W" % 500)
    elif((GPIO.input(16) == True) and (GPIO.input(21) == False)):
        lcdClear()
        lcd.message("Power Consumed:\n%f W" % 1500)
    else:
        lcdClear()
        lcd.message("Power Consumed:\n0 W")
    time.sleep(1)
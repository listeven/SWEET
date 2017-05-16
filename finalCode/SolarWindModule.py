#!/usr/bin/python

from bluetooth import *
import spidev
import time
import Adafruit_CharLCD as LCD
import RPi.GPIO as GPIO

#GPIO Setup

GPIO.setmode(GPIO.BCM)

GPIO.setup(4, GPIO.IN)
GPIO.setup(16, GPIO.OUT)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)
NUM_CYCLES = 10

GPIO.output(16, 0)
GPIO.output(20, 0)
GPIO.output(21, 0)

#Define Vars
delay = 0.5
adc_channel = 0
done = True
solarDone = True
totalPow = 0
frequency = 0
solarPower = 0
windPower = 0

#Pin Setup
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

lcd2_rs = 12
lcd2_en = 5
lcd2_d4 = 6
lcd2_d5 = 13
lcd2_d6 = 19
lcd2_d7 = 26
lcd2_backlight = 2

#Define Column and Row size (16x2 LCD)
lcd_columns = 16
lcd_rows = 2

lcd2_columns = 16
lcd2_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
lcd2 = LCD.Adafruit_CharLCD(lcd2_rs, lcd2_en, lcd2_d4, lcd2_d5, lcd2_d6, lcd2_d7, lcd2_columns, lcd2_rows, lcd2_backlight)
lcd.clear()
lcd2.clear()

if sys.version < '3':
    input = raw_input
    
addr = None

if len(sys.argv) < 2:
    print("No device specified. Searching.")
else:
    addr = sys.argv[1]
    print("Searching on %s" % addr)
    
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
service_matches = find_service(uuid = uuid, address = addr)
tries = 0
while(len(service_matches) == 0) and (tries < 5):
    service_matches = find_service(uuid = uuid, address = addr)
    tries+= 1
if(len(service_matches > 0):
    first_match = service_matches[0]
    port = first_match["port"]
    name = first_match["name"]
    host = first_match["host"]
    sock = BluetoothSocket(RFCOMM)
    sock.connect((host,port))
    
spi = spidev.SpiDev()
spi.open(0,0)
spi.max_speed_hz = 200000

def readADC(adcnum):
    if adcnum > 3 or adcnum < 0:
        return -1
    r = spi.xfer2([1, 8 + adcnum << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data

def windEvent():
    global done
    if done:
        done = False
        readWind()
        done = True
    return

def readWind():
    #Wind Stuff
    global totalPow, frequency, solarPower, windPower
    start = time.time()
    for impulse_count in range(NUM_CYCLES):
        GPIO.wait_for_edge(4, GPIO.FALLING, timeout = 100)
    duration = time.time() - start #seconds to run for loop
    frequency = NUM_CYCLES / duration #in Hz
    time.sleep(.5)
    if(frequency <= 11):
        GPIO.output(16,0)
        GPIO.output(20,0)
        GPIO.output(21,0)
    elif ((frequency > 11) and (frequency <= 1000)):
        GPIO.output(16,1)
        GPIO.output(20, 0)
        GPIO.output(21, 0)
    elif ((frequency <= 2000) and (frequency > 1000)):
        GPIO.output(16, 1)
        GPIO.output(20, 1)
        GPIO.output(21, 0)
    elif (frequency > 2000):
        GPIO.output(16, 1)
        GPIO.output(20, 1)
        GPIO.output(21, 1)
    clearCount = 0
    while(clearCount < 5):
        lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
        lcd.clear()
        clearCount += 1
    windPower = frequency * 1.25
    if(frequency <= 11):
        lcd.message("Power Generated:\n0 W")
        totalPow = solarPower
    else:
        tempStr = "Power Generated:\n%.5g W" % windPower
        lcd.message(tempStr)
        totalPow = solarPower + windPower
    time.sleep(1)
    
def solarEvent():
    global solarDone
    if solarDone:
        solarDone = False
        readSolar()
        solarDone = True
    return

def readSolar():
    #Solar
    global solarPower
    adc_value = 0
    for adcCount in range(10):
        adc_value += readADC(adc_channel)
    avgADC = adc_value /10
    measVolt = (avgADC*3.3)/1025.0
    inpVolt = measVolt * 5.99
    current = .5 * inpVolt
    solarPower = current * inpVolt * 3000
    clearCountS = 0
    while(clearCountS < 5):
        lcd2 = LCD.Adafruit_CharLCD(lcd2_rs, lcd2_en, lcd2_d4, lcd2_d5, lcd2_d6, lcd2_d7, lcd2_columns, lcd2_rows, lcd2_backlight)
        lcd2.clear()
        clearCountS += 1
    lcd2.message("Power Generated:\n%f W" % solarPower)
    time.sleep(1)
try:    
    while True:
        GPIO.output(16,0)
        GPIO.output(20,0)
        GPIO.output(21,0)
        solarEvent()
        windEvent()
        if(len(service_matches) > 0):
            powerData = str(totalPow)
            sock.send(powerData)
        time.sleep(1)
        lcd2.clear()
except KeyboardInterrupt:
    if(len(service_matches) > 0):
        sock.close()
    

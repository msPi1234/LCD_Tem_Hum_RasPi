#!/usr/bin/env python3
# run as python3 myLCD.py

# Created by https://github.com/msPi1234
# Created in December 2020


# Libraries for time and date
import time
import datetime

# Library for Garbage collector, delete memory
import gc
num=0

# Library for LCD char
import Adafruit_CharLCD as LCD

# Library for sensor DHT22
import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 7 #4

# Raspberry Pi setup PIN
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

# Define LCD column and row size for 16x2 LCD
lcd_columns = 16
lcd_rows = 2

lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)

while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
	
        lcd.clear()
        text2=datetime.datetime.now()
        lcd.message(text2.strftime("DATE: %Y-%m-%d\nTIME: %H:%M:%S"))
        time.sleep(1)

        lcd.clear()
        tem=(format(temperature))
        hum=(format(humidity))
        t=tem[0:5]
        h=hum[0:5]
        text=("TEMP: " + t + "\nHUM:  " + h + "\n")
        lcd.message(text)
        time.sleep(1)

        num=num+1
        if num < 10:
            gc.collect()
    else:
        print("Failed to retrieve data from humidity sensor")

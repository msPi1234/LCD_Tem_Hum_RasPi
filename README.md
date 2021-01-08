# LCD2x16_DHT22_RaspberryPI

This project is compilate codes for Python3.
Goal was show Temperature, Huminidity, Time and Date in real time on LCD 2x16 with sensor DHT22.

# Used hardware and software

For right running we must do some three easy steps.

# First steps - setup DHT sensor

sudo apt-get update
sudo apt-get upgrade

Next you may follow this steps on link for install DHT's library:
https://github.com/adafruit/Adafruit_Python_DHT/blob/master/README.md

if you don't want clicking on the link above, follow this steps if you want use only Python3:
sudo apt-get install python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo pip3 install Adafruit_DHT

Now download <a href="https://github.com/adafruit/Adafruit_Python_DHT/releases">GitHub releases page</a> and follow next steps:

You may download direct from command line (this version may be different, check version on source webpage):
wget https://github.com/adafruit/Adafruit_Python_DHT/archive/1.4.1.zip
sudo unzip 1.4.1.zip 

cd Adafruit_Python_DHT-1.4.1
sudo python3 setup.py install

# Second steps - setup LCD display

Next you may follow this steps on link for install LCD's library:
https://github.com/pimylifeup/Adafruit_Python_CharLCD

I will inspirated too from this good <a href="https://pimylifeup.com/raspberry-pi-lcd-16x2/">web page</a>.

If you don't want clicking on the links above, follow this steps if you want use only Python3.
Now download <a href="https://github.com/pimylifeup/Adafruit_Python_CharLCD">GitHub releases page</a> and follow next steps:

Direct download from command line:
wget https://github.com/pimylifeup/Adafruit_Python_CharLCD/archive/master.zip
sudo unzip master.zip
cd Adafruit_Python_CharLCD-master/

sudo pip install RPi.GPIO

If you want use Python3, you must install for this steps:
sudo python3 setup.py install

Important: Don't do this sudo python setup.py install

sudo pip3 install Adafruit-CharLCD
sudo pip3 install adafruit-circuitpython-charlcd

Ok, we go try example code.
First you must change GPIO ports for those what you will be use as own ports on Raspberry Pi. 
For example: 
sudo vi /home/pi/Adafruit_Python_CahrLCD-master/example/char_lcd.py change on:
lcd_rs = 25
lcd_en = 24
lcd_d4 = 23
lcd_d5 = 17
lcd_d6 = 18
lcd_d7 = 22
lcd_backlight = 2

If you try 
python /home/pi/Adafruit_Python_CahrLCD-master/example/char_lcd.py
you maybe show this error:

Traceback (most recent call last):
  File "char_lcd.py", line 5, in <module>
    import Adafruit_CharLCD as LCD
ImportError: No module named Adafruit_CharLCD

Don't worry, next steps are:
sudo pip install Adafruit-CharLCD

Now change first line in /home/pi/Adafruit_Python_CahrLCD-master/example/char_lcd.py:
#!/usr/bin/python3

try run 
python3 char_lcd.py

# Are you Happy now? 
:) Because I am!

# Third steps - run own code

Here is final code:

#!/usr/bin/env python3
# run as python3 myLCD.py

#libraries for time and date
import time
import datetime

#library for LCD char
import Adafruit_CharLCD as LCD

#library for sensor DHT22
import Adafruit_DHT
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 7 #4

# Raspberry Pi pin setup
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
        tem=(format(temperature))
        hum=(format(humidity))
        t=tem[0:5]
        h=hum[0:5]
        text=("Temp: " + t + "\nHum: " + h + "\n")
        lcd.message(text)
        time.sleep(4.0)
        lcd.clear()
        now=datetime.datetime.now()
        lcd.message(now.strftime("DATE:%Y-%m-%d\nTIME:%H:%M:%S\n"))
        time.sleep(4.0)
        lcd.clear()
    else:
        print("Failed to retrieve data from humidity sensor")

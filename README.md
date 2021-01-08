# LCD2x16_DHT22_RaspberryPI

This project is compilate codes for Python3.<br>
Goal was show Temperature, Huminidity, Time and Date in real time on LCD 2x16 with sensor DHT22.

# Used hardware and software

For right running we must do some three easy steps.

# First steps - setup DHT sensor

sudo apt-get update<br>
sudo apt-get upgrade

Next you may follow this steps on link for install DHT's library:<br>
https://github.com/adafruit/Adafruit_Python_DHT/blob/master/README.md

If you don't want clicking on the link above, follow this steps if you want use only Python3:<br>
sudo apt-get install python3-pip<br>
sudo python3 -m pip install --upgrade pip setuptools wheel<br>
sudo pip3 install Adafruit_DHT<br><br>

Now download <a href="https://github.com/adafruit/Adafruit_Python_DHT/releases">GitHub releases page</a> and follow next steps:<br><br>

You may download direct from command line (this version may be different, check version on source webpage):<br>
wget https://github.com/adafruit/Adafruit_Python_DHT/archive/1.4.1.zip<br>
sudo unzip 1.4.1.zip<br><br>

cd Adafruit_Python_DHT-1.4.1<br>
sudo python3 setup.py install

# Second steps - setup LCD display

Next you may follow this steps on link for install LCD's library:<br>
https://github.com/pimylifeup/Adafruit_Python_CharLCD<br><br>

I will inspirated too from this good <a href="https://pimylifeup.com/raspberry-pi-lcd-16x2/">web page</a>.<br><br>

If you don't want clicking on the links above, follow this steps if you want use only Python3.<br>
Now download <a href="https://github.com/pimylifeup/Adafruit_Python_CharLCD">GitHub releases page</a> and follow next steps:<br><br>

Direct download from command line:<br>
wget https://github.com/pimylifeup/Adafruit_Python_CharLCD/archive/master.zip<br>
sudo unzip master.zip<br>
cd Adafruit_Python_CharLCD-master/<br><br>

sudo pip install RPi.GPIO<br><br>

If you want use Python3, you must install for this steps:<br>
sudo python3 setup.py install<br><br>

Important: Don't do this sudo python setup.py install<br><br>

sudo pip3 install Adafruit-CharLCD<br>
sudo pip3 install adafruit-circuitpython-charlcd<br><br>

Ok, we go try example code.<br>
First you must change GPIO ports for those what you will be use as own ports on Raspberry Pi. <br>
For example: <br>
sudo vi /home/pi/Adafruit_Python_CahrLCD-master/example/char_lcd.py change on:<br>
lcd_rs = 25<br>
lcd_en = 24<br>
lcd_d4 = 23<br>
lcd_d5 = 17<br>
lcd_d6 = 18<br>
lcd_d7 = 22<br>
lcd_backlight = 2<br><br>

If you try <br>
python /home/pi/Adafruit_Python_CahrLCD-master/example/char_lcd.py<br>
you maybe show this error:<br><br>

Traceback (most recent call last):<br>
  File "char_lcd.py", line 5, in <module><br>
    import Adafruit_CharLCD as LCD<br>
ImportError: No module named Adafruit_CharLCD<br><br>

Don't worry, next steps are:<br>
sudo pip install Adafruit-CharLCD<br><br>

Now change first line in /home/pi/Adafruit_Python_CahrLCD-master/example/char_lcd.py:<br>
#!/usr/bin/python3<br><br>

try run<br>
python3 char_lcd.py<br><br>

# Are you Happy now? 
:) Because I am!

# Third steps - run own code

You may use my source code from this page.

OK, if you use my own code, please let's me know how it's running. 
If you change anything let's me know.

# Automation
You maybe setup automatic run script and show data on LCD, so, do this:

crontab -l

and now type this on last row:
* * * * * python3 /home/pi/myLCD.py
save file and reboot Raspberry Pi:
sudo init 6 

Now data will showing automatic after start Raspberry Pi. 

Thanks for reading here.

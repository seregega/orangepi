from RPLCD.i2c import CharLCD
import datetime
import psutil
import time

lcd1 = CharLCD(i2c_expander='PCF8574', address=0x22, port=0,
              cols=20, rows=4, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)
lcd1.clear()
lcd1.cursor_pos=(0, 0)
lcd1.write_string("Current Temperature ")
lcd1.cursor_pos=(2, 0)
lcd1.write_string("Current  Datetime   ")

lcd2 = CharLCD(i2c_expander='PCF8574', address=0x20, port=0,
              cols=20, rows=4, dotsize=8,
              charmap='A02',
              auto_linebreaks=True,
              backlight_enabled=True)
lcd2.clear()
lcd2.cursor_pos=(0, 0)
lcd2.write_string("Current Load        ")
lcd2.cursor_pos=(2, 0)
lcd2.write_string("Current Memory      ")

while True:
        temp=psutil.sensors_temperatures(fahrenheit=False)['cpu_thermal'][0][1]
        timer=datetime.datetime.today().strftime("%Y-%m-%d  %H:%M:%S")
        Load=psutil.cpu_percent(interval=None, percpu=True)
        Memory=psutil.virtual_memory()[2]
        lcd1.cursor_pos=(1, 7)
        lcd1.write_string(        str(temp)     )
        lcd1.cursor_pos=(3, 0)
        lcd1.write_string(timer)
        lcd2.cursor_pos=(1, 0)
        lcd2.write_string(str(Load))
        lcd2.cursor_pos=(3, 7)
        lcd2.write_string(str(Memory))
        lcd2.write_string('%')
        time.sleep(0.4)

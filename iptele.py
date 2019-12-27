
### coding: utf-8

#encoding=utf-8
import unicodedata
import codecs
import time
import random
import datetime
import telepot
import sys
import os
import time
import urllib2
import socket
import subprocess
import logging
import RPi.GPIO as GPIO

logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')
led1=5
led2=6
led3=12
led4=13
led5=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)
GPIO.setup(led3,GPIO.OUT)
GPIO.setup(led4,GPIO.OUT)
GPIO.setup(led5,GPIO.OUT)
#sensor = BMP085.BMP085()

#import logging log_name = 'log_sends_notifications'
#logging.basicConfig(filename=log_name,level=logging.DEBUG, format='%(asctime)s %(message)s')
"""
After **inserting token** in the source code, run it:
```
$ python2.7 diceyclock.py
```
[Here is a tutorial](http://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/)
teaching you how to setup a bot on Raspberry Pi. This simple bot does nothing
but accepts two commands:
- `/roll` - reply with a random integer between 1 and 6, like rolling a dice.
- `/time` - reply with the current time, like a clock.
"""
#def loop(msg):
#    p=(sensor.read_temperature())
#    while true:
#      if p == 26 :
#       bot.sendMessage(42433085,'temp is going up2')
#      elif p < 26 :
#       bot.sendMessage(42433085,'temp is going up3')   
def handle(msg) :
   # content_type = msg['photo']
#, chat_type, chat_id = telepot.glance(msg)
   # bot.getFile('filde_id')
    hostname = "google.com" #example
    response = os.system("ping -c 1 " + hostname)
    chat_id = msg['chat']['id']
   # chat_u  = msg['chat']['username']
    command = msg['text']
    arg='ip route list'
#    temp = os.system("/opt/vc/bin/vcgencmd measure_temp").read()
    p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
    data = p.communicate()
    split_data = data[0].split()
    ipaddr = split_data[split_data.index('src')+1] 
    extipaddr = urllib2.urlopen("http://icanhazip.com").read()
   ##### A = ('Temp = {0:0.2f} *C'.format(sensor.read_temperature()))
   # B = ('Pressure = {0:0.2f} Pa'.format(sensor.read_pressure()))
   ##### C = ('Altitude = {0:0.2f} m'.format(sensor.read_altitude()))
   ##### x=(sensor.read_temperature())
   # bot.sendMessage(42433085,'im online')
   # f = open('file.txt', 'wb')
   # f.write(chat_id)
   # data = chat_id
    print 'Got command: %s' % command
   # print chat_id
    text_file = codecs.open("k.txt", "a","utf-8-sig")
    text_file.write(str(chat_id)+'\n')
    text_file.write(str(command) + '\n')
    #file.close()
   # getFile(self, file_id):
   # p = _strip(locals())
   # return self._api_request('getFile", _rectify(p))
    #    bot.sendMessage(42433085,'temp is going up')

    if command == '/test':
	if chat_id==438378601 or chat_id==384010640:
           if response == 0:
              bot.sendMessage(chat_id, 'I am connected to the Internet!')

               #led
    elif command=='/1on':
       	if chat_id==438378601 or chat_id==384010640:
       	    GPIO.output(led1,GPIO.HIGH)
            bot.sendMessage(chat_id,'LED 1 is on!')
    elif command=='/1off':
       	if chat_id==438378601 or chat_id==384010640:
       	    GPIO.output(led1,GPIO.LOW)
     	    bot.sendMessage(chat_id,'LED 1 is off!')
    elif command=='/2on':
       	if chat_id==438378601 or chat_id==384010640:
       	    GPIO.output(led2,GPIO.HIGH)
       	    bot.sendMessage(chat_id,'LED 2 is on!')
    elif command=='/2off':
       	if chat_id==438378601 or chat_id==384010640:
            GPIO.output(led2,GPIO.LOW)
            bot.sendMessage(chat_id,'LED 2 is off!')
    elif command=='/3on':
       	if chat_id==438378601 or chat_id==384010640:
            GPIO.output(led3,GPIO.HIGH)
            bot.sendMessage(chat_id,'LED 3 is on!')
    elif command=='/3off':
       	if chat_id==438378601 or chat_id==384010640:
            GPIO.output(led3,GPIO.LOW)
            bot.sendMessage(chat_id,'LED 3 is off!')
    elif command=='/4on':
       	if chat_id==438378601 or chat_id==384010640:
            GPIO.output(led4,GPIO.HIGH)
            bot.sendMessage(chat_id,'LED 4 is on!')
    elif command=='/4off':
       	if chat_id==438378601 or chat_id==384010640:
            GPIO.output(led4,GPIO.LOW)
            bot.sendMessage(chat_id,'LED 4 is off!')
    elif command=='/5on':
       	if chat_id==438378601 or chat_id==384010640:
            GPIO.output(led5,GPIO.HIGH)
            bot.sendMessage(chat_id,'LED 5 is on!')
    elif command=='/5off':
       	if chat_id==438378601 or chat_id==384010640:
            GPIO.output(led5,GPIO.LOW)
            bot.sendMessage(chat_id,'LED 5 is off!')
    elif command=='/alloff':
       	if chat_id==438378601 or chat_id==384010640:
            GPIO.output(led1,GPIO.LOW)
            GPIO.output(led2,GPIO.LOW)
            GPIO.output(led3,GPIO.LOW)
            GPIO.output(led4,GPIO.LOW)
            GPIO.output(led5,GPIO.LOW)
            bot.sendMessage(chat_id,'Boss all the lights are off!')
    elif command=='/allon':
       	if chat_id==438378601 or chat_id==384010640:
            GPIO.output(led1,GPIO.HIGH)
            GPIO.output(led2,GPIO.HIGH)
            GPIO.output(led3,GPIO.HIGH)
            GPIO.output(led4,GPIO.HIGH)
            GPIO.output(led5,GPIO.HIGH)
            bot.sendMessage(chat_id,'Boss all the lights are on!')

    elif command == '/ip':
         if chat_id==438378601 or chat_id==384010640:	#you can use your chat id for more secure commands
            bot.sendMessage(chat_id, ipaddr)
    elif command == '/ipex':
        if chat_id==438378601 or chat_id==384010640:
            bot.sendMessage(chat_id, extipaddr)
    elif command == '/status':
	if chat_id==438378601 or chat_id==384010640:
            bot.sendMessage(chat_id, chat_id)
    elif command == '/start':
        if chat_id==438378601 or chat_id==384010640:
            bot.sendMessage(chat_id, 'Hi Boss I am ready for your commands')
    elif command == '/poweroff':
        if chat_id==438378601 or chat_id==384010640:
            bot.sendMessage(chat_id,'Goodbye Boss!')
            os.system('sudo poweroff') 
    elif command == '/restart':
        if chat_id==438378601 or chat_id==384010640:
            bot.sendMessage(chat_id,'I am rebooting myself Boss!')
            os.system('sudo reboot')
    elif command == '/time':
        if chat_id==438378601 or chat_id==384010640:
            bot.sendMessage(chat_id, str(datetime.datetime.now()))
     #  if command == '/temp':
       #     bot.sendMessage(chat_id,temp)
    elif command == 'Pic':
        if chat_id==438378601 or chat_id==384010640:
            bot.sendMessage(chat_id, str(datetime.datetime.now()))
            os.system("raspistill -o image.jpg")
            #os.system("fswebcam image.jpg")		for webcam
            time.sleep(5)
            bot.sendPhoto(chat_id, ('image.jpg', open('image.jpg', 'rb')), caption=str(datetime.datetime.now()))
    elif command == 'Video':
        if chat_id==438378601 or chat_id==384010640:
            bot.sendMessage(chat_id, str(datetime.datetime.now()))
            os.system("sudo rm video.h264")
            os.system("sudo rm video.mp4")
            os.system("raspivid -o video.h264 -t 10000")
            time.sleep(5)
            os.system("MP4Box -add video.h264 video.mp4")
            time.sleep(5)
            bot.sendVideo(chat_id, ('video.mp4', open('video.mp4', 'rb')),duration=10,caption=str(datetime.datetime.now()))

       # text_file = open("k.txt", "w")
  #  if content_type == 'photo':
      #  bot.download_file(msg['photo'][-1]['file_id'], './file.png')
       # text_file.write(data)text_file.write(str(command)+'\n')
bot = telepot.Bot('enter your bot token')
bot.message_loop(handle)
#bot.sendMessage(42433085,'i m online sir')
#file = open('k.txt', 'w')
#file.write(data)
#text_file = open("k.txt", "w")
#text_file.write(chat_id)
print 'I am listening ...'
#print (chat_id)
while 1:
    time.sleep(10) 


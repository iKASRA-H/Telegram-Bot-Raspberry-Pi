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
import xlrd

file_location="./fruits.xlsx"
workbook=xlrd.open_workbook(file_location)
sheet=workbook.sheet_by_index(0)

i=0

logging.basicConfig(filename='example.log',level=logging.DEBUG)
logging.debug('This message should go to the log file')
logging.info('So should this')
logging.warning('And this, too')

   
def handle(msg) :
    global i
    content_type, chat_type, chat_id = telepot.glance(msg)

    hostname = "google.com" #example
    response = os.system("ping -c 1 " + hostname)
    chat_id = msg['chat']['id']
    arg='ip route list'

    p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
    data = p.communicate()
    split_data = data[0].split()
    ipaddr = split_data[split_data.index('src')+1] 
    extipaddr = urllib2.urlopen("http://icanhazip.com").read()
   
    text_file = codecs.open("k.txt", "a","utf-8-sig")
    text_file.write(str(chat_id)+'\n')
    
    if content_type == 'photo':
        if chat_id==your own chat id:
            bot.download_file(msg['photo'][-1]['file_id'], './file.png')
            bot.sendPhoto(chat_id, ('file.png', open('file.png', 'rb')), caption= sheet.cell_value(i,0)+"\n"+"channel id")
            i+=1
            print(i)
            
bot = telepot.Bot('Your bot token')
bot.message_loop(handle)
print 'I am listening ...'
while 1:
    time.sleep(10) 

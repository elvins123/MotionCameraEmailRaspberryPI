from picamera import PiCamera
import time
import sys
import time
import random
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders



pir = MotionSensor(4)

camera = PiCamera()

filename = "intruder.jpg"
pir.wait_for_motion()
print("Motion Detected")
camera.capture(filename)
time.sleep(1)
pir.wait_for_no_motion()

email_user = 'enter email here'
email_password = ‘place your email password here’
email_send = 'enter email here'

subject = 'Python'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'The Raspberry Pi has detected motion'
msg.attach(MIMEText(body,'plain'))

filename='intruder.jpg'
attachment  =open(filename,'rb')


part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)

server.sendmail(email_user,email_send,text)
server.quit()



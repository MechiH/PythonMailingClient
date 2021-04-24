import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart


server =smtplib.SMTP_SSL('smtp.gmail.com', 465) # define the server

server.ehlo() # start the server 

server.login('YOUR_EMAIL','YOUR_PASSWORD') # login to your account

msg = MIMEMultipart()
msg['From']='HoussemMechi'
msg['To']='RECEIVER_EMAIL'
msg['Subject']= 'Test From My ClientMailing'

with open('URL_TO_TEXT/msg.txt','r') as f :
    message = f.read()
msg.attach(MIMEText(message,'plain')) # we are not adding the text as an attachement but as a body

filename = 'URL_TO_IMAGE/code.png'

attachement=open(filename ,'rb')# rb = readbinary

p=MIMEBase('application','octet-stream')

p.set_payload(attachement.read())

encoders.encode_base64(p) #encode image
p.add_header('Content-Disposition',f'attachement; filename={filename}')# add a header to p
msg.attach(p) # add the payload to the message

text=msg.as_string()
server.sendmail('YOUR_EMAIL','RECEIVER_EMAIL',text)

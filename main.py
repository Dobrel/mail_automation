from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
from sys import argv
import csv

to=[]

#stabilirea conexiunii prin smtp
#adaugarea criptarii TLS
s=smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()
s.starttls()

#login
s.login(argv[3],argv[4])

def message(sub,text):
    msg=MIMEMultipart()
    msg['Subject']=sub
    msg.attach(MIMEText(text))

    return msg

#deschiderea fisierul cu cotinutul mail-ului
with open(argv[1]) as f:
    txt=f.read()

#adaug subiect mail-ului
#adaug continutul mail-ului
msg=message(argv[5],txt)

#trimit mail-ul si inchid conexiunea
with open(argv[2]) as g:
    r=csv.reader(g)
    for i in r:
        to.append(i)

s.sendmail(from_addr=argv[3],to_addrs=to,msg=msg.as_string())
s.quit()
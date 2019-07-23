#!/usr/bin/python		
		
from email.mime.text import MIMEText		
from email.mime.multipart import MIMEMultipart		
import smtplib, mimetypes, email.mime.application
		
mail = smtplib.SMTP('smtp.cosng.net')		
		
msg = MIMEMultipart()		
msg['Subject'] = 'Again test message'		
msg['From'] = "deepakXXXX@example.com"		
msg['To'] = "deepYYYY@example.com"		
		
txt = MIMEText('Please find today monitoring data.')		
msg.attach(txt)		
		
filename = 'output.txt'		
with open(filename, 'rb') as f:	
        attach = email.mime.application.MIMEApplication(f.read(),_subtype="txt")	
		
attach.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(attach)		
mail.sendmail("deepakXXXX@example.com",	"deepkYYYY@example.com", msg.as_string())
mail.close()		

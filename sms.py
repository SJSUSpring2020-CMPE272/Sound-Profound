import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Sender email
email = "cmpe272project2020@gmail.com"
password = "CMPE@272"

#reciever number and email address
sms_gateway = '5855246544@tmomail.net'  #tmomail.net is used for tmobile numbers
receiver_email = "namratha.bhat@sjsu.edu"

# Using smtp server we use is gmail smtp server ( the port comes by default with the gmail server)
smtp = "smtp.gmail.com" 
port = 587

#what we want the body and subject contents to be
subject_content="ALERT\n"
body_content="Gunshot sound heard!!\n"

#starts pythons email server
server = smtplib.SMTP(smtp,port)
server.starttls()

#login
server.login(email,password)

# To send sms text message
textmsg = MIMEMultipart()
textmsg['From'] = "SOUND PROFOUND"
textmsg['To'] = sms_gateway
textmsg['Subject'] = subject_content
body = body_content
textmsg.attach(MIMEText(body, 'plain'))
sms = textmsg.as_string()
server.sendmail(email,sms_gateway,sms)

# Send Email
emailMessage = MIMEMultipart()
emailMessage['From'] = "SOUND PROFOUND"
emailMessage['To'] = receiver_email
emailMessage['Subject'] = subject_content
body = body_content
emailMessage.attach(MIMEText(body, 'plain'))
mailAlert = emailMessage.as_string()
server.sendmail(email,receiver_email,mailAlert)

server.quit()
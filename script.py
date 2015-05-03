import smtplib

def sendEmail(FROM, TO, CC, SUBJECT, TEXT, UN, PW):
    message = '''From: %s
To: %s
CC: %s
Subject: %s
    
%s''' % (FROM, ", ".join(TO), CC, SUBJECT, TEXT)
    print(message)
    server = smtplib.SMTP('smtp.gmail.com', 587) # SMTP
    server.ehlo()
    server.starttls()
    server.login(UN, PW)
    server.sendmail(FROM, TO, message)
    server.quit()

FROM = 'Me' # Sender's Name
TO = [] # List of addresses to send to
CC = ""
SUBJECT = "Hello!" # Standard email subject
TEXT = "This message was sent with Python's smtplib."

username = "" # gmail username
password = "" # gmail password

sendEmail(FROM, TO, CC, SUBJECT, TEXT, username, password)

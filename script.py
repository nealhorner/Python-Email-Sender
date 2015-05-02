import smtplib

FROM = 'Me' # Sender's Name
TO = [] # List of addresses to send to. Ex. TO = ["example@example.com"]
SUBJECT = "Hello!" # Standard email subject
TEXT = "This message was sent with Python's smtplib."

message = """\
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

username = "" # gmail username
password = "" # gmail password

server = smtplib.SMTP('smtp.gmail.com', 587) # SMTP connection to gmail
server.ehlo()
server.starttls()
server.login(username, password)
server.sendmail(FROM, TO, message)
server.quit()

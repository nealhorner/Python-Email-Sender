import smtplib

def send(FROM,TO,SUBJECT,TEXT,SERVICE,PORT,USERNAME,PASSWORD):
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s""" % (FROM, ", ".join(TO),SUBJECT,TEXT)
    server = smtplib.SMTP(SERVICE, PORT)
    server.ehlo()
    server.starttls()
    server.login(USERNAME, PASSWORD)
    server.sendmail(FROM,TO,message)
    server.quit()

# Example
send("Your Name",["thenealhorner@gmail.com"],"Subject","Text","smtp.gmail.com",587,"server27314","encryption")

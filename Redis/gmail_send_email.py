import smtplib

class Gmail(object):
    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        session = smtplib.SMTP(self.server, self.port)        
        session.ehlo()
        session.starttls()
        session.ehlo
        session.login(self.email, self.password)
        self.session = session

    def send_message(self,toemail,subject, body):
        self.session.sendmail(
            self.email,
            toemail,
            body)


gm = Gmail('Email', 'Password')
gm.send_message("ToEmail",'Subject', 'Message')

#Go to this link and select Turn On
#https://www.google.com/settings/security/lesssecureapps
#https://stackoverflow.com/questions/26852128/smtpauthenticationerror-when-sending-mail-using-gmail-and-python

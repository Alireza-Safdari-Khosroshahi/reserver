import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mail_content = '''<<<<< Hello Mahbod >>>>> ,
Ein Termin bei der Botschaft ist FREI beeil dich !!!!!!!!!!!!!!!!
'''
#The mail addresses and password
sender_address = "py.scraper.mahbod@gmail.com"
sender_pass = "Mahbod69@@"
receiver_address = "mhsafdari@gmail.com"
#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'Freier Termin bei Botschaft.'   #The subject line

def sendMail():
    #The body and the attachments for the mail
    message.attach(MIMEText(mail_content, 'plain'))
    #Create SMTP session for sending the mail
    session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
    session.starttls() #enable security
    session.login(sender_address, sender_pass) #login with mail_id and password
    text = message.as_string()
    session.sendmail(sender_address, receiver_address, text)
    session.quit()
    print('Mail Sent')
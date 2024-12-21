import smtplib
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('vijayrangu22@gmail.com','swtk rnzj judv qpdp')
    msg=EmailMessage()
    msg['FROM']='vijayrangu22@gmail.com'
    msg['TO']=to
    msg['SUBJECT']=subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()
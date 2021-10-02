import smtplib
import email.message
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#for notifying the user that the email has arrived
def send_contact_email(to_user):
    server = smtplib.SMTP('smtp.gmail.com:587')

    email_content =  """
        Thanks for contacting Studyhelp 
    """
    msg = MIMEMultipart()
    msg['Subject'] = 'Study Help'

    msg['From'] = 'studyhelpbusiness@gmail.com'
    msg['To'] = to_user
    password = 'studyhelp$123'
    msg.add_header('Content-Type', 'text/html')
    msg.attach(MIMEText(email_content,'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()

        #Login creds
        server.login(msg['From'],password)

        #Send email
        server.sendmail(msg['From'],[msg['To']],msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as ex:
        print("An exception occured",ex)
    
def send_contact_notification(contact_from,the_message):
    msg = MIMEMultipart()

    
    message = the_message
    contact_name = contact_from
    # setup the parameters of the message
    password = "studyhelp$123"
    msg['From'] = "studyhelpbusiness@gmail.com"
    msg['To'] = "studyhelpbusiness@gmail.com"
    msg['Subject'] = "Contact notification from "+contact_name+""
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com: 587')
    
        server.starttls()
    
        # Login Credentials for sending the mail
        server.login(msg['From'], password)
    
    
        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()

        print("Email sent succesfully")
    except Exception as ex:
        print('Something went wrong',ex)
    #create server
    print ("successfully sent email to %s:" % (msg['To']))




def send_order_email(to_user):
    server = smtplib.SMTP('smtp.gmail.com:587')

    email_content =  """
        Thanks for contacting Studyhelp! We have recieved your order
    """
    msg = MIMEMultipart()
    msg['Subject'] = ' Study Help'

    msg['From'] = 'studyhelpbusiness@gmail.com'
    msg['To'] = to_user
    password = 'studyhelp$123'
    msg.add_header('Content-Type', 'text/html')
    msg.attach(MIMEText(email_content,'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com: 587')
        server.starttls()

        #Login creds
        server.login(msg['From'],password)

        #Send email
        server.sendmail(msg['From'],[msg['To']],msg.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as ex:
        print("An exception occured",ex)
    
def send_order_notification(contact_from,the_message):
    msg = MIMEMultipart()

    
    message = the_message
    contact_name = contact_from
    # setup the parameters of the message
    password = "studyhelp$123"
    msg['From'] = "studyhelpbusiness@gmail.com"
    msg['To'] = "studyhelpbusiness@gmail.com"
    msg['Subject'] = "Order notification from "+contact_name+""
    
    # add in the message body
    msg.attach(MIMEText(message, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com: 587')
    
        server.starttls()
    
        # Login Credentials for sending the mail
        server.login(msg['From'], password)
    
    
        # send the message via the server.
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        server.quit()

        print("Email sent succesfully")
    except Exception as ex:
        print('Something went wrong',ex)
    #create server
    print ("successfully sent email to %s:" % (msg['To']))

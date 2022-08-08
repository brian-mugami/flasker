import smtplib
import os
from email.message import EmailMessage

def to_client(email_to_send):
     EMAIL_ADDRESS = os.environ.get('nyumba_email')
     EMAIL_PASSWORD = os.environ.get('nyumba_pass')

     email = EmailMessage()
     email['Subject'] = "Delivery Confirmation"
     email['From'] = EMAIL_ADDRESS
     email['To'] = email_to_send
     email.set_content("Your message has been received by Nyumba Solutions, our team will reach out to you as soon as possible. \n Kind Regards, Nyumba Soltions. ")

     with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
          smtp.starttls()
          smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
          smtp.send_message(email)

def to_admin(email,message,subject):
    email_from = email
    message = message
    subject = subject

    EMAIL_ADDRESS = os.environ.get('nyumba_email')
    EMAIL_PASSWORD = os.environ.get('nyumba_pass')
    destination_email = os.environ.get('destination_email')
    email=EmailMessage()
    email['Subject'] = "Email From Client"
    email['From'] = EMAIL_ADDRESS
    email['To'] = destination_email
    email.set_content(f"You have a new mail from {email_from} with subject: {subject}  and message:{message} \n Please reply using {EMAIL_ADDRESS} to this message!!!")

    with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
        smtp.starttls()
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(email)


## how to send an email using python
## go over to our gmail account and set up two facot authentication
## generate app password
## create a function to send the mail

from email.message import EmailMessage
import ssl
import smtplib 
 
email_sender = 'effiongblessing@gmail.com'
email_password = "xrgn liyd pyxs ldsl"
 
email_receiver = 'wimelik739@bllibl.com'

subject = "don't forget to be pretty"
body = """
you need to get your bag up, i need a skill
"""

em = EmailMessage ()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp :
     smtp.login(email_sender, email_password)
     smtp.sendmail(email_sender, email_receiver, em.as_string())
     first change
     second change
     third change
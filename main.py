'''
# random: To generate 6 digit otp
# smtplib: To connect with gmail and send otp to destination mail 
# EmailMessage: To Decorate message
'''
import random
import smtplib
from email.message import EmailMessage

# generate 6 digit otp
def otp_verify():
    otp = ''
    for i in range(6):
        otp += str(random.randint(0, 9))
    return otp



def gmail_verify(to_mail, otp):

     # Set up the SMTP server and login
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    from_mail = 'harsha.n.chari31@gmail.com'
    password = 'rnfw bszn sffr hpww'
    server.login(from_mail, password)

     # Specify the path to the HTML template file
    template_path = 'templates/email_template.html'

    # Read the HTML template from the file
    with open(template_path, 'r') as file:
        html_content = file.read()

    # Insert the OTP into the HTML conten
    html_content = html_content.format(otp = otp)

    # Create the email message
    msg = EmailMessage()
    msg['Subject'] = 'One Time Password'
    msg['From'] = from_mail
    msg['To'] = to_mail
    msg.set_content(html_content, subtype = 'html')

    # Send the email    
    # server.sendmail(from_mail, to_mail, otp)
    server.send_message(msg)
    server.quit()
    print('Email sent')

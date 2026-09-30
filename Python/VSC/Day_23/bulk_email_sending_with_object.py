import smtplib
from email.message import EmailMessage
sender = 'dileepkumarvalluri31@gmail.com'
password = ''
contacts = [
    {'name': 'Dileep Kumar', 'email': 'dileepkumarvalluri28@gmail.com'},
    {'name': 'Dileep Kumar', 'email': 'dileepkumarvalluri0103@gmail.com'},
    {'name': 'Dileep Kumar', 'email': 'dileepkumarvalluri2005@gmail.com'},
]
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
for contact in contacts:
    msg = EmailMessage()
    msg['From'] = sender
    msg['To'] = contact['email']
    message = f'''Hi {contact['name']},
    Hope you are doing well.
    I am very excited to share this new with you.
    I have just learnt how to send emails using python
    and I am very interested in learning new things ahead.
    
    Thanks & Regards,
    Dileep Kumar'''
    msg.set_content(message)
    server.send_message(msg)
    print(f'Mail sent to {contact['email']}')
server.quit()
print('All emails sent successfully!')

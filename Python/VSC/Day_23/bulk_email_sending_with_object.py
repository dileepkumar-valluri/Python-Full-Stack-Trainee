import smtplib
from email.message import EmailMessage
sender = ''
password = ''
contacts = [
    {'name': 'User1', 'email': '............@gmail.com'},
    {'name': 'User2', 'email': '...........@gmail.com'},
    {'name': 'User3', 'email': '...........@gmail.com'},
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

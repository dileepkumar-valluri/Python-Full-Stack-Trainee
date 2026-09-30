import smtplib
from email.message import EmailMessage
sender = 'dileepkumarvalluri31@gmail.com'
receiver = 'dileepkumarvalluri28@gmail.com'
password = 'esrbtjstnvbpfvym'

# Create a file containing prime numbers from 2 to 100
with open('prime_numbers.txt', 'w') as file:
    for num in range(2, 101):
        is_Prime = True
        for i in range(2, int(num**0.5)+1):
            if num % i == 0:
                is_Prime = False
                break
        if is_Prime:
            file.write(str(num)+'\n')

# create the mail
msg = EmailMessage()
msg['From'] = sender
msg['To'] = receiver
msg['Subject'] = 'Prime Numbers'
msg.set_content("""Hi,
Please Find the Prime Numbers from 2 to 100 attached.

Thanks and regards,
Dileep Kumar
""")

# Attach file
with open('prime_numbers.txt', 'rb') as file:
    file_data = file.read()
    msg.add_attachment(
        file_data,
        maintype='text',
        subtype='plain',
        filename='prime_numbers.txt'
    )

# Send mail
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
server.send_message(msg)
server.quit()
print('Mail Sent Successfully!')

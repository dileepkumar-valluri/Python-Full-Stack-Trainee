import smtplib
sender = '.....@gmail.com'
receiver = '......@gmail.com'
password = ''
msg = 'Hi this is Dileep Kumar from Codegnan Institute'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, msg)
server.quit()
print('Mail Sent Successfully!')

import smtplib
sender = 'dileepkumarvalluri31@gmail.com'
receiver = 'dileepkumarvalluri28@gmail.com'
password = 'esrbtjstnvbpfvym'
msg = 'Hi this is Dileep Kumar from Codegnan Institute'
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, msg)
server.quit()
print('Mail Sent Successfully!')

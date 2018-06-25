import smtplib

# Specifying the from and to addresses

fromaddr = 'siddamsa.222@gmail.com'
toaddrs  = 'siddamsa.222@gmail.com'

# Writing the message (this message will appear in the email)

msg = 'Message sent from python'

# Gmail Login

username = 'siddamsa.222@gmail.com'
password = 'umaraniram'

# Sending the mail  

server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

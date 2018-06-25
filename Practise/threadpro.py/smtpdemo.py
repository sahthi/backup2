import smtplib

sender='siddamsa.222@gmail.com'
receiver='siddamsa.222@gmail.com'

message="Hi!how are u...."

try:
	smtplib.SMTP('mail.gmail.com', 465)
        smtpObj.sendmail(sender,receiver,message)
        print "successfully sent email"
except SMTPException:
	print"Error:Unable to send mail"
				

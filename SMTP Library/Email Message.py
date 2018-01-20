import smtplib    #Import smtp (Simple Mail Transfer Protocol) Library

s = smtplib.SMTP('smtp.gmail.com', 587)  #Create a server object at gmail

s.ehlo()
s.starttls()

s.login("prasad02dalavi@gmail.com", "BeTheOne!2301") #Next, log in to the server

#Send the mail
msg = "Hello! Python has sent you an email." # The /n separates the message from the headers
s.sendmail("prasad02dalavi@gmail.com", "prasad01dalavi@gmail.com", msg)
print "E-mail has been sent!"
s.quit()

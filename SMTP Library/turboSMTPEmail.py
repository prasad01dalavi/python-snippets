import turbosmtp
from email import message

message = message.Message()
message["From"] = "from@address.com"
message["To"] = "to@addresss.com"
message["Subject"] = "Hello World!"

smtp = turbosmtp.TurboSMTP("your_username", "your_password")
smtp.send(message)

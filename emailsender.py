import smtplib

from_ = 'archnomed@gmail.com'
to_ = 'allbrightdsouza7@gmail.com'

message = 'say yes if ur a faggot'

password = 'Nontypants1'

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()
server.login(from_,password)
server.sendmail(from_,to_,message)
server.quit()



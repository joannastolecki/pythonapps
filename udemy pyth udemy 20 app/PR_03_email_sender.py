import smtplib

#to = input("Enter user email/n") 
to = "jstolecki@icloud.com"

content = "ala ma kota"

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo
    server.starttls
    server.login('joanna.stolecki@gmail.com','OliwkaNatalia2014')
    server.sendmail('joanna.stolecki@gmail.com',to,content)
    server.close # close connention to smtp
    
sendEmail(to, content)

    
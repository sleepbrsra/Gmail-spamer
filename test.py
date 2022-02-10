from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

#Только gmail почта

host = "smtp.gmail.com"
port = 587
#ваша почта
username = input("Почта которая будет спамить?: ")
#пароль от почты
password = input("Пароль от почты спаммера?: ")
from_email = username
#почта на которую происходит спам(макс. 1)
to_list = input("почта на которую будет происходить спам?: ")

email_conn = smtplib.SMTP(host, port)
email_conn.starttls()
email_conn.login(username, password)

the_msg = MIMEMultipart("alternative")
#Текст спама
the_msg['Subject'] = input("text spam?:")
the_msg["From"] = from_email

plain_txt = "Testing the message"
#(use https://html-online.com/editor/)
html_txt = """\
<html>
    <head></head>
    <body>
        <h1></h1>
    </body>
</html>
"""

part_1 = MIMEText(plain_txt, 'plain')
part_2 = MIMEText(html_txt, "html")

the_msg.attach(part_1)
the_msg.attach(part_2)


i=0
print("Отправка...")
#измените значение меньше чем на то, сколько раз вы хотите, чтобы электронное письмо было отправлено
#пример: i<80 sends 80 emails, i<10 sends 10 emails
while i<80:
    email_conn.sendmail(from_email, to_list, the_msg.as_string())
    print("Бот отправил " + str(i+1) + " писем.") 
    i=i+1

print("Всего " + str(i) + " писем было отправлено!")    
email_conn.quit()
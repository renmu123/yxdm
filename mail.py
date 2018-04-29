import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
from config import *


def send_mail(content, address):
    sender = SENDER  # 发件人邮箱账号
    password = PASSWORD  # 发件人邮箱密码(当时申请smtp给的口令)

    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = formataddr([FROM, sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
    # msg['To'] = formataddr([address, address])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
    msg['Subject'] = SUBJECT  # 邮件的主题，也可以说是标题

    with smtplib.SMTP_SSL("smtp.qq.com", 465) as server:
        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(sender, password)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(sender, address, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        print(SUCCESS_MSG)

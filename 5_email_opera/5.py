import smtplib
import schedule
import time

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

from apscheduler.schedulers.blocking import BlockingScheduler

# 1、定义邮箱地址、邮箱号、密码
# 2、定义发送、接收人
# 3、定义邮件内容（标题、发件人、内容
# 4、使用smtp对象发送邮件

mail_host = 'smtp.qq.com'
mail_user = '3253532864@qq.com'
mail_pass = 'wlasthctxxfrdaci'
mail_qq_port = 465

sender = mail_user
receives = ['sewellhe@outlook.com']


def send(msg):
    # smtp_obj = smtplib.SMTP(mail_host, 465)
    # qq邮箱使用SSL协议
    smtp_obj = smtplib.SMTP_SSL(mail_host, mail_qq_port)

    try:
        smtp_obj.login(sender, mail_pass)
        smtp_obj.sendmail(sender, receives, msg.as_string())
    except smtplib.SMTPException as e:
        print(e)


def send_text_email(title, content):
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header(mail_user)
    message['Subject'] = Header(title, 'utf-8')

    send(message)


def send_html_email(title, content):

    message = MIMEText(content, 'html', 'utf-8')
    message['From'] = Header(mail_user)
    message['Subject'] = Header(title, 'utf-8')

    send(message)


def send_attach_email(title, content, file_name):
    message = MIMEMultipart()

    attr = MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')
    attr['Content-Type'] = 'application/octet-stram'
    attr['Content-Disposition'] = f'attachment;filename="{file_name}"'

    message.attach(attr)
    message.attach(MIMEText(content, 'plain', 'utf-8'))

    send(message)


def send_email_regular_time():
    message = MIMEText('测试内容', 'plain', 'utf-8')
    message['From'] = Header(mail_user)
    message['Subject'] = Header('测试定时发送', 'utf-8')

    send(message)


if __name__ == '__main__':
    # send_html_email('发送html邮件测试', '<p style="color: red">测试内容</p>')
    # send_attach_email('发送附件邮件测试', '测试内容 ', )

    scheduler = BlockingScheduler()
    scheduler.add_job(send_email_regular_time, 'interval', seconds=10)
    scheduler.start()

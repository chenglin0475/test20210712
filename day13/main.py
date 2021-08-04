from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

from HTMLTestRunner import HTMLTestRunner
import unittest
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import smtplib
from email.utils import formataddr

tests = unittest.defaultTestLoader.discover(r"D:\PythonTool\test\day13",pattern="test*.py")
runner = HTMLTestRunner.HTMLTestRunner(
    title = "这是一份计算器的测试报告",
    description="这是减乘除法运算的测试报告",
    verbosity=1,
    stream= open("计算器.html",mode="w+",encoding="utf-8")
)
runner.run(tests)






def sendEmail(title, text, send, to, passwd, smtp_server, file):
    '''
    发送带附件的邮件
    :param title: 邮件标题
    :param text: 邮件正文
    :param send: 发送者邮箱
    :param passwd: 授权码
    :param to: 接收者邮箱
    :param smtp_server: 发送邮件的服务器
    :param file: 需要发送的附件
    :return:
    '''
    msg = MIMEMultipart()
    msg['From'] = send
    msg['To'] = to
    #文字部分
    msg['Subject'] = title  # 主题
    strstr=text  #文字内容
    att = MIMEText(strstr,'plain','utf-8')
    msg.attach(att)
    #附件
    att = MIMEApplication(open(file,'rb').read())  #你要发送的附件地址
    att.add_header('Content-Disposition', 'attachment', filename=file) #filename可随意取名
    msg.attach(att)
    server = smtplib.SMTP()
    server.connect(smtp_server)   #连接smtp邮件服务器
    server.login(send,passwd)   #登录smtp邮件服务器
    server.sendmail(send, to, msg.as_string())    #发送
    server.close()  #关闭


if __name__ == '__main__':

    smtp_server = 'smtp.qq.com'  # 使用QQ邮箱的SMTP服务器，可切换
    from_mail = '2015539611@qq.com'
    mail_pass = 'tiwblinqiacxdcef'
    to_mail = '2015539611@qq.com'
    title = 'test'
    text = 'send test'
    file = '计算器.html'
    sendEmail(title=title, text=text, send=from_mail, to=to_mail, passwd=mail_pass, smtp_server=smtp_server, file=file)
# my_sender = '2015539611@qq.com'  # 发件人邮箱账号
# my_pass = 'tiwblinqiacxdcef'  # 发件人邮箱密码
# my_user = '2015539611@qq.com'  # 收件人邮箱账号，我这边发送给自己
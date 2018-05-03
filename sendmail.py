from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr,formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import smtplib

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
def sendmail(text,to):
    from_addr = ''
    pw = ''
    #to = '3199408942@qq.com'
    smtp_server = 'smtp.qq.com'
    msg = MIMEMultipart()
    msg.attach(MIMEText(text,'plain','utf-8'))
    msg['From'] = _format_addr('molika<1104254583@qq.com>')
    msg['Subject'] = Header('天气情况')
    server = smtplib.SMTP_SSL(smtp_server, 465)
    server.set_debuglevel(1)
    server.login(from_addr, pw)
    server.sendmail(from_addr,to, msg.as_string())
import smtplib
from email.header import Header
from email.mime.text import MIMEText  # 引入smtplib和MIMEText,简单的纯文本文件
from email.utils import parseaddr, formataddr


def _format_affr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send(to, subject, content):
    # 通过SMTP发送
    # email地址和口令
    from_addr = 'wlqfzs@163.com'
    password = '50778wy1997910'
    # SMTP服务器地址：
    smtp_server = 'smtp.163.com'
    # 收件人地址
    to_addr = to

    msg = MIMEText(content, 'plain', 'utf-8')
    msg['From'] = _format_affr('Python lover <%s>' % from_addr)
    msg['To'] = _format_affr('wulingqi <%s>' % to_addr)
    msg['Subject'] = Header(subject, 'utf-8').encode()

    server = smtplib.SMTP_SSL(smtp_server, 465)  # SMTP协议默认端口是25
    # server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()

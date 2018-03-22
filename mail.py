import json
import smtplib
from email.header import Header
from email.mime.text import MIMEText  # 引入smtplib和MIMEText,简单的纯文本文件
from email.utils import parseaddr, formataddr


# load accounts from accounts.json
def load_accounts():
    accounts = {}
    with open("accounts.json") as f:
        data = json.loads(f.read())
        for account in data['accounts']:
            accounts[account['alias']] = account
            if account['alias'] == data['default']:
                accounts['default'] = account
    return accounts


accounts = load_accounts()

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send(to, subject, content, from_alias='default', html=True):
    account = accounts[from_alias]
    name = account['name']
    from_addr = account['addr']
    password = account['password']
    host = account['host']
    port = account['port']
    to_addr = to

    if html == True:
        msg = MIMEText(content, 'html', 'utf-8')
    else:
        msg = MIMEText(content, 'plain', 'utf-8')

    msg['From'] = _format_addr('%s <%s>' % (name, from_addr))
    msg['To'] = _format_addr(to_addr)
    msg['Subject'] = Header(subject, 'utf-8').encode()

    if account['ssl'] == True:
        server = smtplib.SMTP_SSL(host, port)
    else:
        server = smtplib.SMTP(host, port)

    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()


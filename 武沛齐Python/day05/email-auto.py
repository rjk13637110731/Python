# 1.将Python内置的模块（功能导入）
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

def send_email(to_email):
    # 2.构建邮件内容
    msg = MIMEText("领导早上好，领导今天辛苦了。", "html", "utf-8")   #  邮件内容
    msg["From"] = formataddr(["任健康", "fullmoonloong@163.com"])  # 自己的名字，自己的邮箱
    msg["To"] = to_email    # 目标邮箱
    msg["Subject"] = "360可视化title"   # 主题

    # 3.发送邮件
    server = smtplib.SMTP_SSL("smtp.163.com")
    server.login("fullmoonloong@163.com", "GFLONS")  # 账户，授权码
    server.sendmail("fullmoonloong@163.com", to_email, msg.as_string())  # 自己的邮箱，目标邮箱，邮件内容
    server.quit()
    
send_email("2322256438@qq.com")
send_email("2322256439@qq.com")
send_email("2322256430@qq.com")

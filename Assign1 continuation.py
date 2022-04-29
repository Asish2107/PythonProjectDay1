import hashlib
import os
from datetime import datetime
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import mysql.connector
import PyPDF2


def password_encryption(password):
    import hashlib
    hash_func = hashlib.sha1()
    encode_string = password.encode()
    hash_func.update(encode_string)
    message = hash_func.digest()
    return  message

from PyPDF2 import PdfFileWriter, PdfFileReader
mydb=mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="jasvemlknpr",
    database="world"
)
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE pdfs (name VARCHAR(255), password VARCHAR(255),encrypted_pass varchar(200),timestamp varchar(150))")
file=os.listdir(r"C:\Users\Dell\Desktop\pythonProject1")
print(file)
sender=input("Enter mail:" )
security=input("Enter password:")
receiver=input("Enter mail:")
for j,i in enumerate(file):
    if i.endswith(".pdf") and not PyPDF2.PdfFileReader(open("{}".format(i), 'rb')).isEncrypted:
        out = PdfFileWriter()
        #input = PdfFileReader(f"C://Users//Dell//Desktop//pythonProject1.pdf/{i}")
        input = PdfFileReader("C://Users//Dell//Desktop//pythonProject1//"+i)
        num = input.numPages
        for idx in range(num):
            page = input.getPage(idx)
            out.addPage(page)
        current_time = datetime.now().replace(microsecond=0)
        format = "%y_%b_%d_%H_%M_%S"
        new_time = datetime.strftime(current_time, format)
        password = new_time
        out.encrypt(password)
        with open(rf"C:\Users\Dell\Desktop\pythonProject1\{password}", "wb") as f:
            out.write(f)
        time.sleep(2)
        pas = password_encryption(password)
        mycursor = mydb.cursor()

        sql = "INSERT INTO pdfs (name, password, encrypted_pass,timestamp) VALUES (%s, %s, %s,%s)"
        val = (str(i),str(password),str(pas),str(i))
        mycursor.execute(sql, val)

        mydb.commit()

        print(pas)
        body = '''Hello,This is your pdf and following is your password {} and following is your encrypted password {}'''.format(password,pas)
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = 'This email has an attacment, a pdf file'
        message.attach(MIMEText(body, 'plain'))
        pdfname = '{}'.format(password)
        binary_pdf = open(pdfname, 'rb')
        payload = MIMEBase('application', 'octate-stream', Name=pdfname)
        payload.set_payload((binary_pdf).read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
        message.attach(payload)
        session = smtplib.SMTP('smtp.gmail.com', 587)
        session.starttls()
        session.login(sender, security)
        text = message.as_string()
        session.sendmail(sender, receiver, text)
        session.quit()
        print('Mail Sent')

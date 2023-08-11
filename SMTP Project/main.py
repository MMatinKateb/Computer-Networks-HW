import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from TextColors import color_escape
from os import system

system('CLS')

print(color_escape['cyan'] + '\t\tPython SMTP User Agent\n\n' + color_escape['reset'])

email = "pythonuseragent@gmail.com"
password = input(color_escape['yellow'] + 'Enter agent\'s password: ' + color_escape['reset'])

def send_email(subject, msg, to):
    message = MIMEMultipart()
    message['From']    = email
    message['To']      = to
    message['Subject'] = subject
    
    body = msg
    message.attach(MIMEText(body, 'plain'))

    smtp_server = smtplib.SMTP("smtp.gmail.com", 587)
    smtp_server.starttls()
    smtp_server.login(email, password)
    smtp_server.send_message(email, to, message.as_string())

    smtp_server.quit()


def main():
    recipient = input(f"{color_escape['yellow']}\tEnter recipient's address: {color_escape['reset']}")
    subject =   input(f"{color_escape['yellow']}\tEnter subject: {color_escape['reset']}")
    message =   input(f"{color_escape['yellow']}\tEnter message: {color_escape['reset']}")

    print(color_escape['red'] + "Sending message..." + color_escape['reset'])
    send_email(subject, message, recipient)
    print(color_escape['Green'] + "Message sent successfully!" + color_escape['reset'])


if __name__ == '__main__':
    main()
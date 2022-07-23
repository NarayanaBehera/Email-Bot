import smtplib

def send():
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("username", "password")
        subject="Testing"
        TEXT="My name is Narayana"
        message = 'Subject: {}\n\n{}'.format(subject, TEXT)
        s.sendmail("sender", "receiver", message)
        print("Success")

    except Exception as exception:
        print(exception)
        print("Failure")

if __name__ == '__main__':
    send()

import smtplib

username = ""
password = ""


def send_mail(text='Email body', subject='hello', from_email=username, to_emails=None):
    assert isinstance(to_emails, list)

    # login to smtp server
    server = smtplib.SMTP()
    server.ehlo()
    server.starttls()
    server.login(user, password)

    server.sendmail(from_email, to_emails, msg_str)

    server.quit()
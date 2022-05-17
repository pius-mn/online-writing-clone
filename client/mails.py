from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse


def otp_email(otp, username, receiver):
    subject = 'Email Verification'
    message = 'Dear' + username + \
              ' We need to verify that your email.This is you Otp ' + str(otp)
    from_email = 'info@goldlinebreeze.com'
    try:
        send_mail(subject, message, from_email, [receiver])
        print('sent')
    except BadHeaderError:
        return HttpResponse('Invalid header found.')

def WelcomeEmail(username, receiver):
    subject = 'Welcome'
    message = 'Welcome ' + username + 'We are glad that you have chosen us. We hope yo enjoy our services'
    from_email = 'info@goldlinebreeze.com'
    try:
        send_mail(subject, message, from_email, [receiver])
        print('sent')
    except BadHeaderError as e:
        print(e)
        return HttpResponse('Invalid header found')

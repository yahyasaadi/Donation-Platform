from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

import schedule
import time


# Create your views here.
def home(request):
    return render(request, 'paymentGateway/index.html')


def job():
    subject = f"Thank you for your Donations"
    message = f"Hello Donor, you can now start sharing beautiful images with the world."
    from_mail = settings.EMAIL_HOST_USER
    recipient_list = [''] #'yahyasnoor@gmail.com'
    send_mail(subject, message, from_mail, recipient_list, fail_silently=False)
    

schedule.every(3).seconds.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
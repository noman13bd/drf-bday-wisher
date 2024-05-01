from django.core.mail import send_mail
from datetime import date, timedelta
from celery import shared_task
from celery.schedules import crontab
from .models import Customer
from .serializers import CustomerSerializer
from .utils import Utils
import logging

logger = logging.getLogger(__name__)

@shared_task
def send_bday_wish():
    print("send_bday_wish")
    today = date.today()
    bdays = Customer.objects.filter(bday__month=today.month, bday__day=today.day, notified=False)
    for bday in bdays:
        print(f"hello {bday.name}. Happy Birthday. Enjoy your day!")
        mail_sub = f"hello {bday.name}. Happy Birthday."
        Utils.mail_send(
            mail_to=bday.email,
            mail_from="myemail@gmail.com",
            mail_subject=mail_sub,
            mail_body="Happy Birthday. Enjoy your day!"
        )
        serializer = CustomerSerializer(bday, data={'notified': True}, partial=True)
        if serializer.is_valid():
            serializer.save()
        
@shared_task
def update_bday_wish():
    print("update_bday_wish")
    today = date.today()
    yesterday = today - timedelta(days=1)
    bdays = Customer.objects.filter(bday__month=yesterday.month, bday__day=yesterday.day, notified=True)
    for bday in bdays:
        print(f"updating {bday.name}'s notified field'")
        bday.notified = False
        serializer = CustomerSerializer(bday, data={'notified': False}, partial=True)
        if serializer.is_valid():
            serializer.save()  
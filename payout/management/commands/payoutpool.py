import uuid
from django.core.management.base import BaseCommand
from django.conf import settings
from kafka import KafkaConsumer
import pickle
from common.hash_utils import sign_message
import requests


def payout_handler(data):
    request_id = str(uuid.uuid4())
    message = "|".join((
        request_id,
        settings.HALONGPAY_PARTNER_ID,
        data['bank_no'],
        data['account_no'],
        str(data['account_type']),
        data['account_name'],
        str(data['amount']),
        data['content'],
    ))
    signature = sign_message(message)
    res = requests.post(
        settings.NIGHT_PAY_ENDPOINT,
        json={
            'request_id': request_id,
            'partner_id': settings.HALONGPAY_PARTNER_ID,
            **data,
            'signature': signature,
        }
    )
    # TODO: dispatch result somewhere to show result to the user
    print(res.content)


class Command(BaseCommand):
    def handle(self, *args, **options):
        consumer = KafkaConsumer(
            settings.KAFKA_TOPIC_NAME,
            bootstrap_servers=[f"{settings.KAFKA_HOST}:{settings.KAFKA_POST}"],
        )
        print("start consuming payout request...")
        for message in consumer:
            deserialized_data = pickle.loads(message.value)
            # TODO: adding a serializer to validate fields and values
            print(deserialized_data)
            payout_handler(deserialized_data)

from django.core.management.base import BaseCommand
from kafka import KafkaProducer
from django.conf import settings
import pickle


class Command(BaseCommand):
    def handle(self, *args, **options):
        producer = KafkaProducer(
            bootstrap_servers=f"{settings.KAFKA_HOST}:{settings.KAFKA_POST}"
        )
        dump_data = {
            "bank_no": "4",                                 # VIETCOMBANK
            "account_no": "1023020330000",
            "account_type": 0,                              # Bank account number
            "account_name": "NGUYEN VAN A",
            "amount": 1000000,
            "content": "blabla",
        }
        serialized_data = pickle.dumps(dump_data)
        producer.send(settings.KAFKA_TOPIC_NAME, serialized_data)

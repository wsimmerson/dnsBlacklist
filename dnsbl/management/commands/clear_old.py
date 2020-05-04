from datetime import timedelta

from django.core.management import BaseCommand
from django.utils import timezone

from dnsbl.models import BlackListedIP


class Command(BaseCommand):
    help = "Clear IPs that haven't been seen in two weeks"

    def handle(self, *args, **options):
        for listed in BlackListedIP.objects.all():
            if listed.last_seen < timezone.now() - timedelta(days=14):
                listed.delete()

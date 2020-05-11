from django.core.management import BaseCommand

from dnsbl.models import BlackListedIP, WhiteListedIP, TrustedDomain


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("""
Blacklisted: {},
WhiteListed: {}
Trusted Domains {}        
        """.format(
            BlackListedIP.objects.all().count(),
            WhiteListedIP.objects.all().count(),
            TrustedDomain.objects.all().count()
        )
              )

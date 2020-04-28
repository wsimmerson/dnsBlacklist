from django.core.management import BaseCommand

from dnsbl.models import WhiteListedIP, BlackListedIP


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('ip_address', type=str, help="IP Address")

        # Named (optional) arguments
        parser.add_argument(
            '--reason',
            type=str,
            nargs='+',
            help="Reason for blacklisting/whitelisting"
        )
        parser.add_argument(
            '--whitelist',
            action="store_true",
            help='switch to whitelist'
        )
        parser.add_argument(
            '--delete',
            action='store_true',
            help='Delete poll instead of closing it',
        )

    def handle(self, *args, **options):
        if options['delete']:
            try:
                if options['whitelist']:
                    WhiteListedIP.objects.filter(ip_address=options['ip_address']).delete()
                else:
                    BlackListedIP.objects.filter(ip_address=options['ip_address']).delete()
            except Exception as e:
                print("Error:", e)
            return

        listing = None
        if options['whitelist']:
            listing = WhiteListedIP()
            if options['reason']:
                listing.reason_for_whitelisting = " ".join(options['reason'])
            BlackListedIP.objects.filter(ip_address=options['ip_address']).delete()
        else:
            listing = BlackListedIP()
            if options['reason']:
                listing.reason_for_blacklisting = " ".join(options['reason'])

        if listing:
            listing.ip_address = options['ip_address']
            listing.save()

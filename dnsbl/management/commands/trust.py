from django.core.management import BaseCommand

from dnsbl.models import TrustedDomain


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('domain', type=str, nargs='+', help="list of trusted domains")

        parser.add_argument(
            '--delete',
            action="store_true",
            help="delete trust"
        )

    def handle(self, *args, **options):
            for domain in options['domain']:
                if options['delete']:
                    TrustedDomain.objects.filter(domain__iexact=domain).delete()
                else:
                    TrustedDomain(
                        domain=domain
                    ).save()
            return

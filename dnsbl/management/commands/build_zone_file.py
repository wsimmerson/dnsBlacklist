from django.core.management import BaseCommand
from django.utils import timezone

from dnsBlacklist import settings
from dnsbl.models import BlackListedIP


def nameservers():
    ns = ""
    for n in settings.DNSBL_NAMESERVERS:
        ns = ns + "\t\t\tIN NS {}\n".format(n)
    return ns


class Command(BaseCommand):
    def handle(self, *args, **options):
        print("Building new zone file")
        serial = timezone.now().strftime('%Y%m%d01')
        zone = """
$TTL    86400
@           IN SOA  {}. {}. (
                {}  ; serial
                7200        ; refresh (2 hours)
                5400        ; retry (1.5 hours)
                1814400     ; expire (3 weeks)
                86400       ; minimum (1 day)
            )
{}
            IN  A {}
        """.format(settings.DNSBL_NAMESERVERS[0],
                   settings.DNSBL_ADMIN_EMAIL.replace("@", "."),
                   serial,
                   nameservers(),
                   settings.DNSBL_A_RECORD_IP)

        with open(settings.DNS_ZONE_FILE, "w") as f:
            f.write(zone)
            for bl in BlackListedIP.objects.all():
                f.write(bl.record())
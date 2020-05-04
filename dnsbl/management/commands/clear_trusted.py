import socket

from django.core.management import BaseCommand

from dnsbl.models import BlackListedIP, TrustedDomain, WhiteListedIP


class Command(BaseCommand):
    def handle(self, *args, **options):
        for ip in BlackListedIP.objects.all():
            try:
                who = socket.gethostbyaddr(ip.ip_address)
                print(who)
                domain = '.'.join(who[0].split('.')[-2:])
                trusted = TrustedDomain.objects.filter(
                    domain__endswith=domain).exists()
                if trusted:
                    print(trusted)
                    whitelisted = WhiteListedIP(
                        ip_address=ip.ip_address,
                        reason_for_whitelisting="{} listed as Trusted".format(domain)
                    )
                    whitelisted.save()
                    ip.delete()
            except Exception as e:
                print(e)

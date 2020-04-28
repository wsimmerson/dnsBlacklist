from django.db import models

# Create your models here.
from django.utils import timezone


def reverse_ip(ip):
    parts = ip.split('.')
    rev_parts = reversed(parts)
    return '.'.join(rev_parts)


class BlackListedIP(models.Model):
    ip_address = models.GenericIPAddressField()
    reason_for_blacklisting = models.CharField(max_length=255, default="IP Reported for sending SPAM")
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ip_address

    def record(self):
        revip = reverse_ip(self.ip_address)
        return """
; {}
{}	IN	A	172.0.0.2
{}	IN	TXT	"{}"
        """.format(self.ip_address, revip, revip, self.reason_for_blacklisting)


class WhiteListedIP(models.Model):
    ip_address = models.GenericIPAddressField()
    reason_for_whitelisting = models.CharField(max_length=255)
    created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.ip_address


class TrustedDomain(models.Model):
    domain = models.CharField(max_length=255)

    def __str__(self):
        return self.domain
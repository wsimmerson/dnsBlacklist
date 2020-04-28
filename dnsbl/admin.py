from django.contrib import admin

# Register your models here.
from dnsbl.models import BlackListedIP, WhiteListedIP


class BlackListedAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'reason_for_blacklisting', 'created']
    search_fields = ['ip_address']


class WhiteListedAdmin(admin.ModelAdmin):
    list_display = ['ip_address', 'reason_for_whitelisting', 'created']
    search_fields = ['ip_address']


admin.site.register(BlackListedIP, BlackListedAdmin)
admin.site.register(WhiteListedIP, WhiteListedAdmin)

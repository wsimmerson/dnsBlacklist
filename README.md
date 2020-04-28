# **README**

Tool to manage blacklisted IP addresses and generate BIND9 zone file to be used by mail servers.

Requires a properly configured BIND9 server.

### Whats an RBL?

Realtime Black List (RBLs) uses the DNS protocol to query the well-known IP addresses which have been complaint to send worm, virus & junk mail. Using RBLs to prevent junk, virus & worm email is very effective. The algorithm of RBLs is different with that of Anti-Spam and Anti-Virus services as RBLs works based on IP address, while Anti-Spam and Anti-Virus services work based on the message content.

### Settings
Include in your dnsBlacklist/settings.py

* DNSBL_DOMAIN = "dnsbl.example.com" #  name of domain under which lookups will occur.
* DNSBL_A_RECORD_IP = "10.2.3.4"  # The IP of the DNSBL_DOMAIN
* DNSBL_NAMESERVERS = ['ns1.example.com', 'ns2.example.com', 'ns3.example.com'] #  Nameservers which serve these records
* DNSBL_ADMIN_EMAIL = "admin@example.com" # self explanatory
* DNS_ZONE_FILE = os.path.join('tmp', 'dnsbl.db') #  path to the zone file as configured in bind9 named.conf.local
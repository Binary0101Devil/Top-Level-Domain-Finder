### Top Level Domain Finder by Binary0101devil

## How to Install
```
sudo apt update
sudo pip install python-whois
sudo git clone https://github.com/Binary0101Devil/Top-Level-Domain-Finder.git
cd Top-Level-Domain-Finder
python3 TLDFinder.py
python3 TLD2.0Finder.py 
```

## How TLDFinder.py works
```
python3 TLDFinder.py
Enter a domain: example
Domain example.com is registered.
Domain example.in is registered.
Domain example.uk is registered.
Domain example.gov is available.
Domain example.org is registered.
```
## How TLD2.0Finder.py works ------------>>>>>> Updated version with table.

```
python3 TLD2.0Finder.py
Enter a domain: example
╒═════════════╤════════════╤══════════════════════════════════════════════════════════════════════════════════════════╕
│ Domain      │ Status     │ WHOIS Details                                                                            │
╞═════════════╪════════════╪══════════════════════════════════════════════════════════════════════════════════════════╡
│ example.com │ Registered │ {                                                                                        │
│             │            │   "domain_name": "EXAMPLE.COM",                                                          │
│             │            │   "registrar": "RESERVED-Internet Assigned Numbers Authority",                           │
│             │            │   "whois_server": "whois.iana.org",                                                      │
│             │            │   "referral_url": null,                                                                  │
│             │            │   "updated_date": "2023-08-14 07:01:38",                                                 │
│             │            │   "creation_date": "1995-08-14 04:00:00",                                                │
│             │            │   "expiration_date": "2024-08-13 04:00:00",                                              │
│             │            │   "name_servers": [                                                                      │
│             │            │     "A.IANA-SERVERS.NET",                                                                │
│             │            │     "B.IANA-SERVERS.NET"                                                                 │
│             │            │   ],                                                                                     │
│             │            │   "status": [                                                                            │
│             │            │     "clientDeleteProhibited https://icann.org/epp#clientDeleteProhibited",               │
│             │            │     "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",           │
│             │            │     "clientUpdateProhibited https://icann.org/epp#clientUpdateProhibited"                │
│             │            │   ],                                                                                     │
│             │            │   "emails": null,                                                                        │
│             │            │   "dnssec": "signedDelegation",                                                          │
│             │            │   "name": null,                                                                          │
│             │            │   "org": null,                                                                           │
│             │            │   "address": null,                                                                       │
│             │            │   "city": null,                                                                          │
│             │            │   "state": null,                                                                         │
│             │            │   "registrant_postal_code": null,                                                        │
│             │            │   "country": null                                                                        │
│             │            │ }                                                                                        │
├─────────────┼────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ example.in  │ Registered │ {                                                                                        │
│             │            │   "domain_name": "example.in",                                                           │
│             │            │   "registrar": "National Informatics Centre",                                            │
│             │            │   "registrar_url": "http://registry.gov.in",                                             │
│             │            │   "registrar_iana": "800111",                                                            │
│             │            │   "updated_date": "2023-02-14 18:17:04",                                                 │
│             │            │   "creation_date": "2004-12-31 18:17:04",                                                │
│             │            │   "expiration_date": "2023-12-31 18:17:04",                                              │
│             │            │   "name_servers": null,                                                                  │
│             │            │   "organization": null,                                                                  │
│             │            │   "state": "Delhi",                                                                      │
│             │            │   "status": [                                                                            │
│             │            │     "serverRenewProhibited http://www.icann.org/epp#serverRenewProhibited",              │
│             │            │     "serverDeleteProhibited http://www.icann.org/epp#serverDeleteProhibited",            │
│             │            │     "serverUpdateProhibited http://www.icann.org/epp#serverUpdateProhibited",            │
│             │            │     "inactive http://www.icann.org/epp#inactive"                                         │
│             │            │   ],                                                                                     │
│             │            │   "emails": null,                                                                        │
│             │            │   "country": "IN",                                                                       │
│             │            │   "dnssec": "unsigned"                                                                   │
│             │            │ }                                                                                        │
├─────────────┼────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ example.uk  │ Registered │ {                                                                                        │
│             │            │   "domain_name": "example.uk",                                                           │
│             │            │   "registrar": "No registrar listed.  This domain is registered directly with Nominet.", │
│             │            │   "registrar_url": null,                                                                 │
│             │            │   "status": "No registration status listed.",                                            │
│             │            │   "registrant_name": "Nominet UK",                                                       │
│             │            │   "registrant_type": "UK Limited Company, (Company number: 3203859)",                    │
│             │            │   "registrant_street": "Oxford Science Park",                                            │
│             │            │   "registrant_city": "Oxford",                                                           │
│             │            │   "registrant_country": "OX4 4DQ",                                                       │
│             │            │   "creation_date": "2016-05-06 00:00:00",                                                │
│             │            │   "expiration_date": null,                                                               │
│             │            │   "updated_date": "2022-11-10 00:00:00",                                                 │
│             │            │   "name_servers": "curt.ns.cloudflare.com"                                               │
│             │            │ }                                                                                        │
├─────────────┼────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ example.gov │ Available  │ -                                                                                        │
├─────────────┼────────────┼──────────────────────────────────────────────────────────────────────────────────────────┤
│ example.org │ Registered │ {                                                                                        │
│             │            │   "domain_name": "example.org",                                                          │
│             │            │   "registrar": "ICANN",                                                                  │
│             │            │   "whois_server": null,                                                                  │
│             │            │   "referral_url": null,                                                                  │
│             │            │   "updated_date": "2023-10-14 04:00:50",                                                 │
│             │            │   "creation_date": "1995-08-31 04:00:00",                                                │
│             │            │   "expiration_date": "2024-08-30 04:00:00",                                              │
│             │            │   "name_servers": [                                                                      │
│             │            │     "a.iana-servers.net",                                                                │
│             │            │     "b.iana-servers.net"                                                                 │
│             │            │   ],                                                                                     │
│             │            │   "status": [                                                                            │
│             │            │     "serverDeleteProhibited https://icann.org/epp#serverDeleteProhibited",               │
│             │            │     "serverRenewProhibited https://icann.org/epp#serverRenewProhibited",                 │
│             │            │     "serverTransferProhibited https://icann.org/epp#serverTransferProhibited",           │
│             │            │     "serverUpdateProhibited https://icann.org/epp#serverUpdateProhibited"                │
│             │            │   ],                                                                                     │
│             │            │   "emails": null,                                                                        │
│             │            │   "dnssec": "signedDelegation",                                                          │
│             │            │   "name": "REDACTED FOR PRIVACY",                                                        │
│             │            │   "org": "ICANN",                                                                        │
│             │            │   "address": "REDACTED FOR PRIVACY",                                                     │
│             │            │   "city": "REDACTED FOR PRIVACY",                                                        │
│             │            │   "state": "CA",                                                                         │
│             │            │   "registrant_postal_code": "REDACTED FOR PRIVACY",                                      │
│             │            │   "country": "US"                                                                        │
│             │            │ }                                                                                        │
╘═════════════╧════════════╧══════════════════════════════════════════════════════════════════════════════════════════╛                                                                          
```


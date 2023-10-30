import whois

def check_domain_availability(domain, tld):
    full_domain = f"{domain}.{tld}"
    try:
        whois_info = whois.whois(full_domain)
        if whois_info.status:
            print(f"Domain {full_domain} is registered.")
        else:
            print(f"Domain {full_domain} is available.")
    except Exception as e:
        print(f"An error occurred while checking {full_domain}: {e}")

# Get domain from user input
domain = input("Enter a domain: ")

# List of TLDs to check
tlds = ["com", "in", "uk", "gov", "org"]  # Add more TLDs as needed

# Check domain availability for each TLD
for tld in tlds:
    check_domain_availability(domain, tld)

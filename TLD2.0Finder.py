import whois
from tabulate import tabulate

def check_domain_availability(domain, tld, results):
    full_domain = f"{domain}.{tld}"
    try:
        whois_info = whois.whois(full_domain)
        if whois_info.status:
            results.append([full_domain, "Registered", str(whois_info)])
        else:
            results.append([full_domain, "Available", "-"])
    except Exception as e:
        results.append([full_domain, "Error", str(e)])

# Get domain from user input
domain = input("Enter a domain: ")

# List of TLDs to check
tlds = ["com", "in", "uk", "gov", "org"]  # Add more TLDs as needed

# Initialize results list
all_results = []

# Check domain availability for each TLD
for tld in tlds:
    check_domain_availability(domain, tld, all_results)

# Display results in an attractive table
headers = ["Domain", "Status", "WHOIS Details"]
print(tabulate(all_results, headers=headers, tablefmt="fancy_grid"))

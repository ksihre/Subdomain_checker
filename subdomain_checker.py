import requests
from bs4 import BeautifulSoup

def get_subdomains(domain):
    print(f"Finding subdomains for: {domain}")
    url = f"https://crt.sh/?q={domain}&output=json"
    
    # Send a request to crt.sh to get the subdomains
    response = requests.get(url)
    if response.status_code == 200:
        subdomains = []
        subdomains_data = response.json()

        for item in subdomains_data:
            subdomain = item['name_value']
            if subdomain not in subdomains:
                subdomains.append(subdomain)
        
        return subdomains
    else:
        print("Failed to retrieve data.")
        return []

# Ask user for the domain
if __name__ == "__main__":
    domain = input("Enter the domain (e.g., example.com): ")
    subdomains = get_subdomains(domain)
    if subdomains:
        print("\nSubdomains found:")
        for subdomain in subdomains:
            print(subdomain)
    else:
        print("No subdomains found.")

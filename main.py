import subprocess
from subdomain_scanner import find_subdomains
from port_scanner import scan_ports
from web_scraper import scrape_info

def main():
    print("Automated Bug Bounty Scanner")

    #Step1 : Get target domain
    target = input("Enter the target domain:")

    #Step2 : Finding Subdomains
    print(f"\nScanning subdomains for the {target}...\n")
    find_subdomains(target)

    #Step3 : Scanning open ports
    print("\nScanning for the open ports...\n")
    scan_ports(target)

    #Step4 : Scraping website for finding emails and links
    print("\nScraping website data...\n")
    target_url = f"https://{target}"
    scrape_info(target_url)

    print("\nScanning and scraping completed\n")

if __name__ == "__main__":
    main()



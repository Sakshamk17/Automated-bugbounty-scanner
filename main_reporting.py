import subprocess
from subdomain_scanner import find_subdomains
from port_scanner import scan_ports
from web_scraper import scrape_info
from sql_injection_scanner import scan_sql_injection
from xss_scanner import scan_xss
from report_generator import save_report  # Import report function

def main():
    print("\nAutomated Bug Bounty Scanner - Reporting Phase\n")

    # Step 1: Get Target Domain
    target_domain = input("Enter the target domain: ").strip()

    # Store results in a dictionary
    scan_results = {
        "target": target_domain,
        "subdomains": [],
        "open_ports": [],
        "emails": [],
        "links": [],
        "vulnerabilities": {
            "SQL Injection": [],
            "XSS": []
        }
    }

    # Step 2: Find Subdomains
    print("\nFinding subdomains...\n")
    subdomains = find_subdomains(target_domain) or []
    scan_results["subdomains"] = subdomains

    # Step 3: Scan for Open Ports
    print("\nScanning open ports...\n")
    open_ports = scan_ports(target_domain) or []
    scan_results["open_ports"] = open_ports

    # Step 4: Scrape Website for Emails & Links
    print("\nScraping website data...\n")
    target_url = f"https://{target_domain.removeprefix('https://')}"
    emails, links = scrape_info(target_url) or ([], [])  # Expecting a return of emails & links
    scan_results["emails"] = emails
    scan_results["links"] = links

    # Step 5: SQL Injection Scan
    target_sql_url = input("Enter a URL with a parameter for SQL Injection (e.g., http://example.com?id=1): ").strip()
    sql_vulns = scan_sql_injection(target_sql_url) or []
    scan_results["vulnerabilities"]["SQL Injection"] = sql_vulns

    # Step 6: XSS Scan
    target_xss_url = input("Enter a URL with a parameter for XSS (e.g., http://example.com/search?q=): ").strip()
    xss_vulns = scan_xss(target_xss_url) or []
    scan_results["vulnerabilities"]["XSS"] = xss_vulns

    # Save the results to a JSON report
    save_report(scan_results)

    print("\nScan complete! Report has been generated.\n")

if __name__ == "__main__":
    main()

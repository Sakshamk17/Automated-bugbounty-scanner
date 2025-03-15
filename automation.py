import json
from subdomain_scanner import find_subdomains
from port_scanner import scan_ports
from web_scraper import scrape_info
from sql_injection_scanner import scan_sql_injection
from xss_scanner import scan_xss
from report_generator import save_report  

def load_targets(filename = "targets.json"):
    """Loading target Domains and URL's from a JSON file."""

    try:
        with open(filename, 'r') as file:
            return json.load(file)
        
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return{}
    
def run_automated_scan():
    """Runs the entire script automatically on targets stored in target.json """

    targets = load_targets()

    if not targets:
        print("No targets found. Exiting...")
        return

    scan_results = {}

    for target in targets.get("domains" , []):
        print(f"\nScanning target: {target}\n")    

        
        scan_results[target] = {
            "subdomains": find_subdomains(target) or [],
            "open_ports": scan_ports(target) or [],
            "emails": [],
            "links": [],
            "vulnerabilities": {
                "SQL Injection": [],
                "XSS": []
            }
        }

        #Scraping data from website
        target_url = f"https://{target.removeprefix('https://')}"
        emails, links = scrape_info(target_url) or ([], [])
        scan_results[target]["emails"] = emails
        scan_results[target]["links"] = links

        #Running SQL Injection scan if applicable
        sql_target = targets.get("sql_urls", {}).get(target, "")
        if sql_target:
            sql_vulns = scan_sql_injection(sql_target) or []
            scan_results[target]["vulnerabilities"]["SQL Injection"] = sql_vulns
        
        #Running XSS scan if applicable
        xss_target = targets.get("xss_urls", {}).get(target, "")
        if xss_target:
            xss_vulns = scan_xss(xss_target) or []
            scan_results[target]["vulnerabilities"]["XSS"] = xss_vulns

    #Saving the full scan results
    save_report(scan_results)

    print("\nAutomated scan complete! Results saved.\n")

if __name__ == "__main__":
    run_automated_scan()

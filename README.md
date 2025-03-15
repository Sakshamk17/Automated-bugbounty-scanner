# Automated-bugbounty-scanner
A Python-based tool for automated bug bounty scanning. It performs subdomain enumeration, port scanning, and web scraping to help security researchers find vulnerabilities efficiently.

# Automated Bug Bounty Scanner

## Overview
The **Automated Bug Bounty Scanner** is a cybersecurity tool designed to automate the process of reconnaissance, vulnerability scanning, and reporting. It identifies subdomains, scans for open ports, scrapes website data, and detects SQL Injection & XSS vulnerabilities, generating a detailed report at the end.

## Features
- **Subdomain Enumeration**: Finds subdomains associated with a target domain.
- **Port Scanning**: Identifies open ports on the target domain.
- **Web Scraping**: Extracts emails, JavaScript files, and links.
- **SQL Injection Detection**: Identifies possible SQL injection vulnerabilities.
- **XSS (Cross-Site Scripting) Detection**: Tests for XSS vulnerabilities.
- **Automated Scanning**: Reads targets from `targets.json` and runs scans automatically.
- **Report Generation**: Saves scan results in a JSON file.

## Installation
### Prerequisites
- Python 3.10+
- Git
- Required libraries (installed via `requirements.txt`)

### Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Sakshamk17/Automated-bugbounty-scanner.git
   cd Automated-bugbounty-scanner
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Ensure `sqlmap` is Installed**:
   ```bash
   git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git
   ```

## Usage
### 1️⃣ **Manual Scanning**
Run individual scans interactively:
```bash
python main_exploitation.py
```
- Enter the **target domain** when prompted.
- Enter the **SQL Injection/XSS test URLs** when prompted.

### 2️⃣ **Automated Scanning** (Using `targets.json`)
Store targets in `targets.json`:
```json
{
    "domains": ["testphp.vulnweb.com"],
    "sql_urls": {"testphp.vulnweb.com": "http://testphp.vulnweb.com/listproducts.php?cat=1"},
    "xss_urls": {"testphp.vulnweb.com": "http://testphp.vulnweb.com/search.php?query="}
}
```
Run the automation script:
```bash
python automation.py
```

### 3️⃣ **Generate Scan Reports**
All scan results are saved automatically in:
```
scan_report.json
```

## File Structure
```
Automated-bugbounty-scanner/
├── automation.py        # Automated scanning script
├── main_exploitation.py # Manual scanning script
├── main_reporting.py    # Generates reports
├── report_generator.py  # Handles report saving
├── subdomain_scanner.py # Finds subdomains
├── port_scanner.py      # Scans open ports
├── web_scraper.py       # Scrapes website data
├── sql_injection_scanner.py # Detects SQL Injection
├── xss_scanner.py       # Detects XSS vulnerabilities
├── targets.json         # Stores predefined targets
├── scan_report.json     # Output report
├── requirements.txt     # Dependencies
├── README.md            # Documentation (this file)
```

## Contributions
We welcome contributions! Feel free to fork, open issues, or submit pull requests.

## Disclaimer
🚨 **For Educational & Research Purposes ONLY.** Unauthorized scanning of systems without permission is illegal. The developers are not responsible for misuse.

---
📌 **Maintainer**: [Sakshamk17](https://github.com/Sakshamk17)  



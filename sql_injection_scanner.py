import subprocess

def scan_sql_injection(target_url):
    print(f"Scanning {target_url} for SQL injection vulnerabilities...")

    #Running SQL map
    sqlmap_command = f"python sqlmap/sqlmap.py -u \"{target_url}\" --batch --dbs"

    try:
        #Running the command
        process = subprocess.Popen(sqlmap_command , shell=True , stdout=subprocess.PIPE , stderr=subprocess.STDOUT , text=True)

        for line in process.stdout:
            #Printing output
            print(line , end="")
        process.wait() # Wait for the sqlmap to finish

        print("SQL injection scan completed!\n")

    except Exception as e:
        print(f"An error occured {e}")        


if __name__ == "__main__":
    target = input("Enter the target url:\n")       
    scan_sql_injection(target)
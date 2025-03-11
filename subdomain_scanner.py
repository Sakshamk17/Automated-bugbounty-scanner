import subprocess

def find_subdomains(domain):
    print("Finding subdomains for " + domain)

    #running sublist3r
    result = subprocess.run(
        ['python' , 'Sublist3r/sublist3r.py' , '-d' , domain , '-o' , 'subdomains.txt'],
        capture_output= True,
        text= True
    )

    print(result.stdout)
    print("Subdomains saved in subdomains.txt")

#Example usage
if __name__ == "__main__":
    target_domain = input("Enter the target domain: ")
    find_subdomains(target_domain)
    
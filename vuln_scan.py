import nmap

# Function to scan for open ports and vulnerabilities
def scan(target, scan_type):
    scanner = nmap.PortScanner()
    
    # Specify port ranges to scan
    args = '-p 1-65535'
    
    # Specify additional options based on scan type
    if scan_type == '1':
        args += ' -sV'
    elif scan_type == '2':
        args += ' -sC'
    
    # Specify SMTP ports to scan
    args += ' -p 25,465,587'
    
    try:
        scanner.scan(target, arguments=args)
    except nmap.PortScannerError:
        print("Nmap error: ", scanner.scaninfo())
        return

    # Print out the results
    print("Host:", target)
    for port in scanner[target]['tcp']:
        print("Port:", port, "State:", scanner[target]['tcp'][port]['state'], "Service:", scanner[target]['tcp'][port]['name'])
        if 'script' in scanner[target]['tcp'][port]:
            print("Vulnerabilities:", scanner[target]['tcp'][port]['script'].strip())
        print("\n")

# Prompt the user for input and run the scan
target = input("Enter the target IP or hostname: ")
print("Select a scan type:\n1. Version detection\n2. Script scan")
scan_type = input("Enter the number of the scan type you want to perform: ")

scan(target, scan_type)

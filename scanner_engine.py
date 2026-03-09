import nmap

def perform_scan(target):
    nm = nmap.PortScanner()
    
    # SYN scan + Service detection
    nm.scan(hosts=target, arguments='-sS -sV')

    results = []

    for host in nm.all_hosts():
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()

            for port in ports:
                service = nm[host][proto][port]['name']

                results.append({
                    "ip": host,
                    "port": port,
                    "service": service
                })

    return results

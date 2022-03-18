import ipaddress 

def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address)
        print("IP address {} працює".format(address, ip))
    except ValueError:
        print("IP address {} не працює".format(address)) 
validate_ip_address("10.10.10.10")
validate_ip_address("10.10.10.01")


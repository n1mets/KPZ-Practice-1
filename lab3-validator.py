import ipaddress 

def validate_ip_address(address):
    try:
        ip = ipaddress.ip_address(address)
        print("IP address {} працює".format(address, ip))
    except ValueError:
        print("IP address {} не працює".format(address)) 
validate_ip_address("93.170.189.158")
validate_ip_address("93.170.189.448")
validate_ip_address("93.220.788.448")



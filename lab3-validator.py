from ipaddress import ip_address, IPv4Address, IPv6Address, AddressValueError


def _is_valid_ip_address(ip, ipv_type: str = 'any') -> bool:
    """Validates an ipd address"""
    try:
        if ipv_type == 'any':
            ip_address(ip)
        elif ipv_type == 'ipv4':
            IPv4Address(ip)
        elif ipv_type == 'ipv6':
            IPv6Address(ip)
        else:
            raise NotImplementedError
    except (AddressValueError, ValueError):
        return False
    else:
        return True

def run_tests():
    ipv4 = '192.168.0.1'
    ipv6 = '2001:db8::1000'
    bad = "I AM NOT AN IP"
    is_pv4 = _is_valid_ip_address(ipv4)
    is_pv6 = _is_valid_ip_address(ipv6)
    bad_ip = _is_valid_ip_address(bad)

    am_i_pv4 = _is_valid_ip_address(ipv6, ipv_type='ipv4')
    am_i_pv6 = _is_valid_ip_address(ipv4, ipv_type='ipv6')
    print(f'''
    * is_pv4 -> {is_pv4}
    * is_pv6 -> {is_pv6}
    * bad_ip -> {bad_ip}
    * am_i_pv4 -> {am_i_pv4}
    * am_i_pv6 -> {am_i_pv6}
    ''')



if __name__ == '__main__':
    run_tests()
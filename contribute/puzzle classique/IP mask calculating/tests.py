def parse(string):
    ip, mask = string.split("/")

    # calculate the ip number
    ip = [int(nb) for nb in ip.split(".")]
    ip_nb = (ip[0]<<24) | (ip[1]<<16) | (ip[2]<<8) | (ip[3])

    # calculate the mask number
    mask = int(mask)
    mask_nb = int("1"*mask + "0"*(32 - mask), 2)

    return ip_nb, mask_nb


def unparse(number):
    return (
        str((number>>24) & 255) + "." +
        str((number>>16) & 255) + "." +
        str((number>>8) & 255) + "." +
        str(number & 255)
    )


def network_address(ip_number, mask_number):
    return ip_number & mask_number


def wildcard_address(ip_mask):
    return ~ip_mask


def broadcast_address(ip_number, wildcard_number):
    return ip_number | wildcard_number


def ip_info(ip):
    ip = parse(ip)
    print("IP: ", unparse(ip[0]))
    print("Network: ", unparse(network_address(ip[0], ip[1])))
    print("Mask: ", unparse(ip[1]))
    wildcard = wildcard_address(ip[1])
    print("Wildcard: ", unparse(wildcard))
    print("Broadcast: ", unparse(broadcast_address(ip[0], wildcard)))


if __name__ in "__main__":

    for addr in [
        "10.0.1.34/24", "192.168.15.91/24", "77.179.54.2/20",
        "145.65.95.5/30", "100.0.52.12/10", "255.255.255.255/1",
        "0.0.0.0/32"
    ]:
        ip_info(addr)
        print()

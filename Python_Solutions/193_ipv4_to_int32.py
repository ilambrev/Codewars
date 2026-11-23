def ip_to_int32(ip):
    return int("".join(format(int(octet), "08b") for octet in ip.split(".")), 2)


# print(ip_to_int32("128.114.17.104"))
# print(ip_to_int32("0.0.0.0"))
# print(ip_to_int32("128.32.10.1"))

def ips_between(start, end):
    start_octets = [int(octet) for octet in start.split('.')]
    end_octets = [int(octet) for octet in end.split('.')]

    ips = 0

    for i in range(4):
        if not start_octets[i] == end_octets[i]:
            ips += (end_octets[i] - start_octets[i]) * 2 ** (8 * (3 - i))

    return ips

# print(ips_between("150.0.0.0", "150.0.0.1"))
# print(ips_between("10.0.0.0", "10.0.0.50"))
# print(ips_between("20.0.0.10", "20.0.1.0"))
# print(ips_between("10.11.12.13", "10.11.13.0"))
# print(ips_between("160.0.0.0", "160.0.1.0"))
# print(ips_between("94.95.217.20", "240.137.22.216"))
# print(ips_between( "236.4.19.226", "236.9.54.139"))
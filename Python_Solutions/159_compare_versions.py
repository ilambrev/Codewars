def compare_versions(version1, version2):
    version1_parts = [int(part) for part in version1.split(".")]
    version2_parts = [int(part) for part in version2.split(".")]

    diff = abs(len(version1_parts) - len(version2_parts))

    if len(version1_parts) > len(version2_parts):
        version2_parts += [0] * diff
    elif len(version2_parts) > len(version1_parts):
        version1_parts += [0] * diff

    for i in range(len(version1_parts)):
        if version1_parts[i] > version2_parts[i]:
            break
        if version1_parts[i] < version2_parts[i]:
            return False

    return True


# print(compare_versions("11", "10"))
# print(compare_versions("11", "11"))
# print(compare_versions("10.4.6", "10.4"))
# print(compare_versions("10.4", "10.4.8"))
# print(compare_versions("10.4", "11"))
# print(compare_versions("10.4", "10.10"))
# print(compare_versions("10.4.9", "10.5"))

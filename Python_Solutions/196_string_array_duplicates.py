def dup(arry):
    result = []

    for strng in arry:
        processed_strng = []
        for i in range(len(strng)):
            if i == 0 or (i > 0 and strng[i] != strng[i-1]):
                processed_strng.append(strng[i])

        result.append("".join(processed_strng))

    return result


# print(dup(["ccooddddddewwwaaaaarrrrsssss", "piccaninny", "hubbubbubboo"]))
# print(dup(["abracadabra", "allottee", "assessee"]))
# print(dup(["kelless", "keenness"]))
# print(dup(["Woolloomooloo", "flooddoorroommoonlighters", "chuchchi"]))
# print(dup(["adanac", "soonness", "toolless", "ppellee"]))
# print(dup(["callalloo", "feelless", "heelless"]))
# print(dup(["putteellinen", "keenness"]))
# print(dup(["kelless", "voorraaddoosspullen", "achcha"]))

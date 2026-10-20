from string import ascii_lowercase, ascii_uppercase


def one_down(txt):
    if isinstance(txt, str):
        decoded_txt = []
        for symbol in txt:
            if symbol in ascii_lowercase:
                decoded_txt.append(ascii_lowercase[ascii_lowercase.index(symbol)-1])
            elif symbol in ascii_uppercase:
                decoded_txt.append(ascii_uppercase[ascii_uppercase.index(symbol)-1])
            else:
                decoded_txt.append(symbol)

        return "".join(decoded_txt)
    else:
        return "Input is not a string"


# print(one_down("Ifmmp"))
# print(one_down("Uif usjdl up uijt lbub jt tjnqmf"))
# print(one_down(45))
# print(one_down("XiBu BcPvU dSbAz UfYu"))
# print(one_down(["Hello there", "World"]))
# print(one_down("BMM DBQT NBZCF"))
# print(one_down("qVAamFt BsF gVo"))
# print(one_down("CodeWars RockZ"))
# print(one_down(""))
# print(one_down("J ipqf zpv bsf ibwjoh b ojdf ebz"))

def roof_fix(f, r):
    if len(f) != len(r):
        return False

    sticking_up_tiles = "\/"

    for i in range(len(r)):
        if r[i] in sticking_up_tiles and f[i] != " ":
            return False

    return True


# print(roof_fix("  l   f l k djmi k", "___\_____//_____/_"))
# print(roof_fix("    ikm il  h  llmmc   a i", "__\_______________________"))
# print(roof_fix("   h c ", "__/____"))
# print(roof_fix("q h", "_/_"))
# print(roof_fix(" cg dg   em  lfh cdam", "_______/____\_____/_/"))

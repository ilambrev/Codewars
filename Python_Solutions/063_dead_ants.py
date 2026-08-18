def dead_ant_count(ants):
    insect_name = "ant"
    letters = {}

    for l in ants:
        if l in insect_name:
            letters[l] = letters.get(l, 0) + 1

    initial_ants_count = max(letters.values()) if letters else 0
    dead_ants = initial_ants_count - ants.count(insect_name)

    return dead_ants


# print(dead_ant_count("ant ant ant ant"))
# print(dead_ant_count(""))
# print(dead_ant_count(" "))
# print(dead_ant_count("ant anantt aantnt"))
# print(dead_ant_count("ant ant .... a nt"))
# print(dead_ant_count("ant ant ant ant"))
# print(dead_ant_count(""))
# print(dead_ant_count(" "))
# print(dead_ant_count("ant anantt aantnt"))
# print(dead_ant_count("ant ant .... a nt"))
# print(dead_ant_count("antatn ant ant"))
# print(dead_ant_count("ant a ant anatttt"))
# print(dead_ant_count("antantantan"))
# print(dead_ant_count("aaaaannnntttt"))
# print(dead_ant_count("aaaannnnntttt"))
# print(dead_ant_count("aaaannnnttttt"))
# print(dead_ant_count("a n t"))
# print(dead_ant_count("... .. ..."))
# print(dead_ant_count("$$$ant..a"))
# print(dead_ant_count(".n..tt.n.nt..t.ntant..aaaaa..tn.na.aaat..n..tn.ntan.t"))
# print(dead_ant_count("ant ant .... a nt"))

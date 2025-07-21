mistakes = {'5': 'S', '0': 'O', '1': 'I'}

def correct(s):
    for key, value in mistakes.items():
        s = s.replace(key, value)
    
    return s

# print(correct("L0ND0N"))
# print(correct("DUBL1N"))
# print(correct("51NGAP0RE"))
# print(correct("BUDAPE5T"))
# print(correct("PAR15"))
from string import ascii_letters


def calculate(price_dict, transaction):
    transactions = {}
    quantity = ""

    for symbol in transaction:
        if symbol in ascii_letters:
            if quantity:
                transactions.setdefault(symbol, []).append(int(quantity))
                quantity = ""
            else:
                if symbol in transactions and transactions[symbol]:
                    transactions[symbol].pop()
        else:
            quantity += symbol

    return sum([price_dict[k] * sum(v) for k, v in transactions.items()])


# print(calculate({"X":0,"Y":0,"Z":0},"5X6Y20Z1X6Y"))
# print(calculate({"R":1,"Q":2,"E":3,"X":4},"4R1Q4X2E1R2X"))
# print(calculate({"T":12,"F":6},"2F5T1T"))
# print(calculate({"G":1,"M":1,"F":1,"H":1,"J":1},"5J2F7M1H9G6M1H"))
# print(calculate({"E":67},"1E"))
# print(calculate({"X":3,"Y":3,"Z":3},"2X-1Y7X2Z-1Z9Y5X-3Y"))
# print(calculate({"W":12},"9W6W-2W8W5W-4W1W"))
# print(calculate({"X":1,"Y":2,"Z":5},"10X22Y12Z2X"))
# print(calculate({"K":0,"P":2,"B":6,"M":4},"50K10P42B521M4K125B"))
# print(calculate({"A":3,"B":1,"C":4},"3C2B1AC"))
# print(calculate({"D":6,"B":10,"G":2},"5D4GG6B2D1GBD"))
# print(calculate({"A":4,"B":3,"C":2,"D":1},"6D1A3B5A2C3AAAA"))
# print(calculate({"S":12,"I":56,"G":2,"M":1,"A":8}, "5G1S7M2I9A6SMISGAS"))
# print(calculate({"T":1,"V":5},"6TVTT2V"))
# print(calculate({"L":2,"M":4,"N":6,"O":8},"12LO3MLL5L1O4N"))
# print(calculate({"W":2,"D":4},"DWDWDWWD"))

def by_state(st):
    states = {
        "AZ": "Arizona",
        "CA": "California",
        "ID": "Idaho",
        "IN": "Indiana",
        "MA": "Massachusetts",
        "OK": "Oklahoma",
        "PA": "Pennsylvania",
        "VA": "Virginia"
    }

    lines = [a for a in st.split("\n") if a]
    addresses = {}

    for line in lines:
        person_name, street, settlement = [p.strip() for p in line.split(",")]
        state_abbreviation = settlement[-2:]
        town = settlement[:-2].strip()
        state = states[state_abbreviation]
        addresses.setdefault(state, []).append({"name": person_name, "street": street, "town": town})

    addresses = {state: sorted(records, key=lambda r: (r["name"], r["street"], r["town"])) for state, records in sorted(addresses.items(), key=lambda item: item[0])}

    result = []

    for state, records in addresses.items():
        result.append("\r\n".join([state] + [f"..... {r['name']} {r['street']} {r['town']} {state}" for r in records]))

    return "\r\n ".join(result)


# case0 = """John Daggett, 341 King Road, Plymouth MA
# Alice Ford, 22 East Broadway, Richmond VA
# Sal Carpenter, 73 6th Street, Boston MA"""

# case1 = """John Daggett, 341 King Road, Plymouth MA
# Alice Ford, 22 East Broadway, Richmond VA
# Orville Thomas, 11345 Oak Bridge Road, Tulsa OK
# Terry Kalkas, 402 Lans Road, Beaver Falls PA
# Eric Adams, 20 Post Road, Sudbury MA
# Hubert Sims, 328A Brook Road, Roanoke MA
# Amy Wilde, 334 Bayshore Pkwy, Mountain View CA
# Sal Carpenter, 73 6th Street, Boston MA"""


# print(by_state(case0))
# print(by_state(case1))

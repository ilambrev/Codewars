def parse_float(string):
    try:
        if isinstance(string, list):
            return float(",".join(string))
        else:
            return float(string)
    except ValueError:
        return None

# print(parse_float("1.0"))
# print(parse_float("a"))
# print(parse_float("234.0234"))
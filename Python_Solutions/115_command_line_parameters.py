def args_to_string(args):
    result = []

    for a in args:
        if isinstance(a, list):
            if len(a) == 1:
                result.append(a[0])
            elif len(a[0]) == 1:
                result.append(f"-{a[0]} {a[1]}")
            else:
                result.append(f"--{a[0]} {a[1]}")
        else:
            result.append(a)

    return " ".join(result)


# print(args_to_string(["foo"]))
# print(args_to_string(["f"]))
# print(args_to_string([["f"]]))
# print(args_to_string([["foo", "bar"]]))
# print(args_to_string([["f", "bar"]]))
# print(args_to_string([["foo", "bar"], "baz"]))
# print(args_to_string([["foo", "bar"], ["baz", "qux"]]))

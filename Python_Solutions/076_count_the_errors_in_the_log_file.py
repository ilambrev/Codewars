from collections import defaultdict


def map_errors():
    file = open("server.log", "r")
    logs = file.read().split("\n")
    file.close()

    errors = defaultdict(str)

    for log in logs:
        if log.startswith("ERROR: "):
            error = log.replace("ERROR: ", "").lower()
            errors[error] = errors.get(error, 0) + 1

    return dict(sorted(errors.items(), key=lambda x: x[1], reverse=True))


# def write_log(content):
#     with open("server.log", "w") as f:
#         f.write(content)


# write_log("ERROR: Disk_Failure")

# print(map_errors())  # {"disk_failure": 1}


# write_log(
#     "ERROR: Network_Down\n"
#     "ERROR: Timeout\n"
#     "ERROR: Network_Down\n"
#     "ERROR: Timeout\n"
#     "ERROR: Network_Down"
# )

# print(map_errors())  # {"network_down": 3, "timeout": 2}


# write_log(
#     "ERROR: Error_A\n"
#     "ERROR: Error_B\n"
#     "ERROR: Error_A\n"
#     "ERROR: Error_B\n"
#     "ERROR: Error_C"
# )

# print(map_errors())  # {"error_a": 2, "error_b": 2, "error_c": 1}


# write_log(
#     "ERROR: alpha\n"
#     "ERROR: beta\n"
#     "ERROR: beta\n"
#     "ERROR: gamma\n"
#     "ERROR: gamma\n"
#     "ERROR: gamma\n"
#     "ERROR: delta"
# )

# print(map_errors())  # {"gamma": 3, "beta": 2, "alpha": 1, "delta": 1}

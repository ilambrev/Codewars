def find_nth_occurrence(substring, string, occurrence=1):
    start_index = 0
    nth_accurrence_index = 0

    for i in range(1, occurrence + 1):
        try:
            current_index = string.index(substring, start_index)
            nth_accurrence_index = current_index
            start_index = current_index + 1
        except ValueError:
            return -1
        
    return nth_accurrence_index

# string = "This is an example. Return the nth occurrence of example in this example string."

# print(find_nth_occurrence("example", string, 1))
# print(find_nth_occurrence("example", string, 2))
# print(find_nth_occurrence("example", string, 3))
# print(find_nth_occurrence("example", string, 4))
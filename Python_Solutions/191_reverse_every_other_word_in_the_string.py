def reverse_alternate(st):
    words = st.strip().split()

    return " ".join(words[i] if i % 2 == 0 else words[i][::-1] for i in range(len(words)))


# print(reverse_alternate("Did it work?"))
# print(reverse_alternate("I really hope it works this time..."))
# print(reverse_alternate("Reverse this string, please!"))
# print(reverse_alternate("Have a beer"))
# print(reverse_alternate("   "))
# print(reverse_alternate("This is not a test "))
# print(reverse_alternate("This       is a  test "))

def longer(st):
    return " ".join(sorted(st.split(), key=lambda word: (len(word), word)))


# print(longer("Another Green World"))
# print(longer("Darkness on the edge of Town"))
# print(longer("Have you ever Seen the Rain"))
# print(longer("Like a Rolling Stone"))
# print(longer("This will be our Year"))
# print(longer("hello Hello"))

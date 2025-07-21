def esrever(st):
    if st:
        sign = st[len(st) - 1]
        st = st[:-1]
        words = st.split()
        words.reverse()

        for i in range(0, len(words)):
            words[i] = words[i][::-1]

        return ' '.join(words) + sign
    else:
        return st

# print(esrever('an Easy one?'))
# print(esrever('a small lOan OF 1,000,000 $!'))
# print(esrever('<?> &!.".'))
# print(esrever('b3tTer p4ss thIS 0ne.'))
# print(esrever(''))
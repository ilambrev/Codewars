from collections import Counter
import re


def top_3_words(text):
    pattern = r"(?<![a-z'])[a-z']*[a-z][a-z']*(?![a-z'])"
    matches = re.findall(pattern, text.lower(), flags=re.MULTILINE)

    return [k for k, _ in sorted(dict(Counter(matches)).items(), key=lambda word: word[1], reverse=True)][:3]


# print(top_3_words("a a a  b  c c  d d d d  e e e e e"))
# print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
# print(top_3_words("  //wont won't won't "))
# print(top_3_words("  , e   .. "))
# print(top_3_words("  ...  "))
# print(top_3_words("  '  "))
# print(top_3_words("  '''  "))
# print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
#         mind, there lived not long since one of those gentlemen that keep a lance
#         in the lance-rack, an old buckler, a lean hack, and a greyhound for
#         coursing. An olla of rather more beef than mutton, a salad on most
#         nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
#         on Sundays, made away with three-quarters of his income."""))

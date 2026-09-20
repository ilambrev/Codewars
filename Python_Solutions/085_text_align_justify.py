def justify(text, width):
    words = text.split()

    row = ""
    justified_text = []

    for word in words:

        if len(row) + len(word) + 1 > width:
            justified_text.append(row)
            row = ""

        row = f"{row} {word}" if row else f"{row}{word}"

    justified_text.append(row.rstrip())

    for i in range(len(justified_text) - 1):
        row_words = justified_text[i].split()
        diff = width - sum([len(w) for w in row_words])

        if len(row_words) > 1:
            j = 1

            while diff > 0:
                row_words[j] = f" {row_words[j]}"
                diff -= 1
                j = j + 1 if j + 1 < len(row_words) else 1

        justified_text[i] = "".join(row_words)

    return "\n".join(justified_text)


# print(justify("123 45 6", 7))
# print(justify("", 10))

# text = """\
# Lorem  ipsum  dolor  sit amet,
# consectetur  adipiscing  elit.
# Vestibulum    sagittis   dolor
# mauris,  at  elementum  ligula
# tempor  eget.  In quis rhoncus
# nunc,  at  aliquet orci. Fusce
# at   dolor   sit   amet  felis
# suscipit   tristique.   Nam  a
# imperdiet   tellus.  Nulla  eu
# vestibulum    urna.    Vivamus
# tincidunt  suscipit  enim, nec
# ultrices   nisi  volutpat  ac.
# Maecenas   sit   amet  lacinia
# arcu,  non dictum justo. Donec
# sed  quam  vel  risus faucibus
# euismod.  Suspendisse  rhoncus
# rhoncus  felis  at  fermentum.
# Donec lorem magna, ultricies a
# nunc    sit    amet,   blandit
# fringilla  nunc. In vestibulum
# velit    ac    felis   rhoncus
# pellentesque. Mauris at tellus
# enim.  Aliquam eleifend tempus
# dapibus. Pellentesque commodo,
# nisi    sit   amet   hendrerit
# fringilla,   ante  odio  porta
# lacus,   ut   elementum  justo
# nulla et dolor."""

# print(justify(" ".join(text.split()), 30))

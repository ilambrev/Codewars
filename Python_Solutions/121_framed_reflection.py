def mirror(text):
    words = [w[::-1] for w in text.split()]
    max_length = max(len(w) for w in words)
    words = [f"* {w}{' ' * (max_length - len(w))} *" for w in words]
    frame = "*" * (max_length + 4)
    words.insert(0, frame)
    words.append(frame)

    return "\n".join(words)


# print(mirror("Hello World"))
# print(mirror("Codewars"))
# print(mirror("emosewA !ataK"))

def word_count(s: str) -> int:
    excluded_words = {"a", "the", "on", "at", "of", "upon", "in", "as"}
    words = "".join([symbol if symbol.isalpha() else " " for symbol in s.lower()]).split()

    return sum(1 for word in words if word not in excluded_words)


# print(word_count("hello there"))
# print(word_count("hello there and a hi"))
# print(word_count("I'd like to say goodbye"))
# print(word_count("Slow-moving user6463 has been here"))
# print(word_count("%^&abc!@# wer45tre"))
# print(word_count("abc123abc123abc"))
# print(word_count("Really2374239847 long ^&#$&(*@# sequence"))

# long_text = "I'd been using my sphere as a stool. I traced counterclockwise circles on it with my fingertips and it shrank until I could palm it. My bolt had shifted while I'd been sitting. I pulled it up and yanked the pleats straight as I careered around tables, chairs, globes, and slow-moving fraas. I passed under a stone arch into the Scriptorium. The place smelled richly of ink. Maybe it was because an ancient fraa and his two fids were copying out books there. But I wondered how long it would take to stop smelling that way if no one ever used it at all; a lot of ink had been spent there, and the wet smell of it must be deep into everything."
# print(word_count(long_text))

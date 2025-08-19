def like_or_dislike(lst):
    if not lst:
        return 'Nothing'

    is_like_pressed = False
    is_dislike_pressed = False

    for button in lst:
        if button == 'Like':
            is_like_pressed = not is_like_pressed
            is_dislike_pressed = False
        if button == 'Dislike':
            is_dislike_pressed = not is_dislike_pressed
            is_like_pressed = False

    if not is_like_pressed and not is_dislike_pressed:
        return 'Nothing'

    if is_like_pressed:
        return 'Like'

    if is_dislike_pressed:
        return 'Dislike'

# print(like_or_dislike(['Dislike']))
# print(like_or_dislike(['Like', 'Like']))
# print(like_or_dislike(['Dislike', 'Dislike']))
# print(like_or_dislike(['Like', 'Like', 'Like']))
# print(like_or_dislike(['Like', 'Dislike']))
# print(like_or_dislike(['Dislike', 'Like']))
# print(like_or_dislike(['Like', 'Dislike', 'Dislike']))
# print(like_or_dislike(['Dislike', 'Like', 'Dislike']))
# print(like_or_dislike(['Like', 'Like', 'Dislike', 'Like', 'Like', 'Like', 'Like', 'Dislike']))
# print(like_or_dislike([]))
def format_playlist(songs):
    name_field_length = 6
    time_field_length = 6
    artist_field_length = 8

    if songs:
        name_field_length = max(len(song[0]) for song in songs) + 2
        artist_field_length = max(len(song[2]) for song in songs) + 2
        songs.sort(key=lambda song: (song[2], song[0]))

    result = []

    result.append(f"+{'-' * name_field_length}+{'-' * time_field_length}+{'-' * artist_field_length}+")
    result.append(f"| Name {' ' * (name_field_length - 6)}| Time | Artist {' ' * (artist_field_length - 8)}|")
    result.append(result[0])

    for song in songs:
        result.append(f"| {song[0]} {' ' * (name_field_length - len(song[0]) - 2)}| {song[1]} | {song[2]} {' ' * (artist_field_length - len(song[2]) - 2)}|")

    if songs:
        result.append(result[0])

    return "\n".join(result)


# print(format_playlist([]))

# print(format_playlist([('MILK', '4:55', 'BROCKHAMPTON')]))

# print(format_playlist([
#     ('Stoned Again', '3:25', 'King Krule'),
#     ('Serenade', '3:00', 'Travis Scott'),
#     ('I Always Wanna Die (Sometimes)', '5:15', 'The 1975'),
#     ('Stick Talk', '2:54', 'Future'),
#     ('Nightcrawler', '5:22', 'Travis Scott')]))

# print(format_playlist([
#     ('In Da Club', '3:13', '50 Cent'),
#     ('Candy Shop', '3:45', '50 Cent'),
#     ('One', '4:36', 'U2'),
#     ('Wicked', '2:53', 'Future'),
#     ('Cellular', '2:58', 'King Krule'),
#     ('The Birthday Party', '4:45', 'The 1975'),
#     ('In The Night Of Wilderness', '5:26', 'Blackmill'),
#     ('Pull Up', '3:35', 'Playboi Carti'),
#     ('Cudi Montage', '3:16', 'KIDS SEE GHOSTS'),
#     ('What Up Gangsta', '2:58', '50 Cent')]))

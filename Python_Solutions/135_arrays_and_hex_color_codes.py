from collections import Counter


def find_predominant_color_channel(color):
    color_intensity = {
        "Red": int(color[:2], 16),
        "Green": int(color[2:4], 16),
        "Blue": int(color[4:], 16)
    }

    return max(color_intensity, key=color_intensity.get)


def find_major_and_minor_color(colors):
    predominant_channels = Counter([find_predominant_color_channel(color) for color in colors]).most_common(2)
    major_color = predominant_channels[0][0]
    minor_color = minor_color = predominant_channels[1][0] if len(predominant_channels) > 1 else major_color

    return f"{major_color}+{minor_color}"


def get_colors(col_arr):

    return ",".join(find_major_and_minor_color(arr) for arr in col_arr)


# col_arr = [["6B8E23", "9ACD32", "2E8B57", "00008B", "00FF00", "6B8E23", "00FA9A"],
#            ["CD5C5C", "8B0000", "FF0000", "F08080", "98FB98", "DC143C"],
#            ["00BFFF", "00008B", "B22222", "000080", "87CEEB", "4169E1"]]

# print(get_colors(col_arr))


# col_arr = [["FF0000", "191970", "FF0000"],
#            ["556B2F", "98FB98", "2E8B57", "00FF7F", "556B2F", "FFA07A"],
#            ["00BFFF", "00BFFF", "4169E1", "1E90FF", "F08080", "191970"]]

# print(get_colors(col_arr))


# col_arr = [["FF0000", "8DC4DE", "87CEFA", "4169E1", "0000FF"],
#            ["FF0000", "191970", "00008B"],
#            ["CD5C5C", "F08080", "0000FF"]]

# print(get_colors(col_arr))

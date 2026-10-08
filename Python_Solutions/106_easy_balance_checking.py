def clean_row(row, allowed_characters):
    return "".join([s for s in row if s in allowed_characters])


def balance(book):
    allowed_characters = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ."
    rows = [clean_row(r, allowed_characters) for r in book.split("\n") if r]
    initial_balance = float(rows[0])
    expenses_count = len(rows) - 1
    rows[0] = f"Original Balance: {float(rows[0]):.2f}"
    current_balance = initial_balance

    for i in range(1, len(rows)):
        row_parts = rows[i].split()
        expense = float(row_parts[-1])
        current_balance -= expense
        rows[i] = f"{' '.join(row_parts[:-1])} {expense:.2f} Balance {current_balance:.2f}"

    total_expense = initial_balance - current_balance
    average_expense = total_expense / expenses_count

    rows.append(f"Total expense  {total_expense:.2f}")
    rows.append(f"Average expense  {average_expense:.2f}")

    return "\r\n".join(rows)


# b1 = """1000.00!=

# 125 Market !=:125.45
# 126 Hardware =34.95
# 127 Video! 7.45
# 128 Book :14.32
# 129 Gasoline ::16.10
# """

# print(balance(b1))


# b2 = """1233.00
# 125 Hardware;! 24.8?;
# 123 Flowers 93.5
# 127 Meat 120.90
# 120 Picture 34.00
# 124 Gasoline 11.00
# 123 Photos;! 71.4?;
# 122 Picture 93.5
# 132 Tyres;! 19.00,?;
# 129 Stamps 13.6
# 129 Fruits{} 17.6
# 129 Market;! 128.00?;
# 121 Gasoline;! 13.6?;"""

# print(balance(b2))

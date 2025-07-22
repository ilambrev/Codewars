def blow_candles(st):
    blows = 0

    while st:
        st = st.lstrip('0')
        
        if st:
            blows += 1
        else:
            break

        candles = [int(candle) for candle in st]

        for i in range(0, 3 if len(candles) >= 3 else len(candles)):
            if candles[i] > 0:
                candles[i] -= 1

        st = ''.join(list(map(str, candles)))

    return blows

# print(blow_candles("1321"))
# print(blow_candles("0323456"))
# print(blow_candles("2113"))
# print(blow_candles("1110"))
# print(blow_candles("121"))

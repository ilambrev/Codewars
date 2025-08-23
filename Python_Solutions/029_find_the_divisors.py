def divisors(integer):
    divisors = [divisor for divisor in range(2, integer) if integer % divisor == 0]

    if divisors:
        return divisors
    else:
        return f'{integer} is prime'

# print(divisors(15))
# print(divisors(253))
# print(divisors(24))
# print(divisors(25))
# print(divisors(13))
# print(divisors(3))
# print(divisors(29))
def product_fib(_prod):
    fib_nums = [0, 1]
    current_prod = fib_nums[0] * fib_nums[1]

    while current_prod < _prod:
        fib_nums.append(fib_nums[-1] + fib_nums[-2])
        current_prod = fib_nums[-1] * fib_nums[-2]

    return [fib_nums[-2], fib_nums[-1], current_prod == _prod]


# print(product_fib(4895))
# print(product_fib(5895))

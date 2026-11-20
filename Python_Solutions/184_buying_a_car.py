def nb_months(start_price_old, start_price_new, saving_per_month, percent_loss_by_month):
    extra_loss = 0.5
    coeff = (100 - percent_loss_by_month) / 100
    savings = 0
    months = 0

    while start_price_old + savings < start_price_new:
        savings += saving_per_month
        months += 1

        if months % 2 == 0:
            coeff -= extra_loss / 100

        start_price_old *= coeff
        start_price_new *= coeff

    return [months, round((start_price_old + savings) - start_price_new)]


# print(nb_months(2000, 8000, 1000, 1.5))
# print(nb_months(12000, 8000, 1000, 1.5))
# print(nb_months(8000, 12000, 500, 1))
# print(nb_months(18000, 32000, 1500, 1.25))
# print(nb_months(7500, 32000, 300, 1.55))

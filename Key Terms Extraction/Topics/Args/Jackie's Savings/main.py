def final_deposit_amount(*interest, amount=1000):

    money = amount
    for rate in interest:
        money *= (1 + int(rate) / 100)

    return round(money, 2)



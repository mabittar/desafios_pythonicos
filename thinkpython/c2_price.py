def calculator(n, discount=.4):
    price = 25.95
    if discount <= 0 or discount >= 1:
        msg = ("O desconto precisa ser decimal, exemplo .4")
    else:
        new_price = price*(1-discount)

        if n == 1:
            total = new_price + 3
        else:
            total = round(n*(new_price) + (3 + (n-1)*0.75), 2)
        msg = ("O preço total + transporte é: R$ "+str(total))
        return msg


print(calculator(60, .10))
# for n in (1, 2, 6, 10, 60, 100):
#     print(calculator(n))

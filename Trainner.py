#125, 132, 137

products = [
    {'name':'PC', 'price': 2400,},
    {'name':'Mouse', 'price':12,},
    {'name': 'Cellphone', 'price': 1800,},
]

new_product = [
    {**product, 'price': product['price']*1.05}
    for product in products
]

print(*new_product)
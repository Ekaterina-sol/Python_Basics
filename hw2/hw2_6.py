products = []

i = 1
product_count = 3
product_names = []
product_prices = []
product_quantities = []
product_uoms = []
product_name = None
product_price = None
product_quantity = None
product_uom = None
goods = []
product= {}

for i in range(product_count):
    product_name = input(f'Введите название товара {i + 1}: ')
    product_names.append(product_name)
    product_price = input(f'Введите цену товара {i + 1}: ')
    product_prices.append(product_price)
    product_quantity = input(f'Введите количество товара {i + 1}: ')
    product_quantities.append(product_quantity)
    product_uom = input(f'Введите единицу измерения товара {i + 1}: ')
    product_uoms.append(product_uom)
    product = {
        "название": product_name,
        "цена": product_price,
        "количество": product_quantity,
        "ед": product_uom,
    }
    goods.append((i+1, product))
    i += 1

print("Товары:", goods)

prod_analytic = {
    "название": product_names,
    "цена": product_prices,
    "количество": product_quantities,
    "ед": product_uoms,
}

print("Аналитика товаров: ", prod_analytic)
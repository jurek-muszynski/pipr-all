# Zadanie 1
def iterator():
    for i in range(1, 101):
        if (i % 15 == 0):
            print("fizzbuzz")
        elif (i % 5 == 0):
            print("buzz")
        elif (i % 3 == 0):
            print("fizz")
        else:
            print(i)

# Zadanie 2


def list_reverse(list):
    return list[::-1][1::3]

# Zadanie 3


def fibonacci(n):
    if (n == 1 or n == 2):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Zadanie 4


available_products = {
    "Bananas": (499, "B"),
    "Oranges": (1803, "B"),
    "Milk": (315, "A"),
    "Lollipop": (100, "E")
}

tax_groups = {
    "A": 0.12,
    "B": 0.08,
    "E": 0.22
}

receipt = [
    ("Bananas", 1),
    ("Oranges", 1),
    ("Milk", 1),
    ("Lollipop", 1)
]


def split_price(price):
    return f"{price//100}.{price%100:02}"


def tax_group_mapper(name):
    return available_products[name][1]


def tax_mapper(product):
    return (price_mapper(product) * tax_groups[tax_group_mapper(product[0])])


def price_mapper(product):
    name, amount = product
    return available_products[name][0] * amount


def print_product(n, product):
    name, amount = product
    tax_group = tax_group_mapper(name)
    price = price_mapper(product)
    print(f"{n}. {name:<8}{split_price(price):>17} {tax_group}")


def print_receipt(date,  products):
    total = 0
    tax = 0
    print(date)
    for i in range(len(products)):
        print_product(i+1, products[i])
        total += price_mapper(products[i])
        tax += tax_mapper(products[i])
    print("-"*30)
    print(f"TOTAL:{split_price(total):>24}")
    print(f"TAX:{split_price(int(tax)):>26}")
    print(f"TOTAL+TAX:{split_price(int(tax)+total):>20}")


if (not receipt):
    print("Empty receipt")
else:
    print_receipt("22-10-2023", receipt)

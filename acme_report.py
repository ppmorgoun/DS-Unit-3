from acme import Product
import numpy as np

name_dict = {
    'adjective': [
        'Awesome',
        'Shiny',
        'Impressive',
        'Portable',
        'Improved'],
    'noun': [
        'Anvil',
        'Catapult',
        'Disguise',
        'Mousetrap',
        '???']}


def generate_products(num=30):
    """This function generates a number (default 30) of products from the Products class in mymodule.acme
    Returns a list of Product objects"""
    products = []
    for i in range(num):
        name = np.random.choice(
            name_dict['adjective']) + ' ' + np.random.choice(name_dict['noun'])
        price = np.random.randint(5, 100)
        weight = np.random.randint(5, 100)
        flammability = np.random.uniform(0.0, 2.5)
        products.append(
            Product(
                name=name,
                price=price,
                weight=weight,
                flammability=flammability))
    return products


def inventory_report(products):
    """This function generates an inventory report with aggregate statistics, from a list of Product objects.
    Prints some strings"""
    names = [i.name for i in products]
    prices = [i.price for i in products]
    weights = [i.weight for i in products]
    flammabilities = [i.flammability for i in products]
    print(f'ACME CORPORATION OFFICIAL INVENTORY REPORT\n'
          f'Number of unique product names: {len(set(names))}\n'
          f'Average price: {sum(prices) / len(prices)}\n'
          f'Average weight: {sum(weights) / len(weights)}\n'
          f'Average flammability: {sum(flammabilities) / len(flammabilities)}')


if __name__ == '__main__':
    inventory_report(generate_products())

import pytest
from acme import Product
from acme_report import generate_products, name_dict


def test_default_product_price():
    """Tests that the default price of a Product object is 10"""
    prod = Product('Test')
    assert prod.price == 10


def test_default_product_weight():
    """Tests that the default weight of a Product object is 20"""
    prod = Product('Test')
    assert prod.weight == 20


def test_stealability():
    """Tests that the stealability of a product is evaluated correctly"""
    prod1 = Product(name='Test', price=1, weight=10)
    prod2 = Product(name='Test', price=9, weight=10)
    prod3 = Product(name='Test', price=100, weight=10)
    assert prod1.stealability() == "Not so stealable..."
    assert prod2.stealability() == "Kinda stealable."
    assert prod3.stealability() == "Very stealable!"


def test_explode():
    """Tests that the explodability of a product is evaluated correctly"""
    prod1 = Product(name='Test', weight=10, flammability=0.1)
    prod2 = Product(name='Test', weight=10, flammability=1)
    prod3 = Product(name='Test', weight=10, flammability=10)
    assert prod1.explode() == '...fizzle.'
    assert prod2.explode() == '...boom!'
    assert prod3.explode() == '...BABOOM!!'


def test_default_num_products():
    """Tests that the default number of products generated by the generate_products functions is 30"""
    products = generate_products()
    assert len(products) == 30


def test_legal_names():
    """Tests that the randomly generated names made by the generate_products function are made up of names
    provided in the name_dict dictionary"""
    products = generate_products()
    for i in products:
        a, b = i.name.split()
        assert a in name_dict['adjective']
        assert b in name_dict['noun']

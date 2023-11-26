import pizzeria.menu as menu
import pytest


def test_pizza_creation_1():
    p = menu.Pepperoni()
    expect_recipe = ['tomato sauce', 'mozzarella', 'pepperoni']
    assert expect_recipe == p.recipe


def test_pizza_creation_2():
    with pytest.raises(ValueError):
        menu.Pepperoni(size='dsjnfm')


def test_set_size():
    p = menu.Pepperoni()
    assert p.size == 'L'
    p.set_size('XL')
    assert p.size == 'XL'


def test_baking():
    p = menu.Pepperoni()
    assert not p.is_baked
    p.bake()
    assert p.is_baked


def test_str():
    p = menu.Pepperoni()
    assert str(p) == 'Pepperoni: tomato sauce, mozzarella, pepperoni'


def test_equality():
    a = menu.Pepperoni()
    b = menu.Margherita()
    c = menu.Pepperoni()
    assert a != b
    assert a == c
    c.set_size('XL')
    assert a != c


def test_dict():
    p = menu.Pepperoni()
    assert sorted(p.dict()) == sorted({'tomato sauce': 1,
                                       'mozzarella': 1,
                                       'pepperoni': 1})


def test_menu_1():
    m = menu.Menu()
    assert m.sizes == ['L', 'XL']


def test_menu_2():
    m = menu.Menu()
    a = '-- Margherita: tomato sauce, mozzarella, tomatoes'
    b = '\n-- Pepperoni: tomato sauce, mozzarella, pepperoni'
    c = '\n-- Hawaiian: tomato sauce, mozzarella, chicken, pineapples'
    assert str(m) == a + b + c

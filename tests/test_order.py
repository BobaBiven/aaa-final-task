import pizzeria.order as order
import pizzeria.menu as menu
import pytest


def test_pizza_creation_func_1():
    p = order.create_pizza('Pepperoni', 'XL')
    expect_recipe = ['tomato sauce', 'mozzarella', 'pepperoni']
    assert expect_recipe == p.recipe


def test_pizza_cration_func_2():
    with pytest.raises(ValueError):
        order.create_pizza(name='Pepperoni', size='dsjnfm')


def test_pizza_creation_func_3():
    p = order.create_pizza('Pepperoni', 'L')
    assert p == menu.Pepperoni('L')


def test_order_creation():
    op = order.Order('Pepperoni', 'L').ordered_pizza
    assert op == menu.Pepperoni('L')


def test_deliver():
    op = order.Order('Pepperoni', 'L')
    op.deliver()
    assert op.is_delivered

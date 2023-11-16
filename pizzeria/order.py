import pizzeria.menu as menu
from pizzeria.decorators import log


def create_pizza(name: str, size: str):
    if size not in ('L', 'XL'):
        raise ValueError('Only avaliable in L or XL!!!')

    if name not in ('Margherita', 'Pepperoni', 'Hawaiian'):
        raise ValueError('There is no such pizza in menu!!!')

    if name == 'Margherita':
        return menu.Margherita(size)

    if name == 'Pepperoni':
        return menu.Pepperoni(size)

    if name == 'Hawaiian':
        return menu.Hawaiian(size)


class Order:

    ordered_pizza: menu.Pizza
    is_delivered: bool

    def __init__(self, name: str, size: str) -> None:

        self.ordered_pizza = create_pizza(name, size)
        self.delivered = False

    @log('Baked for: {}')
    def bake(self) -> None:
        self.ordered_pizza.bake()

    @log('Delivered for: {}')
    def deliver(self) -> None:
        self.is_delivered = True

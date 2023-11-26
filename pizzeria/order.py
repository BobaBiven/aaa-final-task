import pizzeria.menu as menu
from pizzeria.decorators import log


def create_pizza(name: str, size: str):
    """
    Create a Pizza object with specified name and size.

    Args:
    - name (str): The name of the pizza.
    - size (str): The size of the pizza.

    Returns:
    - An instance of the Pizza class with the specified name and size.

    Raises:
    - ValueError: If the pizza with this size/name doesn't exist.
    """
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
    """
    A class representing an order of a pizza.

    Attributes:
    - ordered_pizza (menu.Pizza): The Pizza object representing ordered pizza.
    - is_delivered (bool): Indicates if the order has been delivered or not.

    Methods:
    - __init__(self, name: str, size: str) -> None: Initializes a Order object.
    - bake(self) -> None: Bakes the ordered pizza.
    - deliver(self) -> None: Delivers order.

    Decorators:
    - @log('Baked for: {}'): Logs the time it took to bake the pizza.
    - @log('Delivered for: {}'): Logs the time it took to deliver the pizza.
    """

    is_delivered: bool
    ordered_pizza: menu.Pizza

    def __init__(self, name: str, size: str) -> None:
        """
        Initializes an Order object with the specified name and size.

        Args:
        - name (str): The name of the pizza.
        - size (str): The size of the pizza.
        """
        self.ordered_pizza = create_pizza(name, size)
        self.delivered = False

    @log('Baked for: {} seconds')
    def bake(self) -> None:
        """
        Bake the ordered pizza.
        """
        self.ordered_pizza.bake()

    @log('Delivered for: {} seconds')
    def deliver(self) -> None:
        """
        Deliver order.
        """
        self.is_delivered = True

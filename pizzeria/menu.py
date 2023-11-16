class Pizza:
    """
    A class representing a Pizza.

    Attributes:
    - size (str): The size of the pizza ('L' or 'XL').
    - recipe (list): The list of ingredients for the pizza.
    - is_baked (bool): Indicates if the pizza has been baked or not.

    Methods:
    - __init__(self, size='L'): Creates pizza with the specified size.
    - set_size(self, new_size) -> None: changes the size of the pizza.
    - bake(self) -> None: bakes the pizza.
    - __eq__(self, other) -> bool: compares two Pizza (size, recipe).
    - __str__(self) -> str: Returns a string representation of the Pizza.
    - dict(self) -> dict: Returns a dictionary representation of the Pizza.
    """

    size: str
    recipe: list
    is_baked: bool

    def __init__(self, size='L'):
        if size not in ('L', 'XL'):
            raise ValueError('Only avaliable in L or XL!!!')
        self.size = size
        self.is_baked = False

    def set_size(self, new_size: str) -> None:
        self.size = new_size

    def bake(self) -> None:
        self.is_baked = True

    def __eq__(self, other) -> bool:
        return self.size == other.size and self.recipe == other.recipe

    def __str__(self) -> str:
        tmp_str = ', '.join(self.recipe)
        return f'{self.__class__.__name__}: {tmp_str}'

    def dict(self) -> dict:
        dict_recipe = {}
        for element in self.recipe:
            dict_recipe[element] = 1
        return dict_recipe


class Margherita(Pizza):
    """
    A class representing a Margherita pizza.
    """
    recipe = [
              'tomato sauce',
              'mozzarella',
              'tomatoes'
             ]


class Pepperoni(Pizza):
    """
    A class representing a Pepperoni pizza.
    """
    recipe = [
              'tomato sauce',
              'mozzarella',
              'pepperoni'
             ]


class Hawaiian(Pizza):
    """
    A class representing a Hawaiian pizza.
    """
    recipe = [
              'tomato sauce',
              'mozzarella',
              'chicken',
              'pineapples'
             ]


class Menu:
    """
    A class representing a Menu of pizzas.

    Attributes:
    - pizzas (dict): A dictionary of pizzas on the menu {'name': PizzaObject}.
    - sizes (list): A list of available sizes for the pizzas.

    Methods:
    - __init__(self): Creates a Menu object with possible pizzas and sizes.
    - __str__(self): Returns a string representation of the Menu object.
    """
    def __init__(self):
        self.pizzas = {
                       'Margherita': Margherita(),
                       'Pepperoni': Pepperoni(),
                       'Hawaiian': Hawaiian()
                      }

        self.sizes = ['L', 'XL']

    def __str__(self):
        out = '\n'.join('-- ' + str(self.pizzas[key]) for key in self.pizzas)
        return out

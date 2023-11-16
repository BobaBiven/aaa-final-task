class Pizza:

    size: str
    recipe: list
    is_baked: bool

    def __init__(self, size='L'):
        if size not in ('L', 'XL'):
            raise ValueError('Only avaliable in L or XL!!!')
        self.size = size
        self.is_baked = False

    def set_size(self, new_size) -> None:
        self.size = new_size

    def bake(self) -> None:
        self.is_baked = True

    def __eq__(self, other) -> bool:
        return self.size == other.size and self.recipe == other.recipe

    def __str__(self):
        tmp_str = ', '.join(self.recipe)
        return f'{self.__class__.__name__}: {tmp_str}'

    def dict(self) -> dict:
        dict_recipe = {}
        for element in self.recipe:
            dict_recipe[element] = 1
        return dict_recipe


class Margherita(Pizza):

    recipe = [
              'tomato sauce',
              'mozzarella',
              'tomatoes'
             ]


class Pepperoni(Pizza):

    recipe = [
              'tomato sauce',
              'mozzarella',
              'pepperoni'
             ]


class Hawaiian(Pizza):

    recipe = [
              'tomato sauce',
              'mozzarella',
              'chicken',
              'pineapples'
             ]


class Menu:

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

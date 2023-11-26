import click
import pizzeria.menu
import pizzeria.order


@click.group()
def cli() -> None:
    """Entry point"""
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.option('--large', default=False, is_flag=True)
@click.argument('pizza_name')
def order(pizza_name: str, large: bool, delivery: bool) -> None:
    """
    Place an order for a pizza.

    Args:
    - pizza_name (str): name of the ordered pizza.

    Options:
    -- delivery (bool): delivers a pizza to you.
    -- large (bool): changes size from default 'L' to 'XL'.
    """

    if large:
        size = 'XL'
    else:
        size = 'L'

    order = pizzeria.order.Order(pizza_name, size)

    if delivery:
        order.bake()
        order.deliver()

    else:
        order.bake()

    print('Thank you for staying with us!')
    print(f'Hopefully you love you {size}-sized {pizza_name}.')


@cli.command()
def menu() -> None:
    """
    Display the pizza menu.
    """
    m = pizzeria.menu.Menu()
    print(m)
    sizes = ', '.join(m.sizes)
    print(f'Possible size: {sizes}')


if __name__ == '__main__':
    cli()

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_continue = True
while is_continue:
    user_prompt = input(f"What would you like? ({menu.get_items()}) ")

    if user_prompt == 'report':
        coffee_maker.report()
        money_machine.report()
    elif user_prompt == 'off':
        is_continue = False
    else:
        coffee = menu.find_drink(user_prompt)
        if coffee_maker.is_resource_sufficient(coffee) and money_machine.make_payment(coffee.cost):
            coffee_maker.make_coffee(coffee)





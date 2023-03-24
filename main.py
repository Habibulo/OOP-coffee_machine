from menu import Menu, MenuItem
from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
profit = 0
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
report = [coffee_maker, money_machine]
menu = Menu()

money_machine.report()
coffee_maker.report()

is_on = True
while is_on:
    # options = menu.get_items()
    choice = input(f"What would you like? {menu.get_items()}: ")

    if choice == 'off':
        is_on = False
    elif choice == 'report':
        money_machine.report()
        coffee_maker.report()

    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            payment = money_machine.make_payment(drink.cost)
            if payment:
                coffee_maker.make_coffee(drink)
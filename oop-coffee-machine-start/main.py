from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True

menu_items = Menu()
coffee_machine = CoffeeMaker()
money = MoneyMachine()

while machine_on:
    request = input(f"What would you like? ({menu_items.get_items()}): ")

    if request == "off":
        print("Turning machine off")
        machine_on = False
    else:
        if request == 'report':
            coffee_machine.report()
            money.report()
        else:
            if coffee_machine.is_resource_sufficient(menu_items.find_drink(request)):
                if money.make_payment(menu_items.find_drink(request).cost):
                    coffee_machine.make_coffee(menu_items.find_drink(request))


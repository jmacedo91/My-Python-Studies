from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
coffee = Menu()
resource = CoffeeMaker()
money = MoneyMachine()

while is_on:
    choice = input(f"What would you like? ({coffee.get_items()}): ").lower()
    if choice == "off":
        is_on = False
    # TODO Print Report
    elif choice == "report":
        resource.report()
        money.report()
    # TODO Check Resources Sufficient?
    else:
        drink = coffee.find_drink(choice)
        if resource.is_resource_sufficient(drink):
            # TODO Process Coins
            # TODO Check Transaction Sucessful?
            if money.make_payment(drink.cost):
            # TODO Make Coffee
                resource.make_coffee(drink)

from data import MENU, resources


def calculate_money():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many quarters?: "))
    total_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total_money


def report():
    """Returns the total resources."""
    print(f"Water: {resources['water']}mL.")
    print(f"Milk: {resources['milk']}mL.")
    print(f"Coffee: {resources['coffee']}g.")
    print(f"Money: ${money}.")


def check_resources():
    """Checks the resource stock."""
    for resource in resources:
        if MENU[coffee]["ingredients"][resource] > resources[resource]:
            print(f"Sorry there is not enough {resource}.")
            return False
    return True


is_turn_off = False
money = 0

while not is_turn_off:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee in MENU:
        if check_resources():
            total = calculate_money()
            if total < MENU[coffee]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            else:
                money += MENU[coffee]["cost"]
                resources["water"] -= MENU[coffee]["ingredients"]["water"]
                resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
                resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
                print(f"Here is your {coffee} ☕. Enjoy!")
                if total > MENU[coffee]["cost"]:
                    change = total - MENU[coffee]["cost"]
                    print(f"Here is ${round(change, 2)} dollars in change.")
    elif coffee == "report":
        report()
    elif coffee == "off":
        is_turn_off = True
    else:
        print("Sorry, invalid command.")

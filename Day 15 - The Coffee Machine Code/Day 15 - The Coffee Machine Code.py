from data import MENU, resources

is_turn_off = False
money = 0


def calculate_money():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many quarters?: "))
    total_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total_money


def report():
    print(f"Water: {resources['water']}mL.")
    print(f"Milk: {resources['milk']}mL.")
    print(f"Coffee: {resources['coffee']}g.")
    print(f"Money: ${money}.")


def check_resources(resource):
    if MENU[coffee]["ingredients"][resource] > resources[resource]:
        print(f"Sorry there is not enough {resource}.")


while not is_turn_off:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee in MENU:
        for resource in resources:
            check_resources(resource)
        total = calculate_money()
        if total < MENU[coffee]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            money += MENU[coffee]["cost"]
            resources["water"] -= MENU[coffee]["ingredients"]["water"]
            resources["milk"] -= MENU[coffee]["ingredients"]["milk"]
            resources["coffee"] -= MENU[coffee]["ingredients"]["coffee"]
            print(f"Here is your {coffee}. Enjoy!")
            if total > MENU[coffee]["cost"]:
                change = total - MENU[coffee]["cost"]
                print(f"Here is ${round(change, 2)} dollars in change.")
    elif coffee == "report":
        report()
    elif coffee == "off":
        is_turn_off = True

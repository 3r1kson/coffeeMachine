MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

money = {"Money": 0}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_on = True

def getCoffe(coffee):
    resources['water'] -= MENU[coffee]['ingredients']['water']
    resources['milk'] -= MENU[coffee]['ingredients']['milk'] if MENU[coffee]['ingredients'].get('milk') else 0
    resources['coffee'] -= MENU[coffee]['ingredients']['coffee']

    print(f"Here is your {coffee}. Enjoy!")

def checkResources(coffee):
    if resources['water'] < MENU[coffee]['ingredients']['water']:
        print("Sorry there is not enough water.")
        return False

    if coffee != 'espresso':
        if resources['milk'] < MENU[coffee]['ingredients']['milk']:
            print("Sorry there is not enough milk.")
            return False

    if resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
        print("Sorry there is not enough coffee.")
        return False

    return True

def report():
    for key in resources:
        print(f"{key}: {resources[key]}")
    print(f"Money: ${money['Money']}")

def requestPayment(coffee):
    print("Please insert coins.")
    value = MENU[coffee]['cost']
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01

    received = quarters + dimes + nickles + pennies

    if received > value:
        change = round(received - value, 2)
        print(f"Here is ${change} dollars in change.")
        money['Money'] += value
        return True
    elif received == value:
        money['Money'] += value
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

while machine_on:
    request = input("What would you like? (espresso/latte/cappuccino):").lower()

    if request == 'off':
        print("Turning machine off.")
        machine_on = False
    else:
        if request == 'report':
            report()
        elif checkResources(request):
            if requestPayment(request):
                getCoffe(request)
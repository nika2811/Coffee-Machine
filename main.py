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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# TODO: 4. Check resources sufficient?
def check(var):
    if var == "latte" or var == "cappuccino":
        if MENU[var]["ingredients"]["water"] <= resources["water"] and MENU[var]["ingredients"]["milk"] <= resources["milk"] and MENU[var]["ingredients"]["coffee"] <= resources["coffee"]:
            return True
        else:
            if MENU[var]["ingredients"]["water"] > resources["water"]:
                print("Sorry there is not enough water.")
                return False
            elif MENU[var]["ingredients"]["coffee"] > resources["coffee"]:
                print("Sorry there is not enough coffee.")
                return False
            elif MENU[var]["ingredients"]["milk"] > resources["milk"]:
                print("Sorry there is not enough milk.")
                return False
    elif var == "espresso":
        if MENU[var]["ingredients"]["water"] <= resources["water"] and MENU[var]["ingredients"]["coffee"] <= resources["coffee"]:
            return True
        else:
            if MENU[var]["ingredients"]["water"] > resources["water"]:
                print("Sorry there is not enough water.")
                return False
            elif MENU[var]["ingredients"]["coffee"] > resources["coffee"]:
                print("Sorry there is not enough coffee.")
                return False


in_on = True
money = 0


while in_on:

    sum_coins = 0

    # TODO: 1. Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”

    input1 = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if input1 == "off":
        exit()

    # TODO: 3. Print report.
    if input1 == "report":
        print(f'Water:{resources["water"]}ml \nMilk:{resources["milk"]}ml \ncoffee:{resources["coffee"]}g \nMoney: ${money} ')
        continue

    # TODO: 5. Process coins.
    if check(input1):
        print("Please Insert Coins.")
        quarter = int(input("how many quarters?: "))
        dime = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennie = int(input("how many pennies?: "))

        sum_coins += quarter * 0.25 + dime * 0.10 + nickles * 0.05 + pennie * 0.01
        sum_coins = round(sum_coins, 2)
        print(f"Your current balance: {sum_coins}")

    # TODO: 6. Check transaction successful?
        if sum_coins > MENU[input1]["cost"]:
            change = sum_coins - MENU[input1]["cost"]
            change = round(change, 2)
            print(f"Here is {change} dollars in change")

            money += (sum_coins - change)

            if sum_coins == MENU[input1]["cost"]:
                money += sum_coins

        elif sum_coins < MENU[input1]["cost"]:
            print("Sorry that's not enough money. Money refunded.")
    else:
        continue

    # TODO: 7. Make Coffee.
    if check(input1) and MENU[input1]["cost"] <= sum_coins:
        if input1 == "espresso":
            resources["water"] -= MENU[input1]["ingredients"]["water"]
            resources["coffee"] -= MENU[input1]["ingredients"]["coffee"]
        elif input1 == "latte" or input1 == "cappuccino":
            resources["water"] -= MENU[input1]["ingredients"]["water"]
            resources["coffee"] -= MENU[input1]["ingredients"]["coffee"]
            resources["milk"] -= MENU[input1]["ingredients"]["milk"]

        print(f"Here is your {input1} ☕. Enjoy!.")

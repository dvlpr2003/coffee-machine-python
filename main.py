MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    },
}

resource = {"water": 300, "milk": 200, "coffee": 100, "money": "$0"}

operation = True
total_coins = 0

while operation:
    select_option = input("What would you like? (espresso/latte/cappuccino): ")

    if select_option == "espresso":
        # water
        water = MENU["espresso"]["ingredients"]["water"]
        coffee = MENU["espresso"]["ingredients"]["coffee"]

        cost = MENU["espresso"]["cost"]

        if water <= resource["water"] and coffee <= resource["coffee"]:
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            print(f"Here is ${round(total,2)} in change.")

            if cost <= total:
                print("enjoy")
            else:
                print("you don't have enough coins.")
                continue

        else:
            if water >= resource["water"]:
                print(f"Sorry there is not enough {water}")
                operation = False
            else:
                print(f"Sorry there is not enough {coffee}")
                operation = False
        resource["water"] -= water
        resource["coffee"] -= coffee
    elif select_option == "latte":
        water = MENU["latte"]["ingredients"]["water"]
        coffee = MENU["latte"]["ingredients"]["coffee"]

        cost = MENU["latte"]["cost"]
        milk = MENU["latte"]["ingredients"]["milk"]
        if (
            water <= resource["water"]
            and coffee <= resource["coffee"]
            and resource["milk"]
        ):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            print(f"Here is ${round(total,2)} in change.")

            if cost <= total:
                print("enjoy")
            else:
                print("you don't have enough coins.")
                continue

        else:
            if water > resource["water"]:
                print("Sorry there is not enough water")
                operation = False
            elif milk > resource["milk"]:
                print("Sorry there is not enough milk")
                operation = False
            else:
                print("Sorry there is not enough coffee")
                operation = False
        resource["water"] -= water
        resource["coffee"] -= coffee
        resource["milk"] -= milk
    elif select_option == "cappuccino":
        water = MENU["cappuccino"]["ingredients"]["water"]
        coffee = MENU["cappuccino"]["ingredients"]["coffee"]

        cost = MENU["cappuccino"]["cost"]
        milk = MENU["cappuccino"]["ingredients"]["milk"]
        if (
            water <= resource["water"]
            and coffee <= resource["coffee"]
            and resource["milk"]
        ):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickles = int(input("How many nickles?: "))
            pennies = int(input("How many pennies?: "))

            total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            print(f"Here is ${round(total,2)} in change.")

            if cost <= total:
                print("enjoy")
            else:
                print("you don't have enough coins.")
                continue

        else:
            if water > resource["water"]:
                print("Sorry there is not enough water")
                operation = False
            elif milk > resource["milk"]:
                print("Sorry there is not enough milk")
                operation = False
            else:
                print("Sorry there is not enough coffee")
                operation = False
        resource["water"] -= water
        resource["coffee"] -= coffee
        resource["milk"] -= milk
    elif select_option == "report":
        for i in resource:
            print(f"{i}: {resource[i]}")
    else:
        print("please select valid option")
        operation = False

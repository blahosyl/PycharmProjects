MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

money = 0

switch_off = False

# TODO 1: Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
while switch_off == False:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    choice = choice.lower()

    # TODO 8: if the user enters something not defined, prompt them again
    while not choice == "report" and not choice == "off" and not choice == "espresso" and not choice == "latte" and not choice == "cappuccino":
        choice = input("I did not understand. Choose one of the following: espresso/latte/cappuccino: ")
    # TODO 3: Print report.
    if choice == "report":
        print(f'Water: {resources["water"]}ml')
        print(f'Milk: {resources["milk"]}ml')
        print(f'Coffee: {resources["coffee"]}g')
        print(f'Money: ${money}')
    # TODO 2: Turn off the Coffee Machine by entering “off” to the prompt
    elif choice == "off":
        print("Turning off")
        switch_off = True
    else:
        drink = MENU[choice]
        #print(drink)
        # TODO 4: Check resources sufficient?
        water_available = resources["water"]
        milk_available = resources["milk"]
        coffee_available = resources["coffee"]
        water_needed = drink["ingredients"]["water"]
        milk_needed = drink["ingredients"]["milk"]
        coffee_needed = drink["ingredients"]["coffee"]
        if water_available < water_needed:
            print("Sorry, there is not enough water.")
        elif milk_available < milk_needed:
            print("Sorry, there is not enough milk.")
        elif coffee_available < coffee_needed:
            print("Sorry, there is not enough coffee.")
        else:
            # TODO 5: Process coins.
            print("Please insert coins.")
            quarters = int(input("How many quarters? "))
            dimes = int(input("How many dimes? "))
            nickels = int(input("How many nickels? "))
            pennies = int(input("How many pennies? "))
            coins = round(quarters*0.25+dimes*0.1+nickels*0.05+pennies*0.01, 2)
            cost = round(drink["cost"], 2)
            print(f"You inserted ${coins}. The {choice} costs ${cost}.")
            # TODO 6: Check transaction successful?
            if coins < cost:
                print(f"Sorry, that's not enough money. Here is your refund of {coins}.")
            else:
                # TODO 7: Make Coffee.
                print(f"Here is your {choice} ☕️. Enjoy!")
                money += cost
                if coins > cost:
                    print(f"Here is your change of {round(coins-cost, 2)}.")
                resources["water"] -= water_needed
                resources["milk"] -= milk_needed
                resources["coffee"] -= coffee_needed
                #print(f"Updated resources: {resources}")
                #print(f"Updated money in machine: {money}")



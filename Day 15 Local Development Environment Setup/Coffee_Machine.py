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
    "money": 0,
}

def coffe_machine():
    # TODO-1 : Asking user would like?
    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO-2 : off machine
        if user_input == "off":
            print("Machine shutdown!")
            break

        elif user_input == "report":
            report()

        else:
            is_sufficient = check_sufficient(resources, MENU[user_input]["ingredients"])
            if is_sufficient:
                user_pay = calculate_coins()
                is_enough = check_paying(user_pay, MENU[user_input]["cost"])
                if is_enough:
                    user_order = MENU[user_input]["ingredients"]
                    make_coffe(user_order)
                    print(f"Here is your {user_input}. Enjoy! ☕")
            else:
                for i in resources:
                    for j in MENU[user_input]["ingredients"]:
                        if i == j:
                            if resources[i] < MENU[user_input]["ingredients"][j]:
                                print(f"Sorry there is not enough {j}")





# TODO-3 : Print report
def report():
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: ${resources['money']}")

# TODO-4 : check resources sufficient
def check_sufficient(resource, menu):
    for i in resource:
        for j in menu:
            if i == j:
                if resource[i] < menu[j]:
                    return False
                else:
                    return True

# TODO-5 : Process coin
def calculate_coins():
    print("Please insert coins.")
    quarters = int(input("Enter your quarters: "))
    dimes = int(input("Enter your dimes: "))
    nickles = int(input("Enter your nickles: "))
    pennies = int(input("Enter your pennies: "))
    calculate = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    return calculate

# TODO-6 : Transaction
def check_paying(paying, cost):
    if paying < cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        resources["money"] += cost
        if paying > cost:
            change = round((paying - cost), 2)
            print(f"Here is ${change} dollars in change")
        return True

# TODO-7 : Making Coffe
def make_coffe(order):
    for k in order:
        for l in resources:
            if k == l:
                resources[l] -= order[k]

coffe_machine()






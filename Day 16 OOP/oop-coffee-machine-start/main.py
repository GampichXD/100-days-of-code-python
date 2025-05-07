from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def welcome():
    print('''\033[33m
             )))
            (((
          +-----+
          |     |] - WELCOME TO THE COFFEE MACHINE!
          `-----'

          ------ MENU ------
          Espresso ($1.50)
          Latte ($2.50)
          Cappuccino ($3.00)
          ------------------

          PS: Type "report" at any moment
          to check our resources available.
          Type "off" to log out from the machine.\033[m
        ''')

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
is_on = True



while is_on:
    welcome()
    option = menu.get_items()
    ask = input(f"What would you like? {option}: ")
    if ask == "off":
        print("Thanks For Use Me >///<")
        is_on = False
    elif ask == "report":
        coffee_maker.report()
        money_machine.report()
    elif menu.find_drink(ask) is None:
        print('\033[31mError. Please choose an available option.\033[m')
    else:
        drink = menu.find_drink(ask)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)





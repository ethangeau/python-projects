from data import resource, coffee_types, coin_types


def resource_checker(coffee_type):
    if resource['water'] < coffee_type['water']:
        print("Sorry there is not enough water.")
        return False
    elif resource['coffee'] < coffee_type['coffee']:
        print("Sorry there is not enough coffee.")
        return False
    elif resource['milk'] < coffee_type['milk']:
        print("Sorry there is not enough milk.")
        return False
    return True


def transaction(coffee_type, total_money):
    global resource
    for key in resource:
        resource[key] -= coffee_type[key]
    return round(total_money - coffee_type['money'], 2)


def machine():
    is_continue = True
    while is_continue:
        prompt_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

        is_sufficient = False
        if prompt_coffee == 'off':
            is_continue = False
        elif prompt_coffee == 'report':
            print(f"""Water: {resource['water']}ml
Milk: {resource['milk']}ml
Coffee: {resource['coffee']}g
Money: ${resource['money']}""")
        else:
            coffee_type = coffee_types[prompt_coffee]
            is_sufficient = resource_checker(coffee_type)

        if is_sufficient:
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many dimes?: "))
            nickles = int(input("how many nickles?: "))
            pennies = int(input("how many pennies?: "))
            total_money = coin_types['quarter'] * quarters + coin_types['dime'] * dimes\
                          + coin_types['nickel'] * nickles + coin_types['penny'] * pennies

            if total_money < abs(coffee_type['money']):
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = transaction(coffee_type, total_money)
                if change > 0:
                    print(f"Here is ${change} dollars in change.")
                    print(f"Here is your {prompt_coffee}. Enjoy!")


machine()

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class CoffeeMachine:
    def __init__(self):
        self.menu = {
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
                "cost": 3.0
            }
        }

        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

        self.money = 0

    # Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    # a. Check the user’s input to decide what to do next.
    # b. The prompt should show every time action has completed, e.g. once the drink is
    # dispensed. The prompt should show again to serve the next customer.
    def get_user_req(self):
        req = input("What would you like? (espresso/latte/cappuccino):")
        if (req in self.menu.keys()) or (req == "off") or (req == "report"):
            return req
        else:
            self.get_user_req()

    # Print report.
    # a. When the user enters “report” to the prompt, a report should be generated that shows
    # the current resource values. e.g.
    def get_report(self):
        for k in self.resources:
            print(k + " : " + str(self.resources[k]))
        print("Money : $" + str(self.money))
        return

    # Check resources sufficient?
    # a. When the user chooses a drink, the program should check if there are enough
    # resources to make that drink.
    # b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
    # not continue to make the drink but print: “Sorry there is not enough water.”
    # c. The same should happen if another resource is depleted, e.g. milk or coffee.
    def check_resources(self, req):
        for ing in self.menu[req]["ingredients"]:
            available = (self.get_resource(ing) - self.menu[req]["ingredients"][ing])
            if available < 0:
                print("Sorry there is not enough " + ing + ".")
                return False
        return True

    # 5. Process coins.
    # a. If there are sufficient resources to make the drink selected, then the program should
    # prompt the user to insert coins.
    # b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
    # c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
    # pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
    def request_money(self, req):
        change = 0
        quarters, dimes, nickels, pennies = \
            input(req + " costs $" + str(self.menu[req]["cost"]) + "Enter quarters, dimes, nickels or pennies: ").split()
        money_inserted = float(quarters) * 0.25 + float(dimes) * 0.1 + float(nickels) * 0.05 + float(pennies) * 0.01
        if money_inserted < self.menu[req]['cost']:
            print("Sorry that's not enough money. Money refunded!")
            return "fail"
        else:
            change = money_inserted - self.menu[req]['cost']
            self.update_revenue(self.menu[req]['cost'])
            if change > 0:
                print("Here's $" + str(change) + " dollars in change")
            return "success"

    def make_coffee(self, ref):
        self.update_resources(ref)
        print("Here's your " + ref + " enjoy!")
        return

    def update_resources(self, ref):
        for ing in self.menu[ref]["ingredients"]:
            self.resources[ing] -= self.menu[ref]["ingredients"][ing]
        return

    def get_resource(self, res):
        return self.resources[res]

    def update_revenue(self, revenue):
        self.money += revenue
        return

    def get_money(self):
        return self.money


def main():
    c1 = CoffeeMachine()
    while 1:
        coffee_req = c1.get_user_req()

        # end execution if user inputs off
        if coffee_req == "off":
            break

        # Get report
        elif coffee_req == "report":
            c1.get_report()

        # Check resources and then accept money
        else:
            if c1.check_resources(coffee_req):
                transaction_state = c1.request_money(coffee_req)
                if transaction_state == "success":
                    c1.make_coffee(coffee_req)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

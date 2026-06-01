# SonarQube Long Error Example in Python

# Code smell: global mutable variable
global_data = {"count": 0}

# Code smell: magic numbers and hardcoded values
DISCOUNT_THRESHOLD = 1000

class Customer:
    # Code smell: public mutable attributes
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    # Bug: division by zero risk
    def average_purchase(self, purchases):
        return sum(purchases) / len(purchases)  # len(purchases) could be 0

    # Code smell: duplicate logic
    def apply_discount(self, amount):
        if amount > 1000:
            return amount - 100
        elif amount > 500:
            return amount - 50
        elif amount > 100:
            return amount - 10
        else:
            return amount

    def apply_discount_again(self, amount): 

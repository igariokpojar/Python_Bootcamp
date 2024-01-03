class Pizza:

    def __init__(self, size: str = '', num_of_cheese_topping: float = 0, num_of_pepperoni_topping: float = 0):
        self.size = size
        self.num_of_cheese_topping = num_of_cheese_topping
        self.num_of_pepperoni_topping = num_of_pepperoni_topping

    def calc_cost(self):
        base_cost = {'S': 10, 'M': 12, 'L': 14}.get(self.size, 0)
        topping_cost = 2 * (self.num_of_cheese_topping + self.num_of_pepperoni_topping)
        total_cost = base_cost + topping_cost
        return total_cost

    def __str__(self):
        return (f"Pizza size: {self.size}\nCheese toppings: {self.num_of_cheese_topping}"
                f"\nPepperoni toppings: {self.num_of_pepperoni_topping}\nYour pizza cost: ${self.calc_cost()}"
                f"\nTank you for choosing Meda's pizza")


pizza = Pizza('L', 2, 2)
print(pizza)
print('-----------------------------------')
pizza2 = Pizza('M',25,9)
print(pizza2)


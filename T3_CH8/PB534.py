class InvalidToppingError(Exception):
    pass
class InvalidCheeseError(Exception):
    pass
# -------------------- Pizza Class --------------------
class Pizza:
    valid_sizes = ["small", "medium", "large"]
    valid_toppings = ["corn", "tomato", "onion", "capsicum", "mushroom", "olives", "broccoli"]
    valid_cheese = ["mozzarella", "feta", "cheddar"]
    def __init__(self, size, toppings, cheese):
        if size not in Pizza.valid_sizes:
            raise ValueError("Invalid size selected!")
        for t in toppings:
            if t not in Pizza.valid_toppings:
                raise InvalidToppingError(f"Topping '{t}' is not available!")
        for c in cheese:
            if c not in Pizza.valid_cheese:
                raise InvalidCheeseError(f"Cheese '{c}' is not available!")
        self.size = size
        self.toppings = toppings
        self.cheese = cheese
    def price(self):
        size_price = {"small": 50, "medium": 100, "large": 200} # Base price
        total = size_price[self.size]
        for t in self.toppings:   # Toppings price
            if t in ["broccoli", "mushroom", "olives"]:  # exotic toppings
                total += 50
            else:
                total += 20
        total += len(self.cheese) * 50  # Cheese price
        return total
# -------------------- Order Class --------------------
class Order:
    def __init__(self, name, customerid):
        self.name = name
        self.customerid = customerid
        self.pizzas = []
    def order(self):
        while True:
            print("\nCreating a pizza...")
            size = input("Enter size (small/medium/large): ")
            toppings = input("Enter toppings separated by space: ").split()
            cheese = input("Enter cheese separated by space: ").split()
            try:
                pizza = Pizza(size, toppings, cheese)
                self.pizzas.append(pizza)
                print("Pizza added successfully!")
            except Exception as e:
                print("Error:", e)

            more = input("Add another pizza? (yes/no): ")
            if more.lower() != "yes":
                break
    def bill(self):
        print("\n----- BILL DETAILS -----")
        print(f"Customer Name: {self.name}")
        print(f"Customer ID: {self.customerid}")
        print("------------------------")
        total_cost = 0
        for i, p in enumerate(self.pizzas, start=1):
            print(f"\nPizza {i}:")
            print("Size:", p.size)
            print("Toppings:", p.toppings)
            print("Cheese:", p.cheese)
            price = p.price()
            print("Price:", price)
            total_cost += price
        print("\nTOTAL COST:", total_cost)
        print("------------------------")
        print("Thank you for ordering at Olly’s Pizzas!")
order = Order("SOHANI", 2703)
order.order()
order.bill()
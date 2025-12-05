class Store:
    def __init__(self):
        self.items = {}   
    def input_items(self):
        n = int(input("enter no of items: "))
        for _ in range(n):
            code = input("enter code of item: ")
            price = int(input("enter cost of item: "))
            self.items[code] = price
    def show_items(self):
        print("\nItem Code   Price")
        for item, price in self.items.items():
            print(item, price)
    def generate_bill(self):
        quantities = {}
        print("Enter quantity of each item: ")
        for item in self.items:
            qty = int(input(f"Enter quantity of {item} : "))
            quantities[item] = qty
        print("************************Bill**********************")
        print("ITEM    PRICE   QUANTITY   SUBTOTAL")
        total = 0
        for item, price in self.items.items():
            qty = quantities[item]
            subtotal = price * qty
            print(item, price, qty, subtotal)
            total += subtotal
        print("**************************************")
        print("Total=", total)
store = Store()
store.input_items()     # user enters items + prices
store.show_items()      # show items
store.generate_bill()   
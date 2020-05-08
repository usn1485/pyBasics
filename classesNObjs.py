class Store:
    def __init__(self, name):
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
        self.name = name
        self.items = []

    def add_item(self, name, price):
        # Create a dictionary with keys name and price, and append that to self.items.
        item = {'name': name, 'price': price}
        self.items.append(item)

    @property
    def stock_price(self):
        # total=0
        # Add together all item prices in self.items and return the total.
        # for item in self.items:
        #     total += item['price']
        # return total
        # List Comprehension
        return sum(item['price'] for item in self.items)


store = Store("Walmart")
store.add_item('milk', 3)
store.add_item('bread', 5)
store.add_item('cheese', 10)
print(store.stock_price)

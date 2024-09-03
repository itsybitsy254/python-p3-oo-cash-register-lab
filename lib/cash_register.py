class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        # Add the items to the list based on quantity
        self.items.extend([title] * quantity)
        # Calculate and add the price for the current items
        self.last_transaction = price * quantity
        self.total += self.last_transaction

    def apply_discount(self):
        # Apply discount if there is one; otherwise, print a message
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = self.total * (self.discount / 100)
            self.total = round(self.total - discount_amount)
            print(f"After the discount, the total comes to ${self.total}.")

    def void_last_transaction(self):
        # Void the last transaction by subtracting its value from the total
        self.total -= self.last_transaction
        # Reset last_transaction in case of further operations
        self.last_transaction = 0

class Product:
    def __init__(self, product_id, name, price, active=True):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.active = active

    def update_price(self, new_price):
        self.price = new_price

    def suspend_product(self):
        self.active = False

    def to_dict(self):
        return {"product_id": self.product_id, "name": self.name, "price": self.price, "active": self.active}

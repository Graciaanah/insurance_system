import datetime

class Payment:
    def __init__(self, payment_id, holder_id, product_id, amount, due_date):
        self.payment_id = payment_id
        self.holder_id = holder_id
        self.product_id = product_id
        self.amount = amount
        self.due_date = due_date
        self.paid = False

    def process_payment(self):
        self.paid = True

    def apply_penalty(self):
        today = datetime.date.today()
        if not self.paid and today > self.due_date:
            self.amount += 50

    def to_dict(self):
        return {
            "payment_id": self.payment_id,
            "holder_id": self.holder_id,
            "product_id": self.product_id,
            "amount": self.amount,
            "due_date": str(self.due_date),
            "paid": self.paid
        }

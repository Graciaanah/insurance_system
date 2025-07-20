from policyholder import Policyholder
from product import Product
from payment import Payment
import json
import datetime
import os

def save_to_file(filename, data):
    try:
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving file: {e}")

def main():
    p1 = Policyholder("PH001", "Alice")
    p2 = Policyholder("PH002", "Bob")

    prod1 = Product("PRD001", "Health Insurance", 1200)

    payment1 = Payment("PMT001", p1.holder_id, prod1.product_id, prod1.price, datetime.date.today())
    payment1.process_payment()

    payment2 = Payment("PMT002", p2.holder_id, prod1.product_id, prod1.price, datetime.date.today())
    payment2.process_payment()

    os.makedirs("data", exist_ok=True)
    save_to_file("data/policyholders.json", [p1.to_dict(), p2.to_dict()])
    save_to_file("data/products.json", [prod1.to_dict()])
    save_to_file("data/payments.json", [payment1.to_dict(), payment2.to_dict()])

    for p in [p1, p2]:
        print(f"{p.name} | Active: {p.active} | ID: {p.holder_id}")

if __name__ == "__main__":
    main()

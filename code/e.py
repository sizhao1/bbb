import csv
from datetime import datetime

class Transaction:
    def __init__(self, date, type, amount, category, note):
        self.date = date
        self.type = type
        self.amount = amount
        self.category = category
        self.note = note

class Account:
    def __init__(self, name):
        self.name = name
        self.transactions = []

    def add_transaction(self, date, type, amount, category, note):
        transaction = Transaction(date, type, amount, category, note)
        self.transactions.append(transaction)

    def get_balance(self):
        balance = 0
        for transaction in self.transactions:
            if transaction.type == "income":
                balance += transaction.amount
            else:
                balance -= transaction.amount
        return balance

    def get_transactions_by_month(self, month):
        transactions = []
        for transaction in self.transactions:
            if transaction.date.month == month:
                transactions.append(transaction)
        return transactions

    def export_transactions_to_csv(self):
        filename = self.name + "_transactions.csv"
        with open(filename, mode="w", newline="") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["Date", "Type", "Amount", "Category", "Note"])
            for transaction in self.transactions:
                writer.writerow([transaction.date.strftime("%Y-%m-%d"),
                                 transaction.type,
                                 transaction.amount,
                                 transaction.category,
                                 transaction.note])
        return filename

def main():
    account = Account("My Account")
    account.add_transaction(datetime(2023, 5, 1), "income", 5000, "salary", "Monthly salary")
    account.add_transaction(datetime(2023, 5, 3), "expense", 1500, "food", "Lunch with colleagues")
    account.add_transaction(datetime(2023, 5, 5), "expense", 200, "transportation", "Taxi to airport")
    print(f"Current balance: {account.get_balance()}")
    print("Transactions in May:")
    transactions = account.get_transactions_by_month(5)
    for transaction in transactions:
        print(f"{transaction.date.strftime('%Y-%m-%d')} {transaction.type} {transaction.amount} {transaction.category} {transaction.note}")
    filename = account.export_transactions_to_csv()
    print(f"Transactions exported to {filename}")

if __name__ == "__main__":
    main()
from models.transaction import Transaction
from typing import List

class Book:
    def __init__(self) -> None:
        self.transactions: List[Transaction] = []
        return

    def insert_transaction(self, transaction: Transaction) -> None:
        year: int = transaction.get_year()
        month: int = transaction.get_month()
        day: int = transaction.get_day()

        index_to_insert: int = -1

        for idx, current_transaction in enumerate(self.transactions):
            current_year: int = current_transaction.get_year()
            if year > current_year: continue

            current_month: int = current_transaction.get_month()
            if month > current_month: continue

            current_day: int = current_transaction.get_day()
            if day > current_day: continue

            index_to_insert = idx
            break

        if index_to_insert == -1:
            self.transactions.insert(index_to_insert, transaction)
        else:
            self.transactions.append(transaction)

        return
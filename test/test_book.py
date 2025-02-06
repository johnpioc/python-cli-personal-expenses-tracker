import unittest
from models.transaction import Transaction
from models.book import Book
from models.types import SupabaseTransactionDict
from typing import List

import os
from dotenv import load_dotenv
from supabase import create_client, Client



class TestBook(unittest.TestCase):
    def setUp(self):
        self.book: Book = Book()

        load_dotenv('../config.env')
        supabase_url: str = os.environ.get("SUPABASE_URL")
        supabase_key: str = os.environ.get("SUPABASE_KEY")

        self.supabase: Client = create_client(supabase_url, supabase_key)

    def test_insert(self):
        response = self.supabase.table("transactions").select("*").limit(10).execute()
        supabase_transactions: List[SupabaseTransactionDict] = response.data

        for supabase_transaction in supabase_transactions:
            new_transaction: Transaction = Transaction(
                supabase_transaction['id'],
                supabase_transaction['date'],
                supabase_transaction['amount'],
                supabase_transaction['description'],
                supabase_transaction['category'],
                supabase_transaction['payment_method'],
            )

            self.book.insert_transaction(new_transaction)

        transactions: List[Transaction] = self.book.transactions

        for i in range(1, len(transactions) - 1):
            previous_transaction: Transaction = transactions[i - 1]
            current_transaction: Transaction = transactions[i]

            assert previous_transaction.get_year() <= current_transaction.get_year()






if __name__ == '__main__':
    unittest.main()

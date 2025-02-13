import os
import time

from supabase import create_client, Client
from dotenv import load_dotenv
from typing import List

from models.types import SupabaseTransactionDict
from models.transaction import Transaction
from models.book import Book

load_dotenv("config.env")

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

def get_all_transactions() -> List[Transaction]:
    try:
        response = supabase.table("transactions").select("*").execute()
        supabase_transactions: List[SupabaseTransactionDict] = response.data

        transactions: List[Transaction] = []

        for supabase_transaction in supabase_transactions:
            new_transaction = Transaction(
                supabase_transaction["id"],
                supabase_transaction["date"],
                supabase_transaction["amount"],
                supabase_transaction["description"],
                supabase_transaction["category"],
                supabase_transaction["payment_method"]
            )

            transactions.append(new_transaction)

        return transactions
    except Exception as e:
        print(f"Error occured retrieving transactions: {e}")
        return []

def edit_transaction(updated_transaction: Transaction) -> bool:
    try:
        response = supabase.table("transactions").update({
            "date": updated_transaction.date,
            "amount": updated_transaction.amount,
            "description": updated_transaction.description,
            "category": updated_transaction.category,
            "payment_method": updated_transaction.payment_method
        }).eq("id", updated_transaction.id).execute()

        return True
    except Exception as e:
        print(f"Error occured editing a transaction: {e}")
        time.sleep(2)
        return False

def delete_transaction(transaction_to_delete: Transaction) -> bool:
     try:
         response = supabase.table("transactions").delete().eq("id", transaction_to_delete.id).execute()
         return True
     except Exception as e:
         print(f"Error occured editing a transaction: {e}")
         time.sleep(2)
         return False
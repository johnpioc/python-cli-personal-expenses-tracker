import os
from supabase import create_client, Client
from dotenv import load_dotenv
from typing import List

from models.types import SupabaseTransactionDict
from models.transaction import Transaction

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
        print(f"Error occured: {e}")
        return []

def edit_transaction(transactionId: str) -> bool:
    pass
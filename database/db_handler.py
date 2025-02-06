import os
from supabase import create_client, Client
from dotenv import load_dotenv

from models.transaction import Transaction
from typing import List, TypedDict

load_dotenv("config.env")

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

class SupabaseTransactionDict(TypedDict):
    id: str
    date: str
    amount: float
    description: str
    category: str
    payment_method: str

def get_all_transactions() -> List[Transaction]:
    response = supabase.table("transactions").select("*").limit(100).execute()
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
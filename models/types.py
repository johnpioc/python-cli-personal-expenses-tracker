from typing import List, TypedDict

class SupabaseTransactionDict(TypedDict):
    id: str
    date: str
    amount: float
    description: str
    category: str
    payment_method: str
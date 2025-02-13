import time
import re
import uuid

from models.transaction import Transaction
from models.book import Book
from database.db_handler import add_transaction

def get_and_validate_date() -> str:
    date: str = input("Date (dd/mm/yy): ")
    if not re.match(r"^\d{2}/\d{2}/\d{4}$", date):
        print("\nInvalid date, try again...\n")
        time.sleep(2)
        return get_and_validate_date()
    else:
        return date

def get_and_validate_amount() -> int:
    amount_string: str = input("Amount ($): ")
    try:
        amount: int = int(amount_string)
        return amount
    except ValueError:
        print("\nNot a Valid Amount, try again...\n")
        time.sleep(2)
        return get_and_validate_amount()

def get_and_validate_confirmation() -> bool:
    confirmation: str = input(f"Confirm add? (y/n): ")
    if confirmation == "y":
        return True
    elif confirmation == "n":
        return False
    else:
        print("\nInvalid input, try again...\n")
        time.sleep(2)
        return get_and_validate_confirmation()

def show_add_transaction_page(book: Book) -> None:
    print("-- Add New Transaction --")
    date: str = get_and_validate_date()
    amount: int = get_and_validate_amount()
    description: str = input("Description: ")
    category: str = input("Category: ")
    payment_method: str = input("Payment Method: ")
    confirmation: bool = get_and_validate_confirmation()

    if confirmation:
        new_transaction: Transaction = Transaction(str(uuid.uuid4()), date, amount, description, category, payment_method)
        status: bool = add_transaction(new_transaction)
        if status:
            book.insert_transaction(new_transaction)
            print("\nTransaction added successfully!\n")
            time.sleep(2)
            return


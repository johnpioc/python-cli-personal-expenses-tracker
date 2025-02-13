import time
from typing import List
from colorama import init, Fore, Style

from database.db_handler import get_all_transactions, add_transaction
from models.book import Book
from models.transaction import Transaction
from pages.view_transaction_page import show_view_transaction_page
from pages.add_transaction_page import show_add_transaction_page

def initialise_book() -> Book:
    book: Book = Book()
    transactions: List[Transaction] = get_all_transactions()

    for transaction in transactions:
        book.insert_transaction(transaction)

    return book

def main() -> None:
    book: Book = initialise_book()

    while True:
        print("== Personal Finance Tracker ==")
        print(Fore.BLUE + "1." + Style.RESET_ALL + "Add Transaction")
        print(Fore.BLUE + "2." + Style.RESET_ALL+ "View Transactions")
        print(Fore.BLUE + "3." + Style.RESET_ALL + "Financial Reports")
        print(Fore.BLUE + "4." + Style.RESET_ALL + "Search Transactions")
        print(Fore.BLUE + "5." + Style.RESET_ALL + "Account Settings")
        print(Fore.BLUE + "6." + Style.RESET_ALL + "Exit")
        user_input: str = input("Choose an option (1-6): ")

        match user_input:
            case "1":
                show_add_transaction_page(book)
            case "2":
                show_view_transaction_page(book)
            case _:
                print("\ninvalid input, try again...\n")
                time.sleep(2)

init(autoreset=True)
main()
from models.book import Book
from models.transaction import Transaction
from database.db_handler import get_all_transactions
from typing import List

def initialise_book() -> Book:
    book: Book = Book()
    transactions: List[Transaction] = get_all_transactions()

    for transaction in transactions:
        book.insert_transaction(transaction)

    return book

def view_transactions(book: Book) -> None:
    transactions = book.transactions

    for transaction in transactions:
        print(transaction.date)

def main() -> None:
    print("Welcome to your Personal Finances Tracker!\n")

    book = initialise_book()

    while True:
        print("Type in one of the commands below.\n")

        print("view - see all your transactions")
        print("add - input a new transaction (income or spend)")
        print("edit - go into edit mode")
        print("delete - go into delete mode")
        print("summary - get total income, expenses and net balance")
        print("breakdown - get expense distribution by category")
        print("import - bulk upload transactions via csv file")
        print("export - download a csv file copy of your transactions")
        print("quit - exit the application\n")

        user_input: str = input("Enter a command: ")
        print("")

        match user_input:
            case "view":
                view_transactions(book)
            case "quit":
                break

main()
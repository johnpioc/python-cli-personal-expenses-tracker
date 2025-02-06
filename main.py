from models.book import Book
from models.transaction import Transaction
from database.db_handler import get_all_transactions
from typing import List
from tabulate import tabulate
import math

def initialise_book() -> Book:
    book: Book = Book()
    transactions: List[Transaction] = get_all_transactions()

    for transaction in transactions:
        book.insert_transaction(transaction)

    return book

def view_transactions(book: Book) -> None:
    transactions = book.transactions
    page: int = 0
    table_headers: List[str] = ["Row no.", "Date", "Amount", "Description", "Category", "Payment Method"]
    last_page: int = math.ceil(len(transactions) / 100) - 1

    while True:
        table_data: List[int, str, float, str, str, str] = []

        for i in range(100 * page, 100 * page + 100):
            if (len(transactions) - 1 < i): break

            current_transaction: Transaction =  transactions[i]
            table_data.append([
                i + 1,
                current_transaction.date,
                current_transaction.amount,
                current_transaction.description[:20] + "...",
                current_transaction.category,
                current_transaction.payment_method
            ])

        print(tabulate(table_data, headers=table_headers, tablefmt="fancy_grid"))

        print("\nSelect one of the view commands below:\n")
        print("left - view the previous 100 transactions")
        print("right - view the next 100 transactions")
        print("quit - go back to main menu\n")

        user_input = input("Enter your command: ")

        match user_input:
            case "left":
                if page != 0: page -= 1
            case "right":
                if last_page > page: page += 1
            case "quit":
                break

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
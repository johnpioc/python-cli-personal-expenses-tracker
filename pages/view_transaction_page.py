import math
from tabulate import tabulate
from typing import List, Tuple
from colorama import Fore, Style
import time
import re

from models.book import Book
from models.transaction import Transaction
from database.db_handler import edit_transaction, delete_transaction


def generate_transactions_table(book: Book, page_num: int) -> str:
    table_data: List[str, str, float, str, str, str] = []
    headers: List[str] = [f"{Fore.BLUE}No.{Style.RESET_ALL}", "Date", "Amount", "Category", "Description", "Payment Method"]
    transactions: List[Transaction] = book.transactions
    total_transaction_count: int = len(book.transactions)

    for i in range(100 * page_num, 100 * page_num + 100):
        if (i > total_transaction_count - 1): break

        current_transaction: Transaction = transactions[i]
        table_data.append([
            Fore.BLUE + str(i + 1) + Style.RESET_ALL,
            current_transaction.date,
            f"{Fore.GREEN}{current_transaction.amount}{Style.RESET_ALL}" if current_transaction.category == "Income" else f"{Fore.RED}({current_transaction.amount}){Style.RESET_ALL}",
            current_transaction.category,
            current_transaction.description,
            current_transaction.payment_method
        ])

    return tabulate(table_data, headers=headers, tablefmt="plain")

def get_and_validate_date(transaction_to_update: Transaction) -> str:
    date: str = input(f"Date (dd/mm/yy) (currently: {transaction_to_update.date}): ")
    if not re.match(r"^\d{2}/\d{2}/\d{4}$", date):
        print("\nInvalid date, try again...\n")
        time.sleep(2)
        get_and_validate_date(transaction_to_update)
    else:
        return date

def get_and_validate_amount(transaction_to_update: Transaction) -> int:
    amount_string: str = input(f"Amount ($) (currently: {transaction_to_update.amount}): ")
    try:
        amount: int = int(amount_string)
        return amount
    except ValueError:
        print("\nNot a Valid AMmount, try again...\n")
        time.sleep(2)
        return get_and_validate_amount(transaction_to_update)

def get_and_validate_confirmation(prompt: str) -> bool:
    confirmation: str = input(f"Confirm {prompt}? (y/n): ")
    if confirmation == "y":
        return True
    elif confirmation == "n":
        return False
    else:
        print("\nInvalid input, try again...\n")
        time.sleep(2)
        return get_and_validate_confirmation(prompt)

def edit_transaction_workflow(row_number: int, book: Book) -> None:
    transactions: List[Transaction] = book.transactions
    total_transaction_count: int = len(transactions)

    if row_number <= 0 | row_number > total_transaction_count:
        print("\nInvalid row number, try again...\n")
        time.sleep(2)
        return

    transaction_to_update: Transaction = transactions[row_number - 1]

    print(f"-- Edit Transaction no. {row_number} --")
    date: str = get_and_validate_date(transaction_to_update)
    amount: int = get_and_validate_amount(transaction_to_update)
    description: str = input(f"Description (currently: {transaction_to_update.description}): ")
    category: str = input(f"Category (currently: {transaction_to_update.category}): ")
    payment_method: str = input(f"Payment Method (currently: {transaction_to_update.payment_method}): ")
    confirmation: bool = get_and_validate_confirmation("edit")

    if confirmation:
        transaction_to_update.date = date
        transaction_to_update.amount = amount
        transaction_to_update.description = description
        transaction_to_update.category = category
        transaction_to_update.payment_method = payment_method
        status: bool = edit_transaction(transaction_to_update)
        if status:
            print(f"\nTransaction #{row_number} edited successfully!\n")
            time.sleep(2)

def delete_transaction_workflow(row_number: int, book: Book) -> None:
    transactions: List[Transaction] = book.transactions
    total_transaction_count: int = len(transactions)

    if row_number <= 0 | row_number > total_transaction_count:
        print("\nInvalid row number, try again...\n")
        time.sleep(2)
        return

    transaction_to_delete: Transaction = transactions[row_number - 1]
    print(f"-- Confirm deletion of transaction #{row_number} --")
    print(f"Date: {transaction_to_delete.date}")
    print(f"Amount: ${transaction_to_delete.amount}")
    print(f"Description: {transaction_to_delete.description}")
    print(f"Category: {transaction_to_delete.category}")
    print(f"Payment Method: {transaction_to_delete.payment_method}")
    confirmation: bool = get_and_validate_confirmation("delete")

    if confirmation:
        status: bool = delete_transaction(transaction_to_delete)
        if status:
            transactions.pop(row_number - 1)
            print(f"\nTransaction #{row_number} deleted successfully\n")
            time.sleep(2)


def show_view_transaction_page(book: Book) -> None:
    last_page_num: int = math.ceil(len(book.transactions) / 10) - 1
    page_num: int = 0


    while True:
        table_string: str = generate_transactions_table(book, page_num)
        print("--- Your Transactions ---")
        print(table_string)
        print("Commands:")
        print(f"{Fore.BLUE}[n] {Style.RESET_ALL}Next Page | {Fore.BLUE}[p] {Style.RESET_ALL}Previous Page | {Fore.BLUE}[d <No.>] {Style.RESET_ALL}Delete | {Fore.BLUE}[e <No.>] {Style.RESET_ALL}Edit | {Fore.BLUE}[b] {Style.RESET_ALL}Back \n")
        user_input: str = input("Enter Command: ")

        match user_input:
            case "n":
                if page_num != last_page_num: page_num += 1
            case "p":
                if page_num != 0:
                    page_num -= 1
            case _ if re.match(r"^e \d+$", user_input):
                row_number: int = int(user_input.split()[1])
                edit_transaction_workflow(row_number, book)
            case _ if re.match(r"^d \d+$", user_input):
                row_number: int = int(user_input.split()[1])
                delete_transaction_workflow(row_number, book)
            case "b":
                break
            case _:
                print("\nInvalid input, try again...\n")
                time.sleep(2)

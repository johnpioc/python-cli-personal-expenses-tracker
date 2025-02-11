import math
from tabulate import tabulate
from typing import List
from colorama import Fore, Style
import time
import re

from models.book import Book
from models.transaction import Transaction

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

def show_view_transaction_page(book: Book):
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
            case _:
                print("\nInvalid input, try again...\n")
                time.sleep(2)
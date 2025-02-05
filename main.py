def view_transactions() -> None:
    pass

def main() -> None:
    print("Welcome to your Personal Finances Tracker!\n")

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
                view_transactions()
            case "quit":
                break

main()
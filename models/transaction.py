class Transaction:
    def __init__(self, id: str, date: str, amount: float, description: str,category: str, payment_method: str) -> None:
        self.id: str = id
        self.date: str = date
        self.amount: float = amount
        self.description: str = description
        self.category: str = category
        self.payment_method: str = payment_method
        return

    def get_day(self) -> int:
        return int(self.date[:2])

    def get_month(self) -> int:
        return int(self.date[3:5])

    def get_year(self) -> int:
        return int(self.date[6:])
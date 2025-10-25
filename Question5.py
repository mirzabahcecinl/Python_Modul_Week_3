class Customer:
    def __init__(self, name, surname, tc_identification, phone):
        self.name = name
        self.surname = surname
        self.tc_identification = tc_identification
        self.phone = phone

    # def display_information(self):
    #     print(f"Name: {self.name}")
    #     print(f"Surname: {self.surname}")
    #     print(f"TC: {self.tc_identification}")
    #     print(f"Phone: {self.phone}")

    def __str__(self):
        return (
            f"Customer Information\n"
            f"---------------------------\n"
            f"Name & Surname : {self.name} {self.surname}\n"
            f"TC ID Number   : {self.tc_identification}\n"
            f"Phone Number   : {self.phone}"
        )



class Account(Customer):
    def __init__(self, name, surname, tc_identification, phone, account_number, balance):
        super().__init__(name, surname, tc_identification, phone)
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} TL deposited successfully.")

    def money_check(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"Insufficient balance! Your current balance is {self.balance} TL.")
        else:
            self.balance -= amount
            print(f"{amount} TL withdrawn successfully.")

    def display_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance:,.2f} TL")


customer_account = Account("Beyza Nur", "Sarıkaya", "12345678910", "0555-123-4567", "TR123456789", 5000)

print(customer_account.__str__())


customer_account.deposit(2000)

customer_account.money_check(1000)

customer_account.money_check(7000)
customer_account.display_balance()


print(customer_account.__str__())


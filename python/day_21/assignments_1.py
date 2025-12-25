'''
Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description. The same goes for expenses.
'''

class PersonAccount:
     def __init__(self, firstname, lastname):
         self.firstname = firstname
         self.lastname = lastname
         self.incomes = {}
         self.expenses = {}
         
     def add_income(self, description, amount):
         if amount <= 0:
            raise ValueError("Income amount should be positive")
         self.incomes[description] = self.incomes.get(description, 0) + amount
         
     def add_expense(self, description, amount):
        if amount <= 0:
            raise ValueError("Expense amount must be positive")
        self.expenses[description] = self.expenses.get(description, 0) + amount
    
     def total_income(self):
        return sum(self.incomes.values())

     def total_expense(self):
        return sum(self.expenses.values())
        
     def account_balance(self):
        return self.total_income() - self.total_expense()
        
     def __str__(self):
        return (
            f"Account Holder: {self.firstname} {self.lastname}\n"
            f"Total Income: {self.total_income()}\n"
            f"Total Expense: {self.total_expense()}\n"
            f"Account Balance: {self.account_balance()}"
        )
        
     def account_info(self):
        return {
            "Name": f"{self.firstname} {self.lastname}",
            "Total Income": self.total_income(),
            "Total Expense": self.total_expense(),
            "Balance": self.account_balance(),
            "Incomes": self.incomes,
            "Expenses": self.expenses
        }
        
person = PersonAccount("Keerthi", "Kumar")

# Add incomes
person.add_income("Salary", 100000)
person.add_income("Freelancing", 25000)

# Add expenses
person.add_expense("Rent", 30000)
person.add_expense("Food", 15000)
person.add_expense("Travel", 5000)

print(person.account_info())
print("\n", person)

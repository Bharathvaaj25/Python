import mysql.connector
from functools import reduce
from abc import ABC, abstractmethod

# ---------------- DATABASE CONNECTION ----------------
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bharathvaaj@25901",
    port=3306,
    database="expense_db"
)

cursor = conn.cursor()


# ---------------- ABSTRACT CLASS ----------------
class BaseSystem(ABC):
    @abstractmethod
    def get_details(self):
        pass


# ---------------- USER CLASS ----------------
class User(BaseSystem):
    def __init__(self):
        self.__name = None   # encapsulation

    def set_user(self, name):
        self.__name = name

    def get_user(self):
        return self.__name

    def add_user(self):
        query = "INSERT INTO users (name) VALUES (%s)"
        cursor.execute(query, (self.__name,))
        conn.commit()
        print("User added successfully!")

    def get_details(self):
        print(f"User: {self.__name}")


# ---------------- EXPENSE CLASS ----------------
class Expense(User):   # inheritance

    def __init__(self):
        super().__init__()
        self.__amount = 0
        self.__category = ""
        self.__description = ""
        self.__date = ""

    def add_expense(self, user_id, amount, category, description, date):
        self.__amount = amount
        self.__category = category
        self.__description = description
        self.__date = date

        query = """INSERT INTO expenses 
                   (user_id, amount, category, description, date)
                   VALUES (%s, %s, %s, %s, %s)"""

        cursor.execute(query, (user_id, amount, category, description, date))
        conn.commit()
        print("Expense added successfully!")

    # method overriding
    def get_details(self):
        print("Expense Details:")
        print(self.__amount, self.__category, self.__description, self.__date)

    # ---------------- VIEW EXPENSES ----------------
    def view_expenses(self, user_id):
        query = """SELECT users.name, expenses.amount, expenses.category, 
                          expenses.description, expenses.date
                   FROM expenses
                   JOIN users ON users.user_id = expenses.user_id
                   WHERE users.user_id = %s"""

        cursor.execute(query, (user_id,))
        data = cursor.fetchall()

        for row in data:
            print(row)

        return data

    # ---------------- FILTER EXPENSES ----------------
    def filter_by_category(self, data, category):
        result = list(filter(lambda x: x[2] == category, data))
        return result

    def filter_by_date(self, data, date):
        result = [x for x in data if str(x[4]) == date]
        return result

    # ---------------- TOTAL EXPENSE ----------------
    def total_expense(self, data):
        amounts = list(map(lambda x: x[1], data))
        total = reduce(lambda a, b: a + b, amounts, 0)
        return total

    # ---------------- CATEGORY WISE ----------------
    def category_wise(self, data):
        categories = {x[2] for x in data}

        result = {
            cat: sum([x[1] for x in data if x[2] == cat])
            for cat in categories
        }
        return result

    # ---------------- UPDATE EXPENSE ----------------
    def update_expense(self, exp_id, amount):
        query = "UPDATE expenses SET amount = %s WHERE exp_id = %s"
        cursor.execute(query, (amount, exp_id))
        conn.commit()
        print("Expense updated!")

    # ---------------- DELETE EXPENSE ----------------
    def delete_expense(self, exp_id):
        query = "DELETE FROM expenses WHERE exp_id = %s"
        cursor.execute(query, (exp_id,))
        conn.commit()
        print("Expense deleted!")

    # ---------------- MONTHLY REPORT ----------------
    def monthly_report(self, data):
        report = {}

        for row in data:
            month = str(row[4])[:7]   # YYYY-MM
            report[month] = report.get(month, 0) + row[1]

        return report

    # ---------------- HIGHEST EXPENSE ----------------
    def highest_expense(self, data):
        highest = reduce(lambda a, b: a if a[1] > b[1] else b, data)
        return highest

    # ---------------- SMART INSIGHT ----------------
    def smart_insight(self, data):
        cat_data = self.category_wise(data)
        max_cat = max(cat_data, key=cat_data.get)

        return f"You are spending too much on {max_cat} this month!"


# ---------------- MAIN PROGRAM ----------------
exp = Expense()

# ---- Add User ----
exp.set_user("Bharath")
exp.add_user

# ---- Add Expenses ----
exp.add_expense(1, 2000, "Food", "Hotel", "2026-04-01")
exp.add_expense(1, 1500, "Travel", "Bus", "2026-04-02")
exp.add_expense(1, 3000, "Shopping", "Clothes", "2026-04-03")
exp.add_expense(1, 2500, "Food", "Restaurant", "2026-04-05")

# ---- View ----
data = exp.view_expenses(1)

# ---- Filter ----
print("\nFood Expenses:", exp.filter_by_category(data, "Food"))
print("\nDate Filter:", exp.filter_by_date(data, "2026-04-01"))

# ---- Total ----
print("\nTotal Expense:", exp.total_expense(data))

# ---- Category Wise ----
print("\nCategory Wise:", exp.category_wise(data))

# ---- Monthly Report ----
print("\nMonthly Report:", exp.monthly_report(data))

# ---- Highest Expense ----
print("\nHighest Expense:", exp.highest_expense(data))

# ---- Smart Insight ----
print("\nInsight:", exp.smart_insight(data))
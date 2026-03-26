

account = {
    "name": "Bharath",
    "balance": 1000
}


def deposit(amount):
    account["balance"] += amount
    print(f"Deposited: {amount}")


def withdraw(amount):
    if amount <= account["balance"]:
        account["balance"] -= amount
        print(f"Withdrawn: {amount}")
    else:
        print("Insufficient Balance!")
 

def check_balance():
    print(f"Account Holder: {account['name']}")
    print(f"Current Balance: {account['balance']}")


print("Initial Account Details:")
check_balance()

print("\nDepositing 500...")
deposit(500)

print("\nWithdrawing 300...")
withdraw(300)

print("\nFinal Account Details:")
check_balance()
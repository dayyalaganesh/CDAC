"""
Assignment 5: Stateful Ledger Scope Machine (LEGB Scopes & Closures)
Scenario
You are developing a stateful balance ledger tracker that tracks account state history. To satisfy strict architecture requirements, you must manage this state without defining any classes (class keyword is prohibited). Instead, you must use closures, nested functions, and Python scoping variables.

Problem Description
Define a global variable AUDIT_TRANSACTION_COUNT = 0 at the top level of your script.
Implement a function create_bank_account(owner_name, initial_balance) that returns a dictionary of actions.
Inside create_bank_account, initialize local variables balance (float, set to initial_balance) and history (list of strings, initially containing ["Account created with 1000.0"] or similar initial message).
Define three nested functions inside create_bank_account:
deposit(amount):
Adds amount to the local balance variable.
Appends the string "deposit <amount>" to the local history list.
Increments the global AUDIT_TRANSACTION_COUNT by 1 using the global keyword.
withdraw(amount):
Checks if the current local balance is sufficient (balance 
≥
 amount).
If yes, deducts amount from balance, appends the string "withdraw <amount>" to history, and increments global AUDIT_TRANSACTION_COUNT by 1.
If the balance is insufficient, raises a standard ValueError with message "Insufficient balance".
get_statement():
Returns a tuple containing (owner_name, current_balance, history_list_copy). (Note: Make sure history_list_copy is a copy of the history list to prevent direct external modification).
Return a dictionary containing key-value mappings to these inner functions:
return {
    "deposit": deposit,
    "withdraw": withdraw,
    "statement": get_statement
}
Constraint: You must utilize the nonlocal keyword to modify the variables balance and history inside the nested functions.
Example Walkthrough
# Initial State
print(AUDIT_TRANSACTION_COUNT) # Output: 0

# Create account
acc = create_bank_account("Arham", 1000.0)

# Deposit
acc["deposit"](200.0)

# Withdraw
acc["withdraw"](150.0)

# Overdraft attempt (should raise ValueError)
try:
    acc["withdraw"](2000.0)
except ValueError as e:
    print(e) # Output: Insufficient balance

# Get statement
owner, bal, txn_history = acc["statement"]()
print(owner)       # Output: Arham
print(bal)         # Output: 1050.0
print(txn_history) # Output: ['Account created with 1000.0', 'deposit 200.0', 'withdraw 150.0']

# Verify global log count
print(AUDIT_TRANSACTION_COUNT) # Output: 2
"""
AUDIT_TRANSACTION_COUNT = 0
actions={}

def create_bank_account(owner_name, initial_balance):
    balance=float(initial_balance)
    history=[f"Account created with {balance}"]

    def deposit(amount):
        nonlocal balance, history
        balance += amount
        history.append(f"deposit {amount}")

        global AUDIT_TRANSACTION_COUNT
        AUDIT_TRANSACTION_COUNT += 1

    def withdraw(amount):
        nonlocal balance, history
        if balance < amount:
            raise ValueError("Insufficient balance")
        balance -= amount
        history.append(f"deposit {amount}")
        global AUDIT_TRANSACTION_COUNT
        AUDIT_TRANSACTION_COUNT += 1
        
    def get_statement():
            return (owner_name, balance, list(history))

    return {
        "deposit":deposit,
        "withdraw":withdraw,
        "statement":get_statement
         
    }

print(AUDIT_TRANSACTION_COUNT) 
acc = create_bank_account("Arham", 1000.0)
acc["deposit"](200.0)
acc["withdraw"](150.0)
try:
    acc["withdraw"](2000.0)
except ValueError as e:
    print(e) 

owner, bal, txn_history = acc["statement"]()
print(owner)        
print(bal)          
print(txn_history) 

print(AUDIT_TRANSACTION_COUNT) 
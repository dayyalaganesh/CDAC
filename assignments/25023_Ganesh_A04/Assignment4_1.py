"""
Assignment 1: Inventory Tracker for CDAC Bookstore
Scenario
The CDAC Bookstore needs a backend helper module to manage books and their quantities. 
The inventory is stored in a Python dictionary where keys are book titles (strings) and values are quantities in stock (non-negative integers).

Problem Description
Write a function manage_bookstore_inventory(inventory, action, book_title, quantity=0) that handles inventory operations safely.

The action parameter can be one of three options: "add", "sell", or "lookup".
Add Action ("add"):
Add the specified quantity to the existing stock of book_title.
If the book is not in the inventory dictionary, add it as a new key with quantity as the value.
Sell Action ("sell"):
Decrease the stock of book_title by the specified quantity.
If the book is not found in the inventory, print a message: Error: Book '<book_title>' not found in inventory. and make no changes.
(Do not let the program crash with a KeyError).
If the requested quantity to sell exceeds the stock available, print: Error: Insufficient stock for '<book_title>'. 
Available: <current_stock>. and make no changes.
If the stock reaches exactly 0 after a successful sale, remove the book key from the inventory entirely.
Lookup Action ("lookup"):
Look up the stock quantity of book_title and return it.
Use safe dictionary retrieval; if the book does not exist, return 0 without throwing a KeyError.
The function must return the updated/current inventory dictionary.

Example Walkthrough
# Initial Inventory
inventory = {"Python Basics": 10, "Learning AI": 5}

# 1. Add Stock
inventory = manage_bookstore_inventory(inventory, "add", "Python Basics", 5)
# Result: {"Python Basics": 15, "Learning AI": 5}

# 2. Sell Stock Safely (Missing Book)
inventory = manage_bookstore_inventory(inventory, "sell", "Data Science 101", 1)
# Console output: Error: Book 'Data Science 101' not found in inventory.

# 3. Sell Stock (Insufficient)
inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 10)
# Console output: Error: Insufficient stock for 'Learning AI'. Available: 5.

# 4. Sell Stock (Exactly Zero Stock)
inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 5)
# Result: {"Python Basics": 15}
"""

inventory = {"Python Basics": 10, "Learning Ai": 5}

def manage_bookstore_inventory(inventory, action, book_title, quantity=0):
    if action == "add":
        if book_title not in inventory:
            inventory[book_title] = inventory.get(book_title,0)+ quantity
            print(inventory)
        else:
           inventory[book_title] += quantity
           print(inventory)

    elif action == "sell":
        if book_title not in inventory:
            print(f"Error: Book '{book_title}' not found in inventory.")
        else:
            if inventory[book_title] < quantity:
                print(f"Error: Insufficient stock for '{book_title}'. Available: {inventory[book_title]}.")
            else:
                inventory[book_title] -= quantity
                if inventory[book_title] == 0:
                    del inventory[book_title]
                    print(inventory)
                else:
                    print(inventory)


    elif action == "lookup":
       return inventory.get(book_title,0)

def main():
    action=""
    def books():
        book_title=input("Enter a book title: ")
        book_title=book_title.title()
        print(book_title)
        return book_title

    def quant():
        quantity=int(input("Enter the book quantity: "))
        return quantity
    
    while action != "exit":
        action=input("Enter your action:\n\"Exit\"\n\"Add\"\n\"Sell\"\n\"Lookup\":\n ").lower()
        if action == "exit":
            print("Exiting Inventory")
            break
        elif action == "add":
            book_title=books()
            quantity=quant()
            manage_bookstore_inventory(inventory, action , book_title, quantity)
        elif action == "sell":
            book_title=books()
            quantity=quant()
            manage_bookstore_inventory(inventory, action , book_title, quantity)
        elif action == "lookup":
            book_title=books()
            qty=manage_bookstore_inventory(inventory, action , book_title)
            print(f"Stock quantity for {book_title} is {qty}\n")
        else:
            print("Enter valid choice")
    
main()


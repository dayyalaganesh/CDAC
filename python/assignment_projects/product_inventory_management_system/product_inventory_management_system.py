
products = [
    {"id": 1, "name": "laptop", "category": "electronic", "price": 55000, "quantity": 2},
    {"id": 2, "name": "smartphone", "category": "electronic", "price": 10000, "quantity": 1}
]

id_counter = max([p["id"] for p in products], default=0)


# ------------------------------------------------------------------------------------------------------------------
def menu():

    print("\n")
    print("1.ADD PRODUCT")
    print("2.SEARCH PRODUCT")
    print("3.VIEW PRODUCT")
    print("4.UPDATE PRODUCT")
    print("5.DELETE PRODUCT")
    print("6.EXIT")

    try:
        print("\n")
        choice = int(input("ENTER THE OPTION: "))
        return choice
    except ValueError:
        return -1


# ------------------------------------------------------------------------------------------------------------------
def add_product():

    global id_counter

    try:
        name = input("ENTER PRODUCT NAME: ").strip()
        category = input("ENTER CATEGORY: ").strip()
        price = float(input("ENTER PRICE: "))
        quantity = int(input("ENTER QUANTITY: "))

        if not name or not category:
            print("NAME AND CATEGORY CANNOT BE EMPTY")
            return

        if price < 0 or quantity < 0:
            print("PRICE AND QUANTITY CANNOT BE NEGATIVE")
            return

        id_counter += 1

        products.append({
            "id": id_counter,
            "name": name,
            "category": category,
            "price": price,
            "quantity": quantity
        })

        print("PRODUCT ADDED SUCCESSFULLY")

    except ValueError:
        print("\nINVALID INPUT")


# ------------------------------------------------------------------------------------------------------------------
def search_product():

    while True:

        try:
            print("\n")
            print("1.SEARCH WITH PRODUCT ID")
            print("2.SEARCH WITH PRODUCT NAME")
            print("3.BACK")
            print("\n")

            choice = int(input("ENTER THE OPTION: "))

            if choice == 1:
                search_with_id()

            elif choice == 2:
                search_with_name()

            elif choice == 3:
                break

            else:
                print("\nINVALID OPTION")

        except ValueError:
            print("\nINVALID INPUT")


# ------------------------------------------------------------------------------------------------------------------
def search_with_id():

    try:
        product_id = int(input("ENTER PRODUCT ID: "))

        for record in products:

            if record["id"] == product_id:

                print("\n")
                print("                      PRODUCT DETAILS")
                print("_" * 75)
                print(f"ID       : {record['id']}")
                print(f"NAME     : {record['name']}")
                print(f"CATEGORY : {record['category']}")
                print(f"PRICE    : {record['price']:.2f}")
                print(f"QUANTITY : {record['quantity']}")
                print("_" * 75)

                return True

        print("PRODUCT NOT FOUND")
        return False

    except ValueError:
        print("\nINVALID INPUT")
        return False


# ------------------------------------------------------------------------------------------------------------------
def search_with_name():

    search_dict = []

    try:
        print("\n")
        name = input("ENTER PRODUCT NAME: ").strip().lower()

        for record in products:

            if name == record["name"].lower():
                search_dict.append(record)

        if len(search_dict) == 0:
            print("\nPRODUCT NOT FOUND")
            return False

        print("\n")
        print("_" * 105)
        print(f"{'ID':<10}{'NAME':<30}{'CATEGORY':<30}{'QUANTITY':<20}{'PRICE'}")
        print("_" * 105)

        for record in search_dict:

            print(
                f"{record['id']:<10}"
                f"{record['name']:<30}"
                f"{record['category']:<30}"
                f"{record['quantity']:<20}"
                f"{record['price']:.2f}"
            )

        return True

    except Exception as e:
        print(e)
        print("\nINVALID INPUT")
        return False


# ------------------------------------------------------------------------------------------------------------------
def view_product():

    if len(products) == 0:
        print("NO PRODUCTS")
        return

    print("\n")
    print(f"{'ID':<10}{'NAME':<30}{'CATEGORY':<30}{'QUANTITY':<20}{'PRICE'}")
    print("_" * 105)

    for record in products:

        print(
            f"{record['id']:<10}"
            f"{record['name']:<30}"
            f"{record['category']:<30}"
            f"{record['quantity']:<20}"
            f"{record['price']:.2f}"
        )


# ------------------------------------------------------------------------------------------------------------------
def delete_product():

    try:
        product_id = int(input("ENTER ID TO DELETE PRODUCT: "))

    except ValueError:
        print("INVALID INPUT FORMAT")
        return

    for record in products:

        if record["id"] == product_id:

            confirm = input(
                "ENTER [OK] TO DELETE PRODUCT "
                "[ANY KEY] TO CANCEL: "
            )

            if confirm.lower() == "ok":

                products.remove(record)
                print("PRODUCT DELETED")

            else:
                print("DELETION CANCELLED")

            return

    print("PRODUCT NOT FOUND")


# ------------------------------------------------------------------------------------------------------------------
def update_product():

    try:
        product_id = int(input("ENTER ID TO UPDATE PRODUCT: "))

    except ValueError:
        print("INVALID INPUT FORMAT")
        return

    for record in products:

        if record["id"] == product_id:

            new_name = input(
                "ENTER NEW NAME (PRESS ENTER TO SKIP): "
            ).strip()

            new_price = input(
                "ENTER NEW PRICE (PRESS ENTER TO SKIP): "
            ).strip()

            new_category = input(
                "ENTER NEW PRODUCT CATEGORY (PRESS ENTER TO SKIP): "
            ).strip()

            new_quantity = input(
                "ENTER NEW QUANTITY (PRESS ENTER TO SKIP): "
            ).strip()

            # Update name
            if new_name:
                record["name"] = new_name

            # Update price
            if new_price:
                try:
                    new_price = float(new_price)

                    if new_price < 0:
                        print("PRICE CANNOT BE NEGATIVE")
                    else:
                        record["price"] = new_price

                except ValueError:
                    print("INVALID PRICE")

            # Update category
            if new_category:
                record["category"] = new_category

            # Update quantity
            if new_quantity:
                try:
                    new_quantity = int(new_quantity)

                    if new_quantity < 0:
                        print("QUANTITY CANNOT BE NEGATIVE")
                    else:
                        record["quantity"] = new_quantity

                except ValueError:
                    print("INVALID QUANTITY")

            print("PRODUCT UPDATED SUCCESSFULLY")
            return

    print("PRODUCT NOT FOUND")


# ------------------------------------------------------------------------------------------------------------------
def main():

    while True:

        choice = menu()

        match choice:

            case 1:
                add_product()

            case 2:
                search_product()

            case 3:
                view_product()

            case 4:
                update_product()

            case 5:
                delete_product()

            case 6:
                print("PROGRAM EXITED")
                break

            case _:
                print("INVALID OPTION")


# ------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    main()


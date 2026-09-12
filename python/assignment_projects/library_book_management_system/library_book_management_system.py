import json

def menu():
    print("1.ADD BOOK    :")
    print("2.VIEW BOOK   :")
    print("3.SEARCH BOOK :")
    print("4.DELETE BOOK :")
    print("5.UPDATE BOOK :")
    print("6.SAVE TO FILE:")
    print("7.LOAD TO FILE:")
    print("8.EXIT        :")
    try:
        choice=int(input("ENTER YOUR CHOICE:"))
        return choice
    except:
        return -1


def add_book(catalog:list[dict],next_id:int) -> int:
    try:
        book_id=next_id+1
        book=input("enter the book name:").strip().lower()
        author=input("enter the author name:").strip().lower()
        genre=input("Enter the genre:").strip().lower()
        price=float(input("enter the price:"))
        copies=int(input("enter the copies:"))

        catalog.append(dict(book_id=book_id,
                            name=book,
                            author=author,
                            genre=genre,
                            price=price,
                            copies=copies)
                            )

        print("record successfully added ")

        return book_id

    except:
        print("invalid input price must be a number and copies must be an integer")
        return next_id


def view_book(catalog:list[dict])->None:

    if not catalog:
        print("Empty catalog")
        return

    print(f"{'id':<5}{'name':<10}{'author':<10}{'genre':<20}{'price':<10}{'copies':<15}")
    print("_"*70)

    for record in catalog:
        id,name,author,genre,price,copies=record.values()
        print(f"{id:<5}{name:<10}{author:<10}{genre:<20}{price:<10.2f}{copies:<15}")


def search(catalog:list[dict]):

    while True:
        print("1.SEARCH WITH ID")
        print("2.SEARCH WITH BOOK NAME")
        print("3.SEARCH WITH AUTHOR")
        print("4.BACK")

        try:
            choice=int(input("Enter the choice:"))
        except:
            print("invalid input choice must be an integer")
            continue

        if choice==1 and search_with_id(catalog):
            break
        elif choice==2 and search_with_name(catalog):
            break
        elif choice==3 and search_with_author(catalog):
            break
        elif choice==4:
            break
        else:
            print("invalid input try again")


def search_with_id(catalog):
    try:
        book_id=int(input("enter the id:"))
    except:
        print("invalid input ")
        return False

    for record in catalog:
        if record["book_id"]==book_id:
            b_id,name,author,genre,price,copies=record.values()
            print(f"{'id':<5}{'name':<10}{'author':<10}{'genre':<20}{'price':<10}{'copies':<15}")
            print(f"{b_id:<5}{name:<10}{author:<10}{genre:<20}{price:<10.2f}{copies:<15}")
            return True

    print("id not found")
    return False


def search_with_name(catalog):

    name=input("enter the book name:").strip().lower()

    for record in catalog:
        if record["name"]==name:
            b_id,rname,author,genre,price,copies=record.values()
            print(f"{'id':<5}{'name':<10}{'author':<10}{'genre':<20}{'price':<10}{'copies':<15}")
            print(f"{b_id:<5}{rname:<10}{author:<10}{genre:<20}{price:<10.2f}{copies:<15}")
            return True

    print("name not found")
    return False


def search_with_author(catalog):

    author=input("enter the author name:").strip().lower()

    for record in catalog:
        if record["author"]==author:
            b_id,name,author,genre,price,copies=record.values()
            print(f"{'id':<5}{'name':<10}{'author':<10}{'genre':<20}{'price':<10}{'copies':<15}")
            print(f"{b_id:<5}{name:<10}{author:<10}{genre:<20}{price:<10.2f}{copies:<15}")
            return True

    print("author not found")
    return False


def delete(catalog:list[dict],next_id):

    try:
        id=int(input("enter the id:"))
    except:
        print("invalid")
        return next_id

    for record in catalog:
        if record["book_id"]==id:
            catalog.remove(record)
            print("book deleted successfully")
            return next_id

    print("id not found")
    return next_id


def update_book(catalog:list[dict]):

    try:
        book_id=int(input("enter the book id to update values:"))
    except:
        print("invalid input")
        return

    for record in catalog:
        if record["book_id"]==book_id:
            book_name=input("enter book name (press enter to skip):").strip()
            author=input("enter author name  (press enter to skip):").strip()
            price=input("enter price (press enter to skip):").strip()
            copies=input("enter the copies (press enter to skip):").strip()

            if book_name:
                record["name"]=book_name.lower()

            if author:
                record["author"]=author.lower()

            if price:
                try:
                    record["price"]=float(price)
                except ValueError:
                    print("invalid input format, kept old value")

            if copies:
                try:
                    record["copies"]=int(copies)
                except ValueError:
                    print("invalid input format, kept old value")

            print("updated successfully")
            return

    print("not found ")
    return


def save_to_file(catalog):

    with open("library.txt","w") as file:
        json.dump(catalog,file,indent=4)

    print("catalog saved to file")


def load_to_file(catalog):

    try:
        with open("library.txt","r") as file:
            data=json.load(file)

            catalog.clear()
            catalog.extend(data)

            max_id=max([b["book_id"] for b in catalog],default=0)

            view_book(catalog)

            return max_id

    except FileNotFoundError:
        print("file not found")
        return 0


def main():

    catalog=[]
    next_id=0

    while True:

        choice=menu()

        match choice:

            case 1:
                next_id=add_book(catalog,next_id)

            case 2:
                view_book(catalog)

            case 3:
                search(catalog)

            case 4:
                next_id=delete(catalog,next_id)

            case 5:
                update_book(catalog)

            case 6:
                save_to_file(catalog)

            case 7:
                next_id=load_to_file(catalog)

            case 8:
                break

            case _:
                print("Invalid input!")


if __name__=="__main__":
    main()
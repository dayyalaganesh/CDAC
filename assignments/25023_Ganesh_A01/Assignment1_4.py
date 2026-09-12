"""
### Exercise 4: Odd or Even Checker
Write a program that prompts the user for an integer and prints whether it is even or odd.
* **Sample Input**: `7`
* **Sample Output**: `7 is an Odd number.`
"""
def main():
    num=int(input("Enter positive number: "))
    if num % 2 == 0:
        print(f"{num} is even number")
    else:
         print(f"{num} is odd number")

main()
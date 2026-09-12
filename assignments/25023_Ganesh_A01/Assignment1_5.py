"""
### Exercise 5: Basic Operator Calculator
Create a program that takes two numbers and a math operator (`+`, `-`, `*`, `/`) from the user, performs the corresponding calculation, and prints the result.
* **Sample Input**: `num1=15`, `num2=3`, `operator='/'`
* **Sample Output**: `Result: 5.0`
"""

def main():
    n = int(input(" Ënter First Number: "))
    m = int(input(" Enter Second Number: "))

    operator = input("Enter any Operator\n + (Addition), - (Substraction), * (Mutiplication), / (Division) : ")

    if operator == "*":
        print(f"{n} {operator} {m}= {n * m} ")
    elif operator == "+":
        print(f"{n} {operator} {m}= {n + m} ") 
    elif operator == "-":
        print(f"{n} {operator} {m}= {n - m} ")
    elif operator == "/":
        print(f"{n} {operator} {m}= {n / m:.1f} ") 
    else:
        print(" Invalid Operator ")             


main()


 


    
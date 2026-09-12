"""
Exercise 3: Prime Number Checker
Write a program that checks whether a positive integer entered by the user is a prime number.

Logic: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
Sample Input: 17
Sample Output: 17 is a prime number.
"""
def main():
    num=int(input("Enter the positive number: "))
    if num<=1:
        print(f"{num} is not a prime number")
    else:
        limit=num//2
        is_prime=True
        for i in range(2, limit+1):
            if num% i==0:
                is_prime=False
        if is_prime:
            print(f"{num} is a prime number")
        else:
            print(f"{num} is not a prime number")

main()
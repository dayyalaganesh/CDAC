"""
### Exercise 6: Sum of N Natural Numbers
Write a script that accepts a positive integer $N$ from the user and calculates the sum of all natural numbers up to $N$.
* **Formula**: sum_{i=1}^{N} i = frac{N(N+1)}{2}$
* **Sample Input**: `N = 10`
* **Sample Output**: `Sum: 55`
"""
def main():
    N=int(input("Enter a number: "))
    sum=0
    if N<1:
        print("Not a Natural number")

    for i in range (1,N+1):
        sum= sum+i
    print(f"Total sum of {N} natural number is {sum}")    

main()
"""
### Exercise 2: Fibonacci Sequence Generator
Write a Python script to print the first $N$ terms of the Fibonacci sequence, where $N$ is provided by the user.
* **Fibonacci sequence**: $0, 1, 1, 2, 3, 5, 8, 13, 21, \dots$
* **Sample Input**: `N = 6`
* **Sample Output**: `0, 1, 1, 2, 3, 5`
"""

def main():
    n = int(input("Enter the Number: "))
    num_1 = 0  
    num_2 = 1
    
    for i in range(n):
        print(num_1)
        next_num = num_2 + num_1
        num_1 = num_2
        num_2 = next_num
            
main()    
   


   
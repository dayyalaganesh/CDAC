"""
Exercise 9: The Josephus Elimination Game
Scenario: A group of N soldiers (numbered 1 to N) stand in a circle. Starting from the first soldier, every K-th 
soldier is eliminated from the circle. The count continues with the next remaining soldier, moving clockwise. 
This process repeats until only one soldier remains. Write a program that prompts the user to enter N(number of soldiers) and 
K(elimination interval). Simulate the game using a list and print the order of eliminations and the final survivor.

Sample Input: N = 5, K = 2
Sample Output:
Soldier circle initialized: [1, 2, 3, 4, 5]
Eliminated soldier: 2 (Remaining: [1, 3, 4, 5])
Eliminated soldier: 4 (Remaining: [1, 3, 5])
Eliminated soldier: 1 (Remaining: [3, 5])
Eliminated soldier: 5 (Remaining: [3])
The sole survivor is: 3
"""
def main():
    N=int(input("Enter number of soldiers: "))
    K=int(input("Enter value of K: "))
    k=K
    l=[0]*N
    for i in range(N):
        l[i] = i+1
    print(f"Soldier circle initialized: {l}")
    index = 0
    while len(l) != 1:
        index = (index + K -1) % len(l)
        eliminated=l.pop(index)
        print(f"Eliminated soldier: {eliminated} (Remaining: {l})")
    print(f"The sole survivor is: {l[0]}")
main()
"""
Exercise 7: Manual Substring Counter
Write a program that prompts the user to enter a main text string and a substring.
Count how many times the substring appears in the main string without using Python's built-in .count() method.

Sample Input: (User inputs main string "banana" and substring "an")
Sample Output: 2
"""
def main():
    string = input("Enter the Input : ").lower()
    sub_string = input("Enter the Substring : ").lower()
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
      if string[i:i + len(sub_string)] == sub_string:
         count += 1
    print(count)        

main()    

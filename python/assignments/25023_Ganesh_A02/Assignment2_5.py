"""
Exercise 5: Custom Title Case Formatter
Write a program that accepts a string input from the user and outputs it in Title Case (capitalizing the first letter of each word and lowercasing the remaining letters). Do not use Python's built-in .title() method.

Sample Input: "WELCOME TO BANGALORE CITY"
Sample Output: "Welcome To Bangalore City"
"""
def main():
    sen = input("Please Enter the Sentence: ")
    sen1=sen.lower()
    out=" ".join(word.capitalize() for word in sen1.split())
    print(out)

main()    
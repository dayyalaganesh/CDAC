"""
Exercise 1: Sentence Analysis (Character & Word Count)
Write a Python program that prompts the user to enter a sentence. The program must count and display:

The total number of characters (including spaces and punctuation).
The total number of words.
Sample Input: "Learning Python is fun!"
Sample Output:
Total Characters: 23
Total Words: 4
"""
def main():
    str1=input("Enter a sentence: ")
    charcount=len(str1)
    print(f"Total Character: {charcount}")
    l=str1.split(" ")
    print(f"Total Words: {len(l)}")
    
main()
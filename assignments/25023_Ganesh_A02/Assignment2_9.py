"""
### Exercise 9: Longest Palindromic Substring

Write a program that prompts the user to enter a text string and finds the longest substring within 
it that reads the same forward and backward.If there are multiple palindromic substrings of the same maximum length, 
print any one of them.

- **Sample Input**: `"babad"`
- **Sample Output**: `"bab"` (or `"aba"`)
- **Sample Input**: `"cbbd"`
- **Sample Output**: `"bb"`
"""
def main():
    textString=input("Enter a text string: ")
    long_palindrome=""
    test1=textString[0]*len(textString)
    for i in range(len(textString)):
        for j in range(len(textString)+1):
            test1 = textString[i:j]
            if test1 == test1[::-1]:
                if len(test1) > len(long_palindrome):
                    long_palindrome=test1
    print(long_palindrome)
  
main()
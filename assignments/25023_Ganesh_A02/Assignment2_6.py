"""
Exercise 6: Shift Cipher Encrypter
Write a program that prompts the user for a text string and a shift integer, and encrypts the text using a Caesar cipher. It should shift each alphabetical character in the string by the specified shift number down the alphabet. Maintain uppercase and lowercase characters, and leave spaces or punctuation marks completely unchanged.

Sample Input: (User inputs string "Vinod" and shift 3)
Sample Output: "Ylqrg"
"""
def main():
    str1=input("Enter a string: ")
    shift=int(input("Enter a shift: "))
    a=''.join([chr(ord(c)+shift) for c in str1])
    print(a)
main()
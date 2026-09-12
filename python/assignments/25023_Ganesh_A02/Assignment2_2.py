'''
Write a program that takes a string input from the user, reverses the string, converts the entire reversed string to uppercase, and prints the result.
- **Sample Input**: `"Bangalore"`
- **Sample Output**: `"EROLAGNAB"`
'''
def main():
    word=input("Enter any string: ")
    newword=word[::-1].upper()
    print(newword)

main()
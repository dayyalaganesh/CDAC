"""
### Exercise 8: Name Anonymizer

Write a program that prompts the user to enter a full name (first name, middle name, last name) 
and anonymizes it.The output should print the initials of the first and middle names followed by 
the full last name. If the name consists of only a single word, print it as-is.

- **Sample Input**: `"Vinod Kumar Kayartaya"`
- **Sample Output**: `"V. K. Kayartaya"`
- **Sample Input**: `"Bangalore"`
- **Sample Output**: `"Bangalore"`
"""
def main():
    name=input("Enter the name: ")
    n=name.split(" ")
    
    if len(n)==1:
        print(n[0].capitalize())
    elif len(n)>1 :
            a=[str(word[0].upper()) for word in n[0::-1]]
            str1=" "
            for i in range(len(n)-1):
                 str1 += n[i][0].upper() + ". "
            str1 += n[-1][0].upper() + n[-1][1:]
            print(str1)
            
main()
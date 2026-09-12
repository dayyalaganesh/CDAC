''' 
### Exercise 3: Email Domain Extractor

Write a program that prompts the user to enter an email address string. Extract the domain name (the part after the `@`) and print it. If the string is not a valid email (does not contain exactly one `@`), print `"Invalid Email"`.

- **Sample Input**: `"vinod@vinod.co"`
- **Sample Output**: `"vinod.co"`
- **Sample Input**: `"vinod.co"`
- **Sample Output**: `"Invalid Email"`
'''

def main():
    mail=input("Enter valid email ID:\n")
    if mail.find("@")==-1: #checked whether mail is valid or not (presence of @)
        print("Invalid Email")
    else:
        newMail= mail.split("@")  #Split the mail in two at @ symbol
        print(newMail[1])  #printed the 2nd half part only which was required
            
main()
"""
### Exercise 12: Date Validator & Pretty Formatter
Write a program that prompts the user to enter a date string in the format `"DD/MM/YYYY"`. 

> [!WARNING]
> Do not use any built-in date/time library functions (such as the `datetime` or `time` modules) to format or validate the dates. You must parse and split the string manually, and use a custom tuple of month names for the pretty output if needed.

Your program must:
1. Verify if the date is valid. To be valid:
   * The month must be between `1` and `12` inclusive.
   * The day must be valid for that specific month (e.g., April, June, September, November have 30 days; others have 31 days).
   * For February, the day must be at most `29` in a leap year (divisible by 4, except for centuries not divisible by 400) and 
   at most `28` in standard years.
2. If the date is valid, use a tuple of month names `("January", "February", ...)` to format and print the date in a
 long-form readable layout: `"MonthName DD, YYYY"`.
3. If the date is invalid, print `"Invalid Date"`.

* **Sample Input**: `"26/08/2026"`
* **Sample Output**: `"August 26, 2026"`
* **Sample Input**: `"29/02/2026"`  (2026 is not a leap year)
* **Sample Output**: `"Invalid Date"`
* **Sample Input**: `"31/04/2026"`  (April only has 30 days)
* **Sample Output**: `"Invalid Date"`
"""
def main():
   months=("January", "February", "March", "April", "May", "June", "July", "August", "Septemeber", "October", "November","December")
   date1=input("Enter the date in the form DD/MM/YYYY: ")
   l=date1.split("/")
   print(l)
   l1=[0]*len(l)
   for i in range(len(l)):
      l1[i]=int(l[i])
   print(l1)
   if 0< l1[1] <=12:
      is_leap= l1[2] % 400 == 0 or l1[2] % 4==0 and l1[2] % 100 != 0
      if l1[1] == 2:
         maxDays=29 if is_leap else 28   
      elif l1[1] in (4,6,9,11):
         maxDays=30
      else:
         maxDays=31
      if 1<= l1[0] <= maxDays:
         print(f"{months[l1[1]-1]} {l1[0]}, {l1[2]}")
      else:
         print("Invalid Date")
              
   else:
      print("Invalid Date")

main()
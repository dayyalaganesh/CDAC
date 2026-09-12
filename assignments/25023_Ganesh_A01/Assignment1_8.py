"""
### Exercise 8: Score to Grade Converter
Write a script that takes a numeric test score from the user (0 to 100) and displays a corresponding letter grade based on the following scale:
* 90-100: A
* 80-89: B
* 70-79: C
* 60-69: D
* Below 60: F

"""
def main():
    score = int(input("Enter the score out of 100 \n"))
    if score<=0 or score >100:
        print("Please enter valid score")
    elif score >= 90:
        print("Congratulations you have secured grade A")
    elif score >= 80 and score < 90:
        print("Congratulations you have secured grade B")
    elif score >= 70 and score < 80:
        print("Congratulations you have secured grade C")
    elif score >= 60 and score < 70:
        print("Congratulations you have secured grade D")
    else:
        print("Unfortunately you got garde F")

main()

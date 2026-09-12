"""
Exercise 6: Grading on a Curve
Scenario: A professor wants to adjust exam grades. Prompt the user to enter a list of space-separated test scores.
Convert them to a list of integers. Using a single list comprehension with conditionals, apply the following curve rules:

If a score is below 50, add 10 points.
If a score is 50 or higher, add 5 points.
The maximum possible score is capped at 100 (e.g., a score of 98 becomes 100, not 103). Print the original and the curved grades.
Sample Input: "45 88 30 98 50"
Sample Output:
Original: [45, 88, 30, 98, 50]
Curved: [55, 93, 40, 100, 55]
"""
def main():
    inint=input("Enter scores separated by space out of 100: ")
    v=inint.split(" ")
    if v and all(score.isdigit() for score in v):
        
        print(v)

        v1=[0]*len(v)
        for i in range(len(v1)):
            v1[i]=int(v[i])
        for i in range(len(v)):
            if 0<=v1[i]<=50:
                v1[i] += 10
            elif 50<v1[i]<=100:
                if v1[i]>95:
                    v1[i]+=100-v1[i]
                else:
                    v1[i]+=5
        print(v1)
    else: 
        print("Enter Valid scores ")

main()
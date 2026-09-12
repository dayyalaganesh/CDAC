"""
Exercise 3: The Cargo Train Scanner
Scenario : A train has wagons carrying different resources:
["coal", "iron", "gold", "coal","timber", "coal"].
The train conductor wants to inspect the cargo.
Write a program that prompts the user to enter a resource type(e.g.,"coal"or"gold")

Print the total number of wagons carrying that resource(using.count()).
If the resource is on the train,print the index of the very first wagon carrying it(using .index()).
If it is not found,print"Resource not found on train!"

Sample Input:"coal" 
Sample Output:Number of coal wagons: 3
First coal wagon is at index: 0

SampleInput:"oil"
SampleOutput:"Resource not found on train!"

"""
def main():
    Wagons = ["coal", "iron", "gold", "coal","timber", "coal"]
    resource = input("Enter a Resource type : ")
    if resource in Wagons:
        count_1= Wagons.count(resource)
        print(f"Number of {resource} wagons :{count_1}")
        print(f"First {resource} wagon is at index {Wagons.index(resource)}")
    else :
        print(" Resource not found on the Train! ")    

main()    
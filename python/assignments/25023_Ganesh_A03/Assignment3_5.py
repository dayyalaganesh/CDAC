"""
Exercise 5:
The Spy's Word Reverser Scenario :A secret agent wants to send an encryptedmessage.
The encryption rule is simple:reverse every word in the sentence,but keep the order of words unchanged.
Write a program that prompts the user for a sentence,splits it,uses a list comprehension to reverse the letters of each word,
and joins them back together.
SampleInput:"Meet me at midnight"
SampleOutput:"teeM em ta thgindim"

"""
def main():
    message = input("Enter the Message : ")
    print(message)
    new_message = message.split()
    str_reversed = [0]*len(new_message)
    str_reversed = [word[::-1] for word in new_message]
    a=" ".join(str_reversed)
    print(a)    

main()    
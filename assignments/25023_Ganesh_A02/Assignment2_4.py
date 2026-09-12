"""
Exercise 4: Vowel & Consonant Frequency
Write a program that prompts the user to enter a string and counts:

The individual frequency of each vowel (a, e, i, o, u), case-insensitively.
The total count of all consonants.
Sample Input: "Vinod Kumar Kayartaya"
Sample Output:
Vowel Frequencies:
a: 5
e: 0
i: 1
o: 1
u: 1
Total Consonants: 12
"""
from pprint import pprint
def main():
    sample = input("Enter a Sentence: ")
    n=sample.lower()
    vowel={"a":0,"e":0,"i":0,"o":0,"u":0}
    const = 0
    for s in n:
        if s in vowel:
            vowel[s]+=1
        elif s.isalpha():
            const +=1
    for v,k in vowel.items():
        pprint(f"{v} : {k} ")                    
    pprint(f"const : {const} ")
main()
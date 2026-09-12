"""
### Exercise 10: Run-Length String Compression

Write a program that prompts the user to enter a text string and compresses it using run-length encoding (listing character counts next to each repeated character). If the compressed string is not smaller in size than the original string, print the original string.

- **Sample Input**: `"aabcccccaaa"`
- **Sample Output**: `"a2b1c5a3"`
- **Sample Input**: `"abcd"`
- **Sample Output**: `"abcd"` (since `"a1b1c1d1"` is longer than `"abcd"`)
"""
def main():
    instr=input("Enter the string: ")
    s=list(instr)
    t=[]
    for char in instr:
        if char not in t:
            t.append(char)
    t2=[0]*len(t)

    for i in range(len(s)):
        for j in range(len(t)):
            if t[j] in s:
                t2[j] = instr.count(t[j])
    for i in range(len(t)):
        print(f"{t[i]}{t2[i]}",end="")

main()
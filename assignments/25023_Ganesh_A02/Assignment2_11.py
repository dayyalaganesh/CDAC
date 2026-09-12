"""
### Exercise 11: Group Anagrams

Write a program that starts with a list of strings defined at the top of your script 
(e.g., `words = ["eat", "tea", "tan", "ate", "nat", "bat"]`) and groups the anagrams 
(words formed by rearranging letters) together. Print the final grouped list of lists.

- **Hardcoded Input**: `words = ["eat", "tea", "tan", "ate", "nat", "bat"]`
- **Sample Output**: `[['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]`
"""
def main():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    anagram={}
    for word in words:
        sorted_words="".join(sorted(word))
        if sorted_words in anagram:
            anagram[sorted_words].append(word)
            print(anagram)
        else:
            anagram[sorted_words]=[word]
    finalList= list(anagram.values())
    print(finalList)

main()

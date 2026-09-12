"""
Exercise1:TheWizard'sMagicBag
Scenario:A wizard has a magic bag containing a sequence of items:
["staff", "potion","spellbook"].
When the wizard steps through a magic portal,two things happen:

1.A new item enters the bag(prompts the user to input the item name to append to the end).
2.The oldest item in the bag(at index 0)is dissolved and ejected. Write a program to simulate this portal transition and print the final bag contents.

SampleInput:(Userinputs"amulet")
SampleOutput:

Portal transition activated!Ejected oldest item: staffCurrent items in the magic bag: ['potion', 'spellbook', 'amulet']

"""

def main():
     magic_bag = ["staff","potion","spellbook"]
     new_item = input("Enter the Item Name to be added to the bag: ")
     magic_bag.append(new_item)
     eject= magic_bag.pop(0)
     print(f"Portal transition activated! Ejected oldest item: {eject} Current items in the magic bag: {magic_bag}")
    
main()    
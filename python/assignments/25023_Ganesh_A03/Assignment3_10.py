"""
Exercise 10: Snake Game Board Renderer
Scenario: Render a simple 2D text game board. Write a program that performs the following steps in sequence:

1. Creates a 5 × 5 grid filled with dots "." represented as a nested list.
2. Places a food item "F" at grid position [2, 3].
3. Prompts the user to enter coordinate inputs: a row and a col (integers between 0 and 4) for the snake's head.
4. Places the snake's head "S" at the user-supplied coordinate [row, col], overwriting the character at that position.
5. If the user-supplied coordinates are exactly [2, 3], print the message "Yum! The snake ate the food!"
 (the snake "S" will occupy index [2, 3] on the printed board, overwriting the "F").
6. Prints the grid neatly line-by-line (each row's elements separated by spaces).

Sample Input: (User inputs Row 0 and Column 3)
Sample Output:
. . . S .
. . . . .
. . . F .
. . . . .
. . . . .

Sample Input: (User inputs Row 2 and Column 3)
Sample Output:
. . . . .
. . . . .
. . . S .
. . . . .
. . . . .
Yum! The snake ate the food!
"""
def main():
    grid=[["." for _ in range(5)] for _ in range(5)]

    grid[2][3]="F"
    while True:
        try:
            row=int(input("Enter row [0-4]: "))
            if not (0 <= row <= 4):
                print("Error: Row must be between 0 and 4. Try again.\n")
                continue
            col=int(input("Enter Column [0-4]: "))

            if not (0 <= col <= 4):
                print("Error: Column must be between 0 and 4. Try again.\n")
                continue
            break
        
        except ValueError:
            print("Error: Please enter valid integers. Try again.")
            
    grid[row][col]="S"
    for i in grid:
        print(" ".join(i))
    if row==2 and col==3:
        print("Yum! The snake ate the food!")

main()
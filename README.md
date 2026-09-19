# Water Color Sort
A recreation of the Water Color Sort puzzle game by Python using the Turtle graphics library. Created and Finished in Feb 2024.

## Game Rules
The goal of Water Color Sort is to sort the colored water so that each bottle contains only single color. Each bottle can hold up to four layers of water.

To make a move:
1. Select a bottle containing water.
2. Select another bottle to pour into.
3. Water can only be poured into a bottle if:
    - the destination bottle has empty space and its top color matches the color being poured.
    - the destination bottle is empty.
    - Note: Connected layers of the same color are poured together when there is enough space.

## Features
- Three difficulty levels: Easy, Hard, and Expert
- Randomized color and bottle configurations
- Recursive pouring of connected layers of the same color
- Mouse-based bottle selection
- Undo, Restart, Optional extra empty bottle
- Custom graphical interface built with Python Turtle

## Technologies
- Python
- Turtle
- Python standard libraries (`random`, `copy`, `pathlib`)

## How to Run
5. Enter `0`, `1`, or `2` in the terminal to select a difficulty.

## Error in name of the Undo button
My apologies of confused the meanings of redo and undo because my English wasn't very good when I started this project, only just realized it now. Despite the "redo" labl, this button functions as a one-step undo and restores the game state before the previous move.

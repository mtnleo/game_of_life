# Game of Life (by John Conway)
This repository is a recreation of the Game of Life, created by mathematician John Conway
in 1970.

Game rules were created by using a matrix and displaying it using the Pygame engine.

<img width="899" alt="Screenshot 2024-05-10 at 11 53 51 AM" src="https://github.com/mtnleo/game_of_life/assets/118694913/35fbaf5d-fdfb-4287-b70d-cd336b4c02e1">

How to run?
- Via .exe
  1. Install the exe file
  2. Run the game
- Via CLI
  1. Make sure you have Python3 and Pygame installed
  2. Go to the game directory
  3. Run _main.py_

Playing:
- Press **Left-Click** to draw a tile on the screen.
- Press **Right-Click** to delete a tile previously drawn.
- Hit **Spacebar** to start the simulation

Game of Life's rules:
Conway's Game of Life is a zero-player game on a grid. Cells are alive or dead. They evolve based on the
state of their 8 neighbors:
- A live cell with 2-3 neighbors survives.
- Any other live cell dies (lonely or overcrowded).
- A dead cell with exactly 3 live neighbors comes alive.

This simple rule set can lead to surprising complexity! See more in its [Wikipedia article]([url](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life))

- mtnleo

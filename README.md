# Demineur

A small command-line Minesweeper game written in Python. The game asks the player for a row and a column, reveals the chosen cell, and ends if the player hits a mine. [file:26]

## Files

- `demineur.py` — main game script. [file:26]
- `.gitignore` — ignores Python cache and virtual-environment files for Git. [web:6]
- `requirements.txt` — dependency list for this project.

## Requirements

- Python 3.x [file:26]
- No external Python package is imported in the script beyond the standard library `random`. [file:26]

## Run the game

```bash
python demineur.py
```

## Suggested next improvements

- Add real doctests or unit tests, because the file calls `doctest.testmod()` but does not currently include executable doctest examples. [file:26]
- Move the interactive game loop under `if __name__ == "__main__":` so the module can be imported without starting the game immediately. [file:26]
- Add a screenshot or terminal GIF to the repository page.

## Notes

The current script is a console game and uses a fixed 5x5 grid with mines placed randomly. [file:26]

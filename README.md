# My Python Programs

This repository contains small Python programs and game projects, including command-line exercises and GUI applications.

## Python Files

| File | Description |
| --- | --- |
| `calculator.py` | A modern scientific calculator built with CustomTkinter. It supports basic arithmetic, parentheses, percentages, scientific functions, constants, keyboard input, and safe AST-based expression evaluation. |
| `GuessWhoGameV2.py` | A command-line "Guess Who?" style game. The player thinks of a character, answers yes/no questions, and the program narrows the character list until it makes a guess. |
| `rock_paper_scissors.py` | A Tkinter GUI version of Rock Paper Scissors with clickable move buttons, computer choices, win/tie/loss messages, score tracking, reset, and quit controls. |
| `codedex/rock_paper_scissors.py` | A command-line Rock Paper Scissors game made for a Codedex Python course checkpoint. The player chooses a numbered move, the computer chooses randomly, and the result is shown. |
| `codedex/rock_paper_scissors_lizard_spock.py` | A command-line Rock Paper Scissors Lizard Spock game made for a Codedex Python course checkpoint. It expands the standard game with lizard and Spock choices. |

## Requirements

- Python 3.x
- Tkinter, which is usually included with standard Python installations, for `rock_paper_scissors.py`
- `customtkinter` for `calculator.py`

Install CustomTkinter with:

```bash
pip install customtkinter
```

## Running Programs

Run any script from the repository root with Python:

```bash
python calculator.py
python GuessWhoGameV2.py
python rock_paper_scissors.py
python codedex/rock_paper_scissors.py
python codedex/rock_paper_scissors_lizard_spock.py
```

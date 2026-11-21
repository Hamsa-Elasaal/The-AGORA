# The Agora Quiz

**The Agora** is a small interactive quiz game built with **Python and Tkinter**. It lets players test their knowledge through two quiz categories: Python programming and world capital cities.

The project focuses on practicing Python fundamentals, GUI development, event handling, and basic game logic.

## Features

- **Player welcome screen** to enter a name before starting.
- **Two quiz categories:**
  - Python — code-reading and programming fundamentals.
  - Capitals — questions about world capitals.
- **Randomized questions** each time a quiz starts.
- **Multiple-choice answers** with immediate visual feedback.
- **Weighted scoring** — questions have different point values.
- **Progress and live score** displayed during the quiz.
- **Results screen** showing the final score, accuracy, correct answers, and incorrect answers.
- **Learning links** shown after an incorrect answer.
- **Replay options** to play again, change category, or return home.

## Built With

- Python
- Tkinter (Python's standard GUI library)
- Python standard-library modules: `random` and `webbrowser`

No third-party Python packages are required.

## Run the Game

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

```bash
python agora_quiz.py
```

A desktop window should open. Enter your name, choose a category, and start playing.

> **Note:** Tkinter is included with many standard Python installations. If your Python installation does not include Tkinter, install the Tk support package for your operating system.

## Project Structure

```text
The-AGORA/
├── agora_quiz.py   # Main Python desktop application (Tkinter)
├── index.html      # Browser-based version / web prototype
└── README.md       # Project documentation
```

## How to Play

1. Enter your name.
2. Select **Python** or **Capitals**.
3. Answer the multiple-choice questions.
4. Review the feedback and your score.
5. View your results, then replay or choose another category.

## Project Scope

This is an educational quiz-game project. The question bank is currently defined directly in the source code, and scores are calculated for the current play session. It does not currently include user accounts, a database, or persistent leaderboards.

---

*Built as a hands-on project to explore Python programming and desktop GUI development.*

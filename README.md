# 🪓 Hangman Game (Python)

## 🎯 Project Overview
This is a **simple text-based Hangman game** built using **Python**.  
The player guesses a hidden word one letter at a time, with only 6 incorrect guesses allowed.  
It’s a beginner-friendly project demonstrating Python basics like loops, conditionals, strings, and lists.

---

## 🧠 Key Features
- 🎲 Random word selection from a predefined list  
- 📝 Tracks guessed letters and attempts left  
- 🚫 6 incorrect guesses allowed before losing  
- ✅ Clear text-based user interface  
- 🔁 Works in any terminal or IDE (no graphics required)

---

## 🧰 Technologies Used
- **Python 3.x**
- Built-in modules: `random`

---

## 📂 Project Structure
hangman_game/
│
├── hangman_game.py # Main game script
└── README.md # Project documentation

yaml
Copy code

---

## 🚀 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/Chaitanyasarkate/CodeAlpha_hangman_game.git
Navigate to the folder:

bash
Copy code
cd hangman-game
Run the game:

bash
Copy code
python hangman_game.py
🕹️ How to Play
The program randomly selects a secret word.

Guess one letter at a time.

Each incorrect guess reduces your remaining attempts.

You win if you guess all letters before running out of attempts.

You lose if you reach 0 attempts.

🧩 Example Gameplay
vbnet
Copy code
🎯 Welcome to Hangman Game!
Guess the word letter by letter.
You have 6 incorrect attempts allowed.

Word:  _ _ _ _ _ _
Attempts left: 6
Enter a letter: a
✅ Good job! That letter is in the word.
📚 Concepts Used
random.choice()

while loops

if-else conditions

String and list manipulation

User input and validation

💡 Future Improvements
Add replay option after each game

Include difficulty levels (easy, medium, hard)

Display a hangman ASCII art

Read words from an external file

Track player score and best attempts

👨‍💻 Author
Chaitanya Sarkate
📧 your.email@example.com
🌐 GitHub Profile

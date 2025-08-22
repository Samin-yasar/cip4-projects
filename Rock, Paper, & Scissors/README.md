# 🎮 Rock, Paper, Scissors Game

A simple **Rock, Paper, Scissors** game written in **pure Python**, designed to be compatible with the **Code in Place IDE** (no external libraries required).  
The game is **best of 5 rounds** — the first to reach 5 wins is crowned the champion! 🏆  

---

## ✨ Features

- Classic **Rock, Paper, Scissors** rules.
- **First to 5 wins** (instead of single round).
- Input validation for smoother gameplay.
- Ability to **quit anytime** by typing `quit`.
- **Replay option** after each match.
- Runs entirely in the terminal (no installation needed).
- Uses only Python's standard library (compatible with Code in Place).

---

## 🛠️ How to Play

1. Run the script in the terminal:
   ```bash
   python main.py
   ```

2. Enter your move:
   - `rock`
   - `paper`
   - `scissors`

3. The computer will randomly pick its move:
   - Each move has an equal **1/3 probability** of being chosen (no bias).
   - Example:
     ```
     Round 1
     Enter your move (rock, paper, scissors): rock
     Computer chose: scissors
     ✅ You win this round!
     Score → You: 1 | Computer: 0
     ```

4. First to **5 points wins** the match.

5. After the game ends, choose whether to **play again** or exit.

---

## 📊 Fairness & Randomness

- The computer’s move is chosen using Python’s built-in:
  ```python
  random.choice(["rock", "paper", "scissors"])
  ```
- Each option (`rock`, `paper`, `scissors`) has equal probability.
- Over many rounds, the distribution is statistically balanced.

---

## 🔧 Requirements

- Python 3.x  
- Works in **Code in Place IDE** and standard Python environments.  
- No third-party libraries needed.

---

## 🚀 Future Improvements

- Add more moves (`lizard` and `spock`).
- Track **match history**.
- Show **progress bar style score display**.
- Add **multiplayer mode**.

---

## 👩‍💻 Author

Made with 💙 by [Samin Yasar](https://samin-yasar.github.io) 
Inspired by the spirit of **[Code in Place](https://codeinplace.stanford.edu/cip4/share/BpYSSgwP79h3S7xRg2Mc)** ✨

---

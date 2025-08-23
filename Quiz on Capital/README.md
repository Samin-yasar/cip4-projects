# **Capital Cities Quiz Game**

## **🗺️ Project Description**

This is a command-line quiz game built in Python that tests your knowledge of countries and their capital cities. The game features multiple difficulty levels, a scoring system, life management, and streak bonuses to provide an engaging and challenging experience. You can play in either a normal (country to capital) or reverse (capital to country) mode, with hints and skips available to help you along the way.

## **✨ Features**

* **Multiple Difficulty Levels:** Choose from Easy, Medium, and Hard modes, each with unique rules, point values, and lives.  
* **Dynamic Question Modes:** Questions are randomly presented in both "normal" (country to capital) and "reverse" (capital to country) formats.  
* **Scoring & Streaks:** Earn points for correct answers and receive a bonus for answering questions correctly in a row.  
* **Life System:** Start with a set number of lives and lose one for each incorrect answer. The game ends when you run out of lives.  
* **Hints & Skips:** Use a limited number of hints to reveal the first letter of the answer or skip a question you don't know.  
* **High Score Tracking:** Your highest score is saved to a file, so you can always try to beat your personal best.

## **🚀 How to Run the Game**

### **Prerequisites**

To run this game, you need to have Python 3 installed on your system.

### **Steps**

1. **Save the files:** Ensure both main.py and data.py (which contains the countries\_and\_capitals and common\_countries\_and\_capitals dictionaries) are in the same directory.  
2. **Open a terminal:** Navigate to the directory where you saved the files.  
3. **Run the script:** Execute the following command:  
   python main.py

## **📂 Project Structure**

* **main.py**: The main game logic, including the QuizGame class, game loop, and all core functions.  
* **data.py**: A separate file that stores the dictionaries of countries and capitals used for the quiz questions.  
* **highscore.txt**: A file created by the game to store the high score.

## **✍️ Author**

This game was developed by [Samin Yasar](https://samin-yasar.github.io) as a fun project to practice Python programming concepts especially for Code in Place IDE. Check [Code in Place](https://codeinplace.stanford.edu/cip4/share/zea1uKJ6DiPl21uMD7ei)

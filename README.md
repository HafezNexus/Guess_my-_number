# 🎯 Guess My Number

A simple but challenging **Guess My Number** game built with Python.

The computer chooses a secret number, and your goal is to guess it with as few attempts and hints as possible. The faster and smarter you play, the higher your score! 😈

## ✨ Features

- 🎮 Multiple difficulty levels
- ⚙️ Custom number range
- 🌐 English and Persian language support
- 💡 Hint system
- 🏆 High score system
- 📊 Dynamic scoring
- ⏱️ Time-based bonus
- 🏅 Ranking system
- 😂 Random messages and jokes
- 🔄 Replay system
- 💾 Saves your high score
- 🧩 Modular multi-file structure
- 📦 Ready-to-run `.exe` version

## 🎮 Difficulty Levels

| Level | Number Range |
|---|---|
| 🟢 Easy | 1 - 20 |
| 🟡 Medium | 1 - 100 |
| 🔴 Impossible | 1 - 1000 |
| ⚙️ Custom | Choose your own range |

## 💡 Hint System

You can use up to **3 hints** during a game.

| Hint | Cost |
|---|---:|
| Even / Odd | -5 |
| Divisible by 5 | -5 |
| Prime? | -15 |
| Last Digit | -20 |

Using hints can help you find the number, but they will reduce your score.

## 🏅 Ranking System

Your final score determines your rank:

- 💀 **Beyond Legend** — 120+
- ⚡ **Score Breaker** — 100+
- 👑 **Legend** — 90+
- 🥇 **Master** — 75+
- 🥈 **Pro** — 60+
- 🥉 **Beginner** — 40+
- 🤡 **Lucky Potato** — below 40

## 📁 Project Structure

```text
Game_v1/
│
├── dist/
│   └── main.exe
│
├── main.py
├── high_score.txt
│
├── game/
│   ├── core.py
│   ├── difficulty.py
│   ├── helping.py
│   ├── menu.py
│   └── scoring.py
│
└── unitle/
    ├── helpers.py
    └── language.py
```

## 🚀 How to Run

### 🐍 Run with Python

Make sure Python is installed, then run:

```bash
python main.py
```

### 📦 Run the Executable

You can also run the ready-to-use version without running the Python source code.

Open the `dist` folder and run:

```text
main.exe
```

## 🧠 What I Learned

This project helped me practice:

- Functions
- Modules and packages
- Imports
- Loops
- Conditions
- Exception handling
- File handling
- Random numbers
- `time.monotonic()`
- Lists
- String formatting
- Basic mathematics
- Code organization
- Multi-file Python projects
- Creating an executable with PyInstaller

## 🔮 Future Ideas

- 🎨 Better terminal UI
- 📈 Game statistics and history
- 🏆 Leaderboard
- 👤 Player profiles
- 🔊 Sound effects
- 🧠 Smarter difficulty system
- 📊 More detailed scoring
- 💾 Saving player statistics

## 👨‍💻 Creator

**Amir Hafez**

GitHub: **HfezNexus**

---

Have fun, beat the high score, and try not to become a 🤡 **Lucky Potato**. 😈🎯
# Smart Pronunciation Buddy

An AI-powered web application that helps users practice English pronunciation using **Python**, **Flask**, **Google Speech Recognition**, and **Metaphone**. The application listens to the user's pronunciation, converts speech into text, compares it with the expected word using phonetic matching, and provides instant feedback.

## Overview

Smart Pronunciation Buddy is designed to help users improve their English pronunciation through interactive speech practice. 
The application captures spoken input using a microphone, converts it into text with Google Speech Recognition, and compares the pronunciation with the target word using the Metaphone phonetic algorithm and similarity matching.
This project demonstrates the integration of speech recognition, natural language processing concepts, and web development to create an interactive learning experience.
---

## Features
-  Speech input using microphone
-  Converts speech to text using Google Speech Recognition
-  Phonetic comparison using Metaphone
-  Displays pronunciation similarity score
-  Provides pronunciation feedback (Correct, Almost Correct, Incorrect)
-  Simple and user-friendly web interface built with Flask

---

## Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- SpeechRecognition Library
- Google Speech Recognition API
- Phonetics (Metaphone)
- Difflib (SequenceMatcher)

---

## Project Structure

```text
Smart_Pronunciation_Buddy/
│
├── main.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── screenshots/
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Aryasreenambiar20/smart-pronunciation-buddy.git
```

Move into the project folder:

```bash
cd smart-pronunciation-buddy
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python main.py
```
Open your browser and visit:
```
http://127.0.0.1:5000
```

---

## How to Use

1. Enter an English word.
2. Click **Start Speaking**.
3. Pronounce the word clearly.
4. The application listens through the microphone.
5. It converts your speech to text.
6. The pronunciation is compared with the target word.
7. Feedback and similarity score are displayed instantly.

---

## Future Improvements

- AI-based pronunciation scoring using Whisper or other speech models
- Sentence-level pronunciation evaluation
- Accent detection
- Multi-language pronunciation support
- User authentication and progress tracking
- Pronunciation history and analytics
- Audio playback of correct pronunciation

---

##  Author

**Aryasree Nambiar**

- GitHub: https://github.com/Aryasreenambiar20
- LinkedIn: https://www.linkedin.com/in/aryasree-nambiar-bb1311293

---

##  License

This project is developed for educational and learning purposes.

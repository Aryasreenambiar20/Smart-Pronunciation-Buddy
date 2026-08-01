from flask import Flask, render_template, request, jsonify
import speech_recognition as sr
import phonetics
from difflib import SequenceMatcher

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/check", methods=["POST"])
def check():
    target_word = request.form.get("target", "").strip().lower()

    if not target_word:
        return jsonify({
            "spoken": "",
            "result": "failed",
            "message": "No target word provided."
        })

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎙️ Listening... Speak now.")

        # Reduce background noise
        recognizer.adjust_for_ambient_noise(source, duration=1)

        audio = recognizer.listen(source)

        print("✅ Got the audio. Recognizing...")

        try:
            # Recognize speech
            spoken_word = recognizer.recognize_google(audio).lower().strip()

            print("Recognized:", spoken_word)

            # If multiple words are recognized, take the first one
            spoken_word = spoken_word.split()[0]

            target_code = phonetics.metaphone(target_word)
            spoken_code = phonetics.metaphone(spoken_word)

            similarity = SequenceMatcher(
                None,
                spoken_word,
                target_word
            ).ratio() * 100

            print("--------------------------------")
            print("Target Word :", target_word)
            print("Spoken Word :", spoken_word)
            print("Target Code :", target_code)
            print("Spoken Code :", spoken_code)
            print(f"Similarity  : {similarity:.2f}%")
            print("--------------------------------")

            # Decide result
            if target_code == spoken_code:
                result = "correct"
            elif similarity >= 80:
                result = "almost correct"
            else:
                result = "incorrect"

            return jsonify({
                "spoken": spoken_word,
                "result": result,
                "similarity": round(similarity, 2)
            })

        except sr.UnknownValueError:
            print("😕 Could not understand audio")

            return jsonify({
                "spoken": "",
                "result": "failed",
                "message": "Could not understand speech."
            })

        except sr.RequestError:
            print("🌐 Google Speech Recognition service unavailable.")

            return jsonify({
                "spoken": "",
                "result": "failed",
                "message": "Speech recognition service unavailable."
            })


if __name__ == "__main__":
    app.run(debug=True)
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

    print("✅ /check route called")

    target_word = request.form.get("target", "").strip().lower()

    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:

            print("🎙️ Listening... Speak now.")

            recognizer.adjust_for_ambient_noise(source, duration=0.5)

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=4
            )

        print("✅ Audio captured")

        spoken_word = recognizer.recognize_google(audio).lower().strip()

        print("Recognized:", spoken_word)

        if len(spoken_word.split()) > 1:
            spoken_word = spoken_word.split()[0]

        target_code = phonetics.metaphone(target_word)
        spoken_code = phonetics.metaphone(spoken_word)

        similarity = round(
            SequenceMatcher(
                None,
                spoken_word,
                target_word
            ).ratio() * 100,
            2
        )

        if target_code == spoken_code:
            result = "correct"
        elif similarity >= 80:
            result = "almost correct"
        else:
            result = "incorrect"

        return jsonify({
            "spoken": spoken_word,
            "result": result,
            "similarity": similarity
        })

    except sr.WaitTimeoutError:
        return jsonify({
            "spoken": "",
            "result": "failed",
            "message": "No speech detected."
        })

    except sr.UnknownValueError:
        return jsonify({
            "spoken": "",
            "result": "failed",
            "message": "Could not understand your speech."
        })

    except sr.RequestError:
        return jsonify({
            "spoken": "",
            "result": "failed",
            "message": "Speech Recognition service unavailable."
        })

    except Exception as e:
        print(e)

        return jsonify({
            "spoken": "",
            "result": "failed",
            "message": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)
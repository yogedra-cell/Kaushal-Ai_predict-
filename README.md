# Kaushal-Ai_predict-
import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Command processor
def processCommand(c):
    c = c.lower()

    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    elif "open whatsapp" in c:
        speak("Opening WhatsApp")
        webbrowser.open("https://www.whatsapp.com")
    elif "open Facebook" in c:
        speak("Opening Facebook")
        webbrowser.open("https://www.Facebook.com")

if __name__ == "__main__":
    speak("Kaushal AI Activated...")

    while True:
        try:
            r = sr.Recognizer()

            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=15, phrase_time_limit=7)

            print("Recognizing...")
            command = r.recognize_google(audio)

            # Wake Word
            if "kaushal" in command.lower():
                speak("Yes Kaushal")

                with sr.Microphone() as source:
                    print("Kaushal Active...")
                    audio = r.listen(source)

                command = r.recognize_google(audio)
                processCommand(command)

        except sr.UnknownValueError:
            print("Could not understand audio.")

        except sr.RequestError:
            print("Speech service down or no internet.")

        except Exception as e:
            print("Error:", e)


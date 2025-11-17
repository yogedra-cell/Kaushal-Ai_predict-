import speech_recognition as sr
import webbrowser
import pyttsx3

# Initialize recognizer (for speech-to-text) and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

# Function to speak text through speakers
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function that checks command and opens websites
def processCommand(c):
    c = c.lower()   # Convert command to lowercase for easy matching

    # Command to open Google
    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    # Command to open YouTube
    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com")

    # Command to open WhatsApp
    elif "open whatsapp" in c:
        speak("Opening WhatsApp")
        webbrowser.open("https://www.whatsapp.com")


# Main program starts here
if __name__ == "__main__":
    speak("Kaushal AI Activated...")   # Initial startup voice

    while True:
        try:
            r = sr.Recognizer()  # New recognizer instance

            # Use microphone input
            with sr.Microphone() as source:
                print("Listening...")
                # Listen with timeout and phrase time limit
                audio = r.listen(source, timeout=15, phrase_time_limit=7)

            print("Recognizing...")
            command = r.recognize_google(audio)  # Convert speech to text

            # Wake-word detection: AI activates only when user says "Kaushal"
            if "kaushal" in command.lower():
                speak("Yes Kaushal")

                # Listen for actual command after wake word
                with sr.Microphone() as source:
                    print("Kaushal Active...")
                    audio = r.listen(source)

                # Convert second audio input to text and process
                command = r.recognize_google(audio)
                processCommand(command)

        # Errors if speech is not clear
        except sr.UnknownValueError:
            print("Could not understand audio.")

        # Errors if speech service or internet is down
        except sr.RequestError:
            print("Speech service down or no internet.")

        # Any unexpected error
        except Exception as e:
            print("Error:", e)

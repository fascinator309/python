import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

speak("Initilizing Jarvis.........")

if __name__ == "__main__":
    print(__name__)


#listen for the wake word JARVIS
while True:
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..........")
        audio = r.listen(source)

    # recognize speech using Sphinx
    try:
        command = r.recognize_sphinx(audio)
        print("I thinks you said " + r.recognize_sphinx(audio))
    except sr.UnknownValueError:
        print("Sphinx could not understand audio")
    except sr.RequestError as e:
        print("Sphinx error; {0}".format(e))


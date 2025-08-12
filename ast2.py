import win32com.client as wc
import speech_recognition as sr



def say(rrr):
    sp = wc.Dispatch("SAPI.SpVoice")
    sp.Speak(rrr)


def tc():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        aud = r.listen(source)
        try:
            query = r.recognize_google(aud, language="en-IN")
            print("You said:", query)
            return query
        except Exception as e:
            print(f"Error: {e}")
            return "Some error occurred"

d = "I am parrot"
if __name__ == "__main__":
    say(d)


    while True:
        rrr = tc()
        if rrr.lower() == "exit":
            print("Exiting...")
            break
        say(rrr)
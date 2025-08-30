import speech_recognition as sr
import pyttsx3
import os
import re

def speak(text):
    # Initialize TTS
    engine = pyttsx3.init()
    engine.setProperty('rate', 145)
    engine.setProperty('volume', 0.9)
    print("Response:", text)
    engine.stop()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source)
        try:
            query = recognizer.recognize_google(audio)
            return query
        except sr.UnknownValueError:
            return "Sorry, I couldn't understand that."
        except sr.RequestError:
            return "Speech service is currently unavailable."

# Start message
d = "hey Zishaanmalik"
speak(d)

# App launch paths or URLs
app_open = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "camera": "microsoft.windows.camera:",
    "windows store": "ms-windows-store:",
    "notepad":"notepad.exe",
    "music": "MediaPlayer.exe",
    "calculator": "calc.exe",
    "paint": "mspaint.exe",
    "command prompt":  "cmd.exe",
    "settings": "ms-settings:",
    "explorer": "explorer.exe",
    "wordpad": "wordpad.exe",
    "control panel": "control.exe"
}

app_close = {
    "google": "chrome.exe",
    "youtube": "chrome.exe",
    "camera":  "WindowsCamera.exe",
    "windows store":  "WinStore.App.exe",
    "notepad":  "notepad.exe",
    "music":  "Microsoft.Media.Player.exe",
    "calculator": "Calculator.exe",
    "paint":  "mspaint.exe",
    "command prompt":  "cmd.exe",
    "settings":  "SystemSettings.exe",
    "explorer":  "explorer.exe",
    "wordpad":  "wordpad.exe",
    "control panel":  "control.exe"
}


# Map app names to their task image names for termination
app_processes = {

}

while True:
    user_input = listen()
    print("You said:", user_input)

    # Exit condition
    if user_input.lower() == "exit":
        print("Exiting...")
        break

    # Check for open or close using regex
    command = re.search(r"\b(open|close)\b", user_input.lower())
    if command:
        action = command.group(1)  # 'open' or 'close'
        found = False

        for key in app_open:
            if key in user_input.lower():
                found = True
                if action == "open":
                    try:
                        os.startfile(app_open[key])
                        speak(f"Opening {key}")

                    except Exception as e:
                        speak(f"Cannot open {key}")
                        print(f"Error: {e}")

                elif action == "close" and key in app_close:
                    app = app_close[key]
                    result = os.system(f"taskkill.exe /f /im {app}")

                    if result == 0:
                        speak(f"Closed {key}")
                    else:
                        speak(f"Could not close {key}")
                break

        if not found:
            speak("App not recognized.")

    else:
        # Default fallback if no open/close detected
        speak("Please say open or close followed by the app name.")

    #print("Response:", user_input)


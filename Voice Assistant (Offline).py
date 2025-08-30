import pyttsx3
import os
import re
import whisper
import sounddevice as sd
import numpy as np

# Load Whisper model
model = whisper.load_model("base")  # You can change to "base", "small", "medium", or "large"

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 145)
    engine.setProperty('volume', 0.9)
    print("Response:", text)
    engine.stop()
    engine.say(text)
    engine.runAndWait()

def listen():
    duration = 5  # seconds
    samplerate = 16000

    print("Listening...")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
    sd.wait()

    audio = np.squeeze(audio)
    audio = whisper.pad_or_trim(audio)
    mel = whisper.log_mel_spectrogram(audio).to(model.device)
    result = model.decode(mel)
    return result.text.strip()

# Start message
d = "hey doctor knight"
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


while True:
    user_input = listen()
    print("You said:", user_input)

    if user_input.lower() == "exit":
        print("Exiting...")
        break

    command = re.search(r"\b(open|close)\b", user_input.lower())
    if command:
        action = command.group(1)
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
        speak("Please say open or close followed by the app name.")

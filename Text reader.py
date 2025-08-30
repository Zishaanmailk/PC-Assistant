import win32com.client as wc
# Initialize the speech engine
speaker = wc.Dispatch("SAPI.SpVoice")

# Infinite loop to take input and speak
while True:
    s = input("Enter text to speak (or 'exit' to quit): ")
    if s.lower() == 'exit':
  # Check if the input exactly matches 'exit'
        break
    speaker.Speak(s)
 # Speak the input text
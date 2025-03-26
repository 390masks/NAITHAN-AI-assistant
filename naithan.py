import speech_recognition as sr
import pyttsx3

# Tuned voice as per your wish
naithan = pyttsx3.init()
voices = naithan.getProperty('voices')
naithan.setProperty('voice', voices[0].id)
naithan.setProperty('rate', 130)  
naithan.setProperty('volume', 1.0)

# Speak function
def speak(text):
    naithan.say(text)
    naithan.runAndWait()

# Function to take voice as command
def take_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        speak("I'm listening, sir...")
        recognizer.adjust_for_ambient_noise(source, duration=1)  
        audio = recognizer.listen(source, timeout=5, phrase_time_limit=8) 
    try:
        command = recognizer.recognize_google(audio)
        return command.lower()
    except (sr.UnknownValueError, sr.RequestError):
        return ""  # No response if not recognized

# Function to process the command
def process_command(command):
    if "introduce yourself" in command or "naithan introduce yourself" in command or "introduce" in command:
        speak("Allow me to introduce myself.")
        speak("I am NAITHAN, a virtual artificial intelligence.")
        speak("I am here to assist you with a variety of tasks as best I can.")
    elif "how are you" in command:
        speak("I am always at your service, sir. How can I assist you today?")
    elif "exit" in command or "take rest naithan" in command or "take rest buddy" in command:
        speak("Goodbye sir. Have a great day!")
        exit()
    elif command != "":
        speak(f"You said: {command}")
    else:
        pass 

# Main loop
if __name__ == "__main__":
    speak("Hello sir how can i assist you ")
    while True:
        command = take_command()
        if command:
            process_command(command)

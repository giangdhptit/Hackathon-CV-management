import speech_recognition as sr

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)  # Reduce background noise
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)  # Use Google Speech API
        print("You said:", text)
    except sr.UnknownValueError:
        print("Sorry, could not understand the audio.")
    except sr.RequestError:
        print("Could not request results. Check your internet connection.")

recognize_speech_from_mic()

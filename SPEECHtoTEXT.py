import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.AudioFile("speech_orig.wav") as source:
    audio_data = recognizer.record(source)
    try:
        text = recognizer.recognize_google(audio_data, language="en-US")
        print("Recognized text:")
        print(text)
    except sr.UnknownValueError:
        print("Unable to recognize speech")
    except sr.RequestError as e:
        print(f"Speech recognition service error; {e}")

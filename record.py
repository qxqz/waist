import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say Something!!")
    audio = r.listen(source)

    try:
        transcript = r.recognize_google(audio, language="ko-KR")
        print("Google Speech Recognition thinks you said " + transcript)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service: {0}".format(e))
    
    
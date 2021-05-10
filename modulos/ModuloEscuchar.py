import speech_recognition as sr

def escuchar():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Speak Anything : ')
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio, language='es')
            print('You said: {}'.format(text))
            return text
        except:
            print('Sorry could not hear')


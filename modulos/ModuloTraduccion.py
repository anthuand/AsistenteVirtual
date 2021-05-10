#!/usr/bin/env python
#!/usr/bin/python
import pyttsx3
from googletrans import Translator



def traducir(text):
    translator=Translator()
    translation = translator.translate(text, dest='en')
    engine = pyttsx3.init()  # object creation
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(str(translation.text))
    engine.runAndWait()
    engine.stop()






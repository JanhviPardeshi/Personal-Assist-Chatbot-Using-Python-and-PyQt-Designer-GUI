import pyttsx3
import datetime

hour = int(datetime.datetime.now().hour)

strtime = datetime.datetime.now().strftime("%H hour  %M minutes  %S seconds")
print(hour)
print(strtime)

a = 20

print(f" the value is {a} " ,a)
# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# # print(voices[1].id)
# engine.setProperty('voices', voices[1].id)
# print(voices[1].id)

import pyjokes

# print(pyjokes.get_joke())

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1])
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# print(pyjokes.get_joke())
speak(pyjokes.get_joke('en','all'))
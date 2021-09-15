import pyttsx3
engine = pyttsx3.init()
engine.say("下午好！")
engine.runAndWait()
age = int(input())
if age <= 20:
    print("young!")
    engine.say("young!")
engine.runAndWait()

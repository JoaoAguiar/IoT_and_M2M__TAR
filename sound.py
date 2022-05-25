import pyttsx3


def sound_1(aux):

    engine = pyttsx3.init()
    if(aux>="25"):
        engine.say("Hot")
    elif(aux <="10"):
        engine.say("Cold")
    else:
        engine.say("Mild")

    engine.runAndWait()
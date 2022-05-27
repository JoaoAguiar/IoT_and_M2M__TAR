import pyttsx3

def sound_temperature(aux,topic):
    if(topic == "TEMPERATURE CELSIUS"):
        engine = pyttsx3.init()
        #print(aux)
        if(float(aux)>=25.0):
            engine.say("Hot")
        elif(float(aux) <=10.0):
            engine.say("Cold")
        else:
            engine.say("Mild")

        engine.runAndWait()
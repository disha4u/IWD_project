import win32com.client as wincl
import speech_recognition as sr
#import Error
r=sr.Recognizer()

def tts(q):
    speak = wincl.Dispatch("SAPI.SpVoice")
    speak.Speak(q)


def stt():
    try:
        
        with sr.Microphone() as source:
    
            audio=r.listen(source,5,10)
    except:
        print("err occured")
    return r.recognize_google(audio)
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import pyjokes
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning !!!!!!!!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon !!!!!!!!")

    else:
        speak("Good Evening !!!!!!!!")

    speak("I am Jarvis Sir, How may I help u")


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    '''
    It takes microphone input from the user and return string output
    '''

    r = sr.Recognizer() # It will help in recoginize the voice
    with sr.Microphone() as source:
        print("Listening..........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing.........")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)

    except Exception as e:
        print("Say that again..")
        return "None"

    return query

if __name__ == '__main__':
    WishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia.......')
            query = query.replace('wikipedia','')
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'play music' in query:
            speak("Here you go with music")
            music_dir = "D:\\Music\\"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query:
            speak("Good to hear that Sir.... How may I help you sir")

        elif 'what is your name' in query:
            speak('My Name is Jarvis Sir. But what had happen . U know my name very well')

        elif 'who made you' in query:
            speak('I am created by Aditya')



        elif 'open code' in query:
            speak('Here you go Sir')
            codepath = "C:\\Program Files\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)


        elif 'open slack' in query:
            codepath = "C:\\Slack\\SlackSetup.exe"
            os.startfile(codepath)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'quit' in query:
            speak('Ok Sir, ...... Take Care. Let me Know if u need any help')
            exit()



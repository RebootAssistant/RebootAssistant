import os
import requests
from pprint import pprint
from tkinter import *
import smtplib, ssl
import speech_recognition as sr
from PyDictionary import PyDictionary
from googlesearch import *
import webbrowser

i = 1

window = Tk()

window.title("Reboot")

lbl1 = Label(window, text="Reboot")
lbl1.pack()
lbl2 = Label(window, text="User")
lbl2.pack()

def command():

    r = sr.Recognizer()
    import win32com.client as wincl
    speak = wincl.Dispatch("SAPI.SpVoice")

    configDoc = open("config.txt","r")
    configLines = configDoc.readlines()
    nameText = configLines[0]
    nameAudio = configLines[1]
    email = configLines[3]
    emailPassword = configLines[4]
    city_name = configLines[2]

    WTString = ''

    nameAudio.replace('\n',' ')

    dictionary=PyDictionary()

    welcomeText = "Welcome back ",nameText,". What would you like me to do?"
    WTString = WTString.join(welcomeText)
    lbl1.configure(text=WTString.replace('\n',''))
    welcomeAudio = "Welcome back ",nameAudio,". What would you like me to do?"
    speak.Speak(welcomeAudio)
    window.update()
    print(WTString.replace('\n',''))
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        commandAudio = r.listen(source)

    welcomeCommand = r.recognize_google(commandAudio)
    print(welcomeCommand)
    lbl2.configure(text=welcomeCommand)
    window.update()

    UIText2 = welcomeCommand
        
    if 'weather' in welcomeCommand:
        API_key = "c6269ea0f84111e5cc382078107f1a83"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        Final_url = base_url + "appid=" + API_key + "&q=" + city_name
        weather_data = requests.get(Final_url).json()
        temp = weather_data['main']['temp']
        temp -= 273.15
        temp1 = int(temp)
        tempAudio = 'The temperature in '+ city_name +' right now is ' + str(temp1) + ' degrees Celsius.'
        print(tempAudio)
        speak.Speak(tempAudio)
        lbl1.configure(text=tempAudio)
        window.update()
        UIText1 = tempAudio
    elif 'email' in welcomeCommand:
        port = 465
        context = ssl.create_default_context()

        speak.Speak("What do you want your message to be?")
        print("What do you want your message to be?")
        UIText1 = "What do you want your message to be?"
        lbl1.configure(text=UIText1)
        window.update()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            messageAudio = r.listen(source)

        message = r.recognize_google(messageAudio)
        print(message)

        lbl2.configure(text=message)
        window.update()

        UIText2 = message
            
        speak.Speak("Who is receiving the email?")
        print("Who is receiving the email?")
        UIText1 = "Who is receiving the email?"
        lbl1.configure(UIText1)
        window.update()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            emailAudio = r.listen(source)

        receivingEmail = r.recognize_google(emailAudio)
        receivingEmail = ''.join(receivingEmail.split())
        if "at" in receivingEmail:
            receivingEmail = receivingEmail.replace("at", "@")

        print(receivingEmail)
        UIText2 = receivingEmail
        lbl2.configure(text=receivingEmail)
        window.update()
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(email, emailPassword)
            server.sendmail(email, receivingEmail, message + " Sent from Reboot, a virtual assistant made for PC.")
            messageAudio = 'Message sent.'
            speak.Speak(messageAudio)
            print(messageAudio)
            UIText1 = messageAudio
            lbl1.configure(text=messageAudio)
    elif 'create' and 'text' in welcomeCommand:
        speak.Speak("What is the name of the text file?")
        print("What is the name of the text file?")
        lbl1.configure(text="What is the name of the text file?")
        window.update()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            dNameAudio = r.listen(source)

        docName = r.recognize_google(dNameAudio)
        print(docName)
        lbl2.configure(text=docName)
        window.update()

        doc = open(docName + ".txt", "w+")
        doc.close()
        speak.Speak("Document created.")
        print("Document created.")
        lbl1.configure(text="Document created.")
        window.update()

        speak.Speak("What would you like to write in it?")
        print("What would you like to write in it?")
        lbl1.configure(text="What would you like to write in it?")
        window.update()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            dTextAudio = r.listen(source)

        docText = r.recognize_google(dTextAudio)
        print(docText)
        lbl2.configure(text=docText)
        window.update()

        doc = open(docName + ".txt", "w")
        doc.write(docText)
        doc.close()
    elif 'who' and 'you' in welcomeCommand:
        print("My name is Reboot. I am a new virtual assistant for your PC. The problem with PC virtual assistants, are that they lack in features and are not easy to use. This then drives us away from using them. Think about it - when was the last time you used Siri on your Mac, or Cortana on your Windows PC? Reboot solves these issues. So far I am only in early beta stages, however, I will get new features when my creator can make them, and I am also open source, meaning that people can edit my code and make custom features for their needs. To summarise, I am called Reboot, as I am rebooting the virtual assistant, on your PC.")
        lbl1.configure(text="My name is Reboot. I am a new virtual assistant for your PC. The problem with PC virtual assistants, are that they lack in features and are not easy to use. This then drives us away from using them. Think about it - when was the last time you used Siri on your Mac, or Cortana on your Windows PC? Reboot solves these issues. So far I am only in early beta stages, however, I will get new features when my creator can make them, and I am also open source, meaning that people can edit my code and make custom features for their needs. To summarise, I am called Reboot, as I am rebooting the virtual assistant, on your PC.")
        window.update()
        speak.Speak("My name is Reboot. I am a new virtual assistant for your PC. The problem with PC virtual assistants, are that they lack in features and are not easy to use. This then drives us away from using them. Think about it - when was the last time you used Siri on your Mac, or Cortana on your Windows PC? Reboot solves these issues. So far I am only in early beta stages, however, I will get new features when my creator can make them, and I am also open source, meaning that people can edit my code and make custom features for their needs. To summarise, I am called Reboot, as I am rebooting the virtual assistant, on your PC.")
    elif 'dictionary' in welcomeCommand:
        print("What would you like to know the meaning of?")
        speak.Speak("What would you like to know the meaning of?")
        lbl1.configure(text="What would you like to know the meaning of?")
        window.update()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            wordAudio = r.listen(source)

        word = r.recognize_google(wordAudio)
        print(word)
        lbl2.configure(text=word)
        wordMeaning = dictionary.meaning(word)
        print(wordMeaning)
        lbl1.configure(text=wordMeaning)
        window.update()
        speak.Speak(wordMeaning)
    elif 'search' in welcomeCommand:
        print("What would you like to search?")
        lbl1.configure(text="What would you like to search?")
        window.update()
        speak.Speak("What would you like to search?")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            searchqueryAudio = r.listen(source)

        searchquery = r.recognize_google(searchqueryAudio)
        lbl2.configure(text=searchquery)
        window.update()

        webbrowser.open_new("https://google.com/search?q=%s" % searchquery)

btn = Button(window, text="Start Command", command=command)
btn.pack()



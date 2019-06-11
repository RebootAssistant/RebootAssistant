import os
import requests
from pprint import pprint
import smtplib, ssl
import speech_recognition as sr

r = sr.Recognizer()
import win32com.client as wincl
speak = wincl.Dispatch("SAPI.SpVoice")
i = 1

configDoc = open("config.txt","r")
configLines = configDoc.readlines()
nameText = configLines[0]
nameAudio = configLines[1]
email = configLines[3]
emailPassword = configLines[4]
city_name = configLines[2]

#welcome text
while i == 1:
    welcomeText = "Welcome back ",nameText,". What would you like me to do?"
    welcomeAudio = "Welcome back ",nameAudio,". What would you like me to do?"
    speak.Speak(welcomeAudio)
    print(welcomeText)
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        commandAudio = r.listen(source)

    welcomeCommand = r.recognize_google(commandAudio)
    print(welcomeCommand)



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

    elif 'email' in welcomeCommand:
        port = 465
        context = ssl.create_default_context()

        speak.Speak("What do you want your message to be?")
        print("What do you want your message to be?")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            messageAudio = r.listen(source)

        message = r.recognize_google(messageAudio)
        print(message)
        
        speak.Speak("Who is receiving the email?")
        print("Who is receiving the email?")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            emailAudio = r.listen(source)

        receivingEmail = r.recognize_google(emailAudio)
        receivingEmail = ''.join(receivingEmail.split())
        if "at" in receivingEmail:
            receivingEmail = receivingEmail.replace("at", "@")

        print(receivingEmail)
        with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
            server.login(email, emailPassword)
            server.sendmail(email, receivingEmail, message + " Sent from Reboot, a virtual assistant made for PC.")
        messageAudio = 'Message sent.'
        speak.Speak(messageAudio)
        print(messageAudio)

    elif 'create' and 'text' in welcomeCommand:
        speak.Speak("What is the name of the text file?")
        print("What is the name of the text file?")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            dNameAudio = r.listen(source)

        docName = r.recognize_google(dNameAudio)
        print(docName)

        doc = open(docName + ".txt", "w+")
        doc.close()
        speak.Speak("Document created.")
        print("Document created.")

        speak.Speak("What would you like to write in it?")
        print("What would you like to write in it?")
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            dTextAudio = r.listen(source)

        docText = r.recognize_google(dTextAudio)
        print(docText)

        doc = open(docName + ".txt", "w")
        doc.write(docText)
        doc.close()

    elif 'who' and 'you' in welcomeCommand:
        print("My name is Reboot. I am a new virtual assistant for your PC. The problem with PC virtual assistants, are that they lack in features and are not easy to use. This then drives us away from using them. Think about it - when was the last time you used Siri on your Mac, or Cortana on your Windows PC? Reboot solves these issues. So far I can only do three things: send emails, tell you the weather and create text files. However, I will get new features when my creator can make them, and I am also open source, meaning that people can edit my code and make custom features for their needs. To summarise, I am called Reboot, as I am rebooting the virtual assistant, on your PC.")
        speak.Speak("My name is Reboot. I am a new virtual assistant for your PC. The problem with PC virtual assistants, are that they lack in features and are not easy to use. This then drives us away from using them. Think about it - when was the last time you used Siri on your Mac, or Cortana on your Windows PC? Reboot solves these issues. So far I can only do three things: send emails, tell you the weather and create text files. However, I will get new features when my creator can make them, and I am also open source, meaning that people can edit my code and make custom features for their needs. To summarise, I am called Reboot, as I am rebooting the virtual assistant, on your PC.")

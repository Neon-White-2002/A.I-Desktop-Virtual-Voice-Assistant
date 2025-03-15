# A.I. VIRTUAL ASSISTANT (JARVIS)

import pyttsx3
import requests
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from requests import get
import pywhatkit as kit
import sys
import time
import psutil
import pygame.mixer
from googlesearch import search

# BY USING 'PYTTSX3' WE HAVE SET A VOICE TO OUR PROGRAM.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


# SPEAK FUNCTION HELP TO SPEAK OUR 'JENNIFER'
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# THIS FUNCTION WISH ME WHEN WE START THE PROGRAM EXECUTION.
def wishMe():
    current_hour = int(datetime.datetime.now().hour)
    if 0 <= current_hour < 12:
        print("Good Morning Sir ! \n")
        speak("Good Morning Sir !")

    elif 12 <= current_hour < 17:
        print("Good Afternoon Sir ! \n")
        speak("Good Afternoon Sir !")

    else:
        print("Good Evening Sir ! \n")
        speak("Good Evening Sir !")

    print("Hello Sir, How may I help You ? \n")
    speak("Hello Sir, How may I help you ?")


# THIS FUNCTION HELP THE USER TO SAY AND ENGINE WILL UNDERSTAND IT
def takeCommand():
    # IT TAKES INPUT FROM MICROPHONE FROM THE USER AND RETURN STRING OUTPUT.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening Sir... ")
        speak("Listening Sir !")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing Sir...")
        query = r.recognize_google(audio, language='en-in')
        print(f"Sir Said: {query} \n")

    except Exception as e:
        print(e)
        print("Say that again please sir... \n")
        speak("Sorry Sir, can you say it again please...!")
        return "None"
    return query


# THIS FUNCTION HELP THE USER TO USER SEND E-MAIL
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gamil.com', 587)
    server.ehlo()
    server.starttls()
    server.login('USER EMAIL ADDRESS', 'USER PASSWORD')
    server.sendmail('USER EMAIL', to, content)
    server.close()


# THIS FUNCTION CHECK EVENT OR SPECIAL ANYTHING
def Event():
    date = datetime.datetime.now().strftime("%d/%m")
    print("Wait Sir, Let me Check...! \n")
    speak("Wait Sir, Let me Check...!")
    hours = time.strftime("%H")
    hour = int(hours)
    minute = time.strftime("%M")
    min = int(minute) + 2

    if date == '11/02':
        print("Sir ! Today is Marriage Anniversary of your Mummy & Daddy !")
        speak("Sir ! Today is Marriage Anniversary of your Mummy & Daddy !")

        print("Sir ! Wishing them please wait.")
        speak("Sir ! Wishing them please wait.")

        kit.sendwhatmsg("+919028259775",
                        f"Wishing a perfect pair a perfectly happy day. \n HAPPY MARRIAGE ANNIVERSARY MUMMY!", hour,
                        min)
        kit.sendwhatmsg("+919820740326",
                        f"Wishing a perfect pair a perfectly happy day. \n HAPPY MARRIAGE ANNIVERSARY DADDY!", hour,
                        min)
        print("Sir ! Message has been sent to Mummy & Daddy.")
        speak("Sir ! Message has been sent to Mummy & Daddy.")

        print("Sir, now what should I do for you?")
        speak("Sir, now what should I do for you?")


    elif date == '07/05':
        print("Sir ! Today is your Brother Birthday Sir !")
        speak("Sir ! Today is your Brother Birthday Sir !")


    elif date == '16/06':
        print("Sir ! Today is your Mummy's Birthday !")
        speak("Sir ! Today is your Mummy's Birthday !")

        print("Sir ! Wishing to Mom please wait.")
        speak("Sir ! Wishing to Mom please wait.")

        kit.sendwhatmsg("+919028259775",
                        f"Thank you for always comforting me when I was sad and making me laugh whenever I cried... \n HAPPY BIRTHDAY MUMMY LOVE YOU SO MUCH.!",
                        hour, min)
        print("Sir ! Message has been sent to Mummy.")
        speak("Sir ! Message has been sent to Mummy.")

        print("Sir, now what should I do for you?")
        speak("Sir, now what should I do for you?")


    elif date == '13/09':
        print("Sir ! Today is Your Birthday Sir !")
        speak("Sir ! Today is your Birthday Sir !")

        print("Many Many Happy Returns of the day Sir !")
        speak("Many Many Happy Returns of the day Sir !")

        kit.sendwhatmsg("+919137868099",
                        f"The day has come again for me to say a wish, and I wish myself success and everlasting happiness as I celebrate a birthday full of joy today. I am very thankful and grateful to the Almighty for granting me yet another year. I pray for an abundance of grace in my world.",
                        hour, min)
        print("Sir, now what should I do for you?")
        speak("Sir, now what should I do for you?")

    elif date == '11/12':
        print("Sir ! Today is your your Daddy Birthday.")
        speak("Sir ! Today is your your Daddy Birthday.")

        print("Sir ! Wishing to Daddy please wait.")
        speak("Sir ! Wishing to Daddy please wait.")

        kit.sendwhatmsg("+919820740326",
                        f"Happy birthday! Daddy, you've given me so many invaluable things in life and I will always be grateful for them. May your special day bring you plenty of wonderful surprises! I am lucky that I was given the best father in the world, a father who truly loves me with all of his heart.",
                        hour, min)
        print("Sir ! Message has been sent to Daddy.")
        speak("Sir ! Message has been sent to Daddy.")

        print("Sir, now what should I do for you?")
        speak("Sir, now what should I do for you?")

    else:
        print("No Sir ! Nothing Special today or any Event.")
        speak("No Sir ! Nothing Special today or any Event.")
        print("Sir, now what should I do for you?")
        speak("Sir, now what should I do for you?")


# THIS FUNCTION CHECK THAT ANY SPECIAL OR ANY EVENT IS THERE TODAY OR NOT WHEN THE PROGRAM IT RUN
def checkEvent():
    date = datetime.datetime.now().strftime("%d/%m")

    hours = time.strftime("%H")
    hour = int(hours)
    minute = time.strftime("%M")
    min = int(minute) + 2

    if date == '11/02':
        print("Ohh ! Sir Today is something special...")
        speak("Ohh ! Sir Today is something special...")

        print("Sir ! Today is Marriage Anniversary of your Mummy & Daddy !")
        speak("Sir ! Today is Marriage Anniversary of your Mummy & Daddy !")

        print("Sir ! Wishing them please wait.")
        speak("Sir ! Wishing them please wait.")

        kit.sendwhatmsg("+919028259775",
                        f"Wishing a perfect pair a perfectly happy day. \n HAPPY MARRIAGE ANNIVERSARY MUMMY!", hour,
                        min)
        kit.sendwhatmsg("+919820740326",
                        f"Wishing a perfect pair a perfectly happy day. \n HAPPY MARRIAGE ANNIVERSARY DADDY!", hour,
                        min)
        print("Sir ! Message has been sent to Mummy & Daddy.")
        speak("Sir ! Message has been sent to Mummy & Daddy.")

        print("Sir, now what should I do for you?")
        speak("Sir, now what should I do for you?")


    elif date == '07/05':
        print("Ohh ! Sir Today is something special...")
        speak("Ohh ! Sir Today is something special...")

        print("Sir ! Today is Birthday of your Brother !")
        speak("Sir ! Today is Birthday of your Brother !")


    elif date == '16/06':
        print("Ohh ! Sir Today is something special...")
        speak("Ohh ! Sir Today is something special...")

        print("Sir ! Today is your Mummy's Birthday !")
        speak("Sir ! Today is your Mummy's Birthday !")

        print("Sir ! Wishing to Mom please wait.")
        speak("Sir ! Wishing to Mom please wait.")

        kit.sendwhatmsg("+919028259775",
                        f"Thank you for always comforting me when I was sad and making me laugh whenever I cried... \n HAPPY BIRTHDAY MUMMY LOVE YOU SO MUCH.!",
                        hour, min)
        print("Sir ! Message has been sent to Mummy.")
        speak("Sir ! Message has been sent to Mummy.")

        print("Sir, now what should I do for you?")
        speak("Sir, now what should I do for you?")


    elif date == '13/09':
        print("Ohh ! Sir Today is something special...")
        speak("Ohh ! Sir Today is something special...")

        print("Sir ! Today is Your Birthday Sir !")
        speak("Sir ! Today is your Birthday Sir !")

        print("Many Many Happy Returns of the day Sir !")
        speak("Many Many Happy Returns of the day Sir !")

        kit.sendwhatmsg("+919137868099",
                        f"The day has come again for me to say a wish, and I wish myself success and everlasting happiness as I celebrate a birthday full of joy today. I am very thankful and grateful to the Almighty for granting me yet another year. I pray for an abundance of grace in my world.",
                        hour, min)
        print("Sir, now what should I do for you?")
        speak("Sir, now what should I do for you?")

    elif date == '11/12':
        print("Ohh ! Sir Today is something special...")
        speak("Ohh ! Sir Today is something special...")

        print("Sir ! Today is your your Daddy Birthday.")
        speak("Sir ! Today is your your Daddy Birthday.")

        print("Sir ! Wishing to Daddy please wait.")
        speak("Sir ! Wishing to Daddy please wait.")

        kit.sendwhatmsg("+919820740326",
                        f"Happy birthday! Daddy, you've given me so many invaluable things in life and I will always be grateful for them. May your special day bring you plenty of wonderful surprises! I am lucky that I was given the best father in the world, a father who truly loves me with all of his heart.",
                        hour, min)
        print("Sir ! Message has been sent to Daddy.")
        speak("Sir ! Message has been sent to Daddy.")

        print("Sir, now what should I do for you?")
        speak("Sir, now what should I do for you?")


# THIS FUNCTION HELP THE USER TO SEE THE VARIOUS NEWS
def News():
    print("Alright Sir ! \n")
    speak("Alright Sir !")

    print("Sir, Which of the following News you want to see?")
    speak("Sir, Which of the following News you want to see?")

    print(" \n ZEE NEWS. \n AAJ TAK. \n DNA NEWS. \n CNBC NEWS. \n NDTV NEWS. \n ABP NEWS. \n BBC NEWS")
    speak("And, Sir any other News you want to see you, I will help it out !")

    run = True

    while run:

        ncmd = takeCommand().lower()

        if 'zee' in ncmd:
            print("Ok Sir ! Opening Zee News Page.")
            speak("Ok Sir ! Opening Zee News Page.")
            webbrowser.open("https://zeenews.india.com/")
            print("Sir, any other news you want to see tell me?")
            speak("Sir, any other news you want to see tell me?")

        elif 'aaj tak' in ncmd:
            print("Ok Sir ! Opening Aaj Tak News Page.")
            speak("Ok Sir ! Opening Aaj Tak News Page.")
            webbrowser.open("https://www.aajtak.in/")
            print("Sir, any other news you want to see tell me?")
            speak("Sir, any other news you want to see tell me?")

        elif 'dna' in ncmd:
            print("Ok Sir ! Opening DNA News.")
            speak("Ok Sir ! Opening DNA News.")
            webbrowser.open("https://www.dnaindia.com/")
            print("Sir, any other news you want to see tell me?")
            speak("Sir, any other news you want to see tell me?")

        elif 'cnbc' in ncmd:
            print("Ok Sir ! Opening CNBC News.")
            speak("Ok Sir ! Opening CNBC News.")
            webbrowser.open("https://www.cnbc.com/world/?region=world")
            print("Sir, any other news you want to see tell me?")
            speak("Sir, any other news you want to see tell me?")

        elif 'ndtv' in ncmd:
            print("Ok Sir ! Opening NDTV News.")
            print("Ok Sir ! Opening NDTV News.")
            webbrowser.open("https://www.ndtv.com/")
            print("Sir, any other news you want to see tell me?")
            speak("Sir, any other news you want to see tell me?")

        elif 'abp' in ncmd:
            print("Ok Sir ! Opening ABP News.")
            speak("Ok Sir ! Opening ABP News.")
            webbrowser.open("https://www.abplive.com/")
            print("Sir, any other news you want to see tell me?")
            speak("Sir, any other news you want to see tell me?")

        elif 'bbc' in ncmd:
            print("Ok Sir ! Opening BBC News.")
            speak("Ok Sir ! Opening BBC News.")
            webbrowser.open("https://www.bbc.com/news")
            print("Sir, any other news you want to see tell me?")
            speak("Sir, any other news you want to see tell me?")


        elif 'no' in ncmd:
            print("Alright Sir has you say.")
            speak("Alright Sir has you say.")
            run = False
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")


        elif 'dont' in ncmd:
            print("Alright Sir has you say.")
            speak("Alright Sir has you say.")
            run = False
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'wait' in ncmd:
            print("Alright Sir.")
            speak("Alright Sir.")

        else:
            print("Alright Sir !")
            speak("Alright Sir !")
            webbrowser.open(f"{ncmd}")
            print(f"Opening {ncmd}")
            speak(f"Opening {ncmd}")
            print("Sir, any other news you want to see tell me?")
            speak("Sir, any other news you want to see tell me?")


# THIS FUNCTION HELP USER TO SEE STOCK MARKET NEW'S:
def stockMarket():
    print("Alright Sir. \n")
    speak("Alright Sir.")

    print("Sir, which of the following you want to see?")
    speak("Sir, which of the following you want to see?")

    print(
        "\n NSE (National Stock Exchange) \n BSE (Bombay Stock Exchange) \n NYSE (New York Stock Exchange) \n Zee Business Market \n MCSM (Money Control Stock Market)")
    speak("And, Sir any other Stock Market News you want to see you, I will help it out !")

    run = True

    while run:
        smcmd = takeCommand().lower()

        if 'nse' in smcmd:
            print("Ok Sir ! Opening NSE (National Stock Exchange) News.")
            speak("Ok Sir ! Opening NSE (National Stock Exchange) News.")
            webbrowser.open("https://www.nseindia.com/")
            print("Sir, any other stock market news you want see tell me?")
            speak("Sir, any other stock market news you want see tell me?")

        elif 'national stock exchange' in smcmd:
            print("Ok Sir ! Opening NSE (National Stock Exchange) News.")
            speak("Ok Sir ! Opening NSE (National Stock Exchange) News.")
            webbrowser.open("https://www.nseindia.com/")
            print("Sir, any other stock market news you want see tell me?")
            speak("Sir, any other stock market news you want see tell me?")


        elif 'bse' in smcmd:
            print("Ok Sir ! Opening BSE (Bombay Stock Exchange) News.")
            speak("Ok Sir ! Opening BSE (Bombay Stock Exchange) News.")
            webbrowser.open("https://www.bseindia.com/")
            print("Sir, any other stock market news you want see tell me?")
            speak("Sir, any other stock market news you want see tell me?")

        elif 'bombay stock exchange' in smcmd:
            print("Ok Sir ! Opening BSE (Bombay Stock Exchange) News.")
            speak("Ok Sir ! Opening BSE (Bombay Stock Exchange) News.")
            webbrowser.open("https://www.bseindia.com/")
            print("Sir, any other stock market news you want see tell me?")
            speak("Sir, any other stock market news you want see tell me?")

        elif 'nysc' in smcmd:
            print("Ok Sir ! Opening NYSE (New York Stock Exchange) News.")
            speak("Ok Sir ! Opening NYSE (New York Stock Exchange) News.")
            webbrowser.open("https://www.nyse.com/index")
            print("Sir, any other stock market news you want see tell me?")
            speak("Sir, any other stock market news you want see tell me?")

        elif 'new york stock exchange' in smcmd:
            print("Ok Sir ! Opening NYSE (New York Stock Exchange) News.")
            speak("Ok Sir ! Opening NYSE (New York Stock Exchange) News.")
            webbrowser.open("https://www.nyse.com/index")
            print("Sir, any other stock market news you want see tell me?")
            speak("Sir, any other stock market news you want see tell me?")


        elif 'zee business' in smcmd:
            print("Ok Sir ! Opening Zee Business Market News.")
            speak("Ok Sir ! Opening Zee Business Market News.")
            webbrowser.open("https://www.zeebiz.com/markets")
            print("Sir, any other stock market news you want see tell me?")
            speak("Sir, any other stock market news you want see tell me?")

        elif 'mcsm' in smcmd:
            print("Ok Sir ! Opening Money Control Stock Market News.")
            speak("Ok Sir ! Opening Money Control Stock Market News.")
            webbrowser.open("https://www.moneycontrol.com/stocksmarketsindia/")
            print("Sir, any other stock market news you want see tell me?")
            speak("Sir, any other stock market news you want see tell me?")

        elif 'money control stock market' in smcmd:
            print("Ok Sir ! Opening Money Control Stock Market News.")
            speak("Ok Sir ! Opening Money Control Stock Market News.")
            webbrowser.open("https://www.moneycontrol.com/stocksmarketsindia/")
            print("Sir, any other stock market news you want see tell me?")
            speak("Sir, any other stock market news you want see tell me?")

        elif 'no' in smcmd:
            print("Alright Sir, has you say.")
            speak("Alright Sir, has you say.")
            run = False
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")


        elif 'dont' in smcmd:
            print("Alright Sir, has you say.")
            speak("Alright Sir, has you say.")
            run = False
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'wait' in smcmd:
            print("Alright Sir.")
            speak("Alright Sir.")

        else:
            print("Alright Sir ! \n")
            speak("Alright Sir !")
            webbrowser.open(f"{smcmd}")
            print("Sir, any other stock market news you want see tell me?")
            speak("Sir, any other stock market news you want see tell me?")


# THIS FUNCTION HELP THE USER TO SEND MESSAGE ON WHATSAPP
def sendMessage():
    speak("Sir your Contact is been displayed.")
    contacts = ["Mom", "Dad", "Me"]
    numbers = ["+919028259775", "+919820740326", "+919137868099"]
    print("Sir Yours Contact List: -")
    for x in contacts:
        print(x)

    hours = time.strftime("%H")
    hours: int = int(hours)
    minute = time.strftime("%M")
    min = int(minute) + 2
    print("Sir to whom I send message ?")
    speak("Sir ! to whom I send Message ?")

    run = True
    while run:
        user = takeCommand()

        if 'Mom' in user:
            print("Alright Sir, What message I should send ?")
            speak("Alright Sir, What message I should send ?")

            msg = takeCommand()
            print("Sir ! Please wait till the message has sent !")
            speak("Sir ! Please wait till the message has sent !")
            kit.sendwhatmsg(numbers[0], f"{msg}", hours, min)
            print(f"Sir ! Message as been send to {user} \n")
            speak(f"Sir ! Message as been send to {user}")
            print("Sir, now to whom you want to send message?")
            speak("Sir, now to whom you want to send message?")

        elif 'Dad' in user:
            print("Alright Sir, What message I should send ?")
            speak("Alright Sir, What message I should send ?")

            msg = takeCommand()
            print("Sir ! Please wait till the message has sent !")
            speak("Sir ! Please wait till the message has sent !")
            kit.sendwhatmsg(numbers[1], f"{msg}", hours, min)
            print(f"Sir ! Message has been to {user} \n")
            speak(f"Sir ! Message has been to {user}")
            print("Sir, now to whom you want to send message?")
            speak("Sir, now to whom you want to send message?")

        elif 'Me' in user:
            print("Alright Sir, What message I should send ?")
            speak("Alright Sir, What message I should send ?")

            msg = takeCommand()
            print("Sir ! Please wait till the message has sent !")
            speak("Sir ! Please wait till the message has sent !")
            kit.sendwhatmsg(numbers[2], f"{msg}", hours, min)
            print(f"Sir ! Message has been to {user} \n")
            speak(f"Sir ! Message has been to {user} \n")
            print("Sir, now to whom you want to send message?")
            speak("Sir, now to whom you want to send message?")

        elif 'stop' in user:
            run = False
            print("Alright Sir !")
            speak("Alright Sir !")
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'dont' in user:
            run = False
            print("Alright Sir, has you say.")
            speak("Alright Sir, has you say.")
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'no' in user:
            run = False
            print("Alright Sir !")
            speak("Alright Sir !")
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'wait' in user:
            print("Alright Sir.")
            speak("Alright Sir.")


# THIS FUNCTION HELP THE USER TO FIND IT'S CURRENT LOCATION.
def location():
    print("Alright Sir, let me check.")
    speak("Alright Sir, let me check.")
    res = requests.get('http://ipinfo.io/')
    data = res.json()

    city = data['city']
    region = data['region']

    user_location = data['loc'].split(',')
    latitude = user_location[0]
    longitude = user_location[1]

    print(f"City : {city} \n")
    speak(f"Sir City is: {city}")

    print(f"Region : {region} \n")
    speak(f"Region is : {region} \n")

    print(f"Latitude : {latitude} \n")
    speak(f"Latitude is : {latitude} \n")

    print(f"Longitude : {longitude} \n")
    speak(f"Longitude is : {longitude} \n")

    print("Sir, now what can I do for you? \n")
    speak("Sir, now what can I do for you?")


# THIS FUNCTION HELP USER TO TYPE ON NOTEPAD.
def Notepad():
    print("Sir What Should I Type on Notepad.")
    speak("What Should I type Sir?")
    file = open(r"D:\\PYTHON Programming\\A.I Desktop Virtual Voice Assistance\\NOTEPAD DATA\\EXAMPLE.txt", "w+")
    run = True

    while run:
        user_command = takeCommand()
        file.write(f"{user_command} \n")

        if 'close' in user_command:
            file.close()
            run = False
            print("Alright Sir ! I am closing Notepad.")
            speak("Alright Sir ! I am closing Notepad Typing Work.")
            speak("Sir, now you can check your typing work.")
            speak("Now how may I help you ?")

        elif 'stop' in user_command:
            file.close()
            run = False
            print("Alright Sir ! I am closing Notepad.")
            speak("Alright Sir ! I am closing Notepad Typing Work.")
            speak("Sir, now you can check your typing work.")
            speak("Now how may I help you ?")

        elif 'wait' in user_command:
            print("Alright Sir.")
            speak("Alright Sir.")

        print("Done Sir, now ?")
        speak("Done Sir, now ?")

    os.startfile("D:\\PYTHON Programming\\A.I Desktop Virtual Voice Assistance\\NOTEPAD DATA\\EXAMPLE.txt")


# THIS FUNCTION HELP TO CHECK BATTERY AND ALERT TO USER.
def CheckBattery():
    battery = psutil.sensors_battery()
    percent = str(battery.percent)

    if percent <= '20':
        print(f"Sir your Battery Power is running slow, may I suggest you to charge it soon.")
        speak(f"Sir your Battery Power is running slow, may I suggest you to charge it soon.")


# THIS FUNCTION WILL TO CHECK THE WEATHER OF ANY CITY.
def CheckWeather():
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    print("Sir, of which city you want to find weather ?")
    speak("Sir, of which city you want to find weather ?")
    CITY = takeCommand()
    API_KEY = "576b39c9be8cede3a8038ec4f341d678"

    URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY
    response = requests.get(URL)

    if response.status_code == 200:
        # GETTING THE DATA IN 'JSON' FORMATE.
        data = response.json()

        # GETTING THE 'MAIN' DICT BLOCK.
        main = data['main']

        # GETTING TEMPERATURE.
        temperature = main['temp']

        # GETTING THE HUMIDITY.
        humidity = main['humidity']

        # GETTING THE PRESSURE.
        pressure = main['pressure']

        # WEATHER REPORT.
        report = data['weather']

        k = int(temperature)
        c = round(k - 273.15)
        C = str(c)

        print(f" \n City Name : {CITY}")
        speak(f"City Name is {CITY}")

        print(f"\n Temperature : {C + '°C'}")
        speak(f"Temperature is {C + '°C'}")

        print(f"\n Humidity : {humidity}")
        speak(f"Humidity is {humidity}")

        print(f"\n Pressure : {pressure}")
        speak(f"Pressure is {pressure}")

        print(f"\n Weather Report: {report[0]['description']} \n")
        speak(f"Weather Report is {report[0]['description']}")

        print("Now, how may I help you sir? \n")
        speak("Now, how may I help you sir?")
    else:
        print("\n Sorry Sir, I can't find the city.")
        speak("Sorry Sir, I can't find the city.")


if __name__ == "__main__":
    pygame.mixer.init()
    pygame.mixer.music.load("D:\\PYTHON Programming\\A.I Desktop Virtual Voice Assistance\\SOUNDS\\Assistant.mp3")
    pygame.mixer.music.play()
    time.sleep(10)
    pygame.mixer.music.stop()

    print("\n")
    print("Welcome to A.I Virtual Command World...!")
    wishMe()
    CheckBattery()
    checkEvent()

    while True:
        query = takeCommand().lower()

        # LOGIC FOR EXECUTING TASKS BASED ON QUERY...!

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=5)
            speak("According to Wikipedia,")
            print(result)
            speak(result)
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'open youtube' in query:
            speak("Opening YouTube Sir !")
            webbrowser.open("https://www.youtube.com/")
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'open google' in query:
            speak("Opening Google Sir !")
            webbrowser.open("https://www.google.com/")
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'open brave' in query:
            speak("Opening, Brave Web-Browser Sir !")
            webbrowser.open("https://www.brave.com/")
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'open amazon' in query:
            speak("Opening Amazon Website !")
            webbrowser.open("https://www.amazon.in/")
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'open flipkart' in query:
            speak("Opening Flipkart Website !")
            webbrowser.open("https://www.flipkart.com/")
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'play music' in query:
            speak("Playing Music Sir...!")
            music_dir = 'D:\\PYTHON Programming\\A.I Desktop Virtual Voice Assistance\\MUSIC'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M:%p")
            print(strTime)
            speak(f"Sir, the Time is: {strTime}")
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'date' in query:
            date = datetime.datetime.now().date()
            print(date)
            speak(f"Sir, The Date is: {date}")
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        # elif 'open visual studio code' in query:
        #     speak("Opening Visual Studio Code Sir !")
        #     codePath = "C:\\Users\\Neeku\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        #     os.startfile(codePath)
        #     print("Sir, now what should I do for you?")
        #     speak("Sir, now what should I do for you?")

        # elif 'git bash' in query:
        #     print("Opening Git Bash Sir !")
        #     speak("Opening Git Bash Sir !")
        #     gitbash = "C:\\Program Files\\Git\\git-bash.exe"
        #     os.startfile(gitbash)
        #     print("Sir, now what should I do for you ?")
        #     speak("Sir, now what should I do for you ?")


        elif 'email to nikunj' in query:
            try:
                speak("What Should I Say Sir?")
                print("What Should I Say Sir?")
                content = takeCommand()
                to = "USER EMAIL ADDRESS"
                sendEmail(to, content)
                speak("Email has been Sent !")
                print("Sir, now what should I do for you?")
                speak("Sir, now what should I do for you?")

            except Exception as e:
                print(e)
                speak("Sorry! Sir I was not able to sent this email")

        elif 'who are you' in query:
            print(
                "Let me introduce my self, I am Jennifer an AI Virtual Assistant or AI Desktop Virtual Voice Assistant.")
            speak(
                "Let me introduce my self, I am Jennifer an AI Virtual Assistant or AI Desktop Virtual Voice Assistant.")

        elif 'your name' in query:
            print("My Name is 'JENNIFER'.")
            speak("My Name is Jennifer.")

        elif 'for whom you work' in query:
            speak("I work for Nick Sir.")
            print("I work for Nick Sir.")

        elif 'what are you' in query:
            print("I am Jennifer, an Artificial Intelligence or AI Virtual Voice Assistance")
            speak("I am Jennifer, an Artificial Intelligence or AI Virtual Voice Assistance")

        elif 'sppu' in query:
            speak("Opening SPPU (Savitribai Phule Pune University) Website Sir !")
            webbrowser.open("http://www.unipune.ac.in/")
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'thank you' in query:
            print("Your Welcome Sir Always !")
            speak("Your Welcome Sir Always !")

        elif 'sure' in query:
            print("Ok Sir ! \n")
            speak("Ok Sir !")

        elif 'wait' in query:
            print("Alright Sir.")
            speak("Alright Sir.")

        elif 'how are you' in query:
            speak("I am Fine Sir, what about you sir?")
            print("I am Fine Sir, what about you sir?")

        elif 'i am fine' in query:
            speak("Nice, I always wish to god that keep my sir always happy, healthy and wealthy ! ")
            print("Nice, I always wish to god that keep my sir always happy, healthy and wealthy ! ")

        elif 'jennifer' in query:
            speak("Yes Sir !")
            print("Yes Sir !")

        elif 'jarvis' in query:
            print("Oops ! Sir, I am Jennifer not Jarvis.")
            speak("Oops ! Sir, I am Jennifer not Jarvis.")

        elif 'are you there' in query:
            print("For you always Sir...!")
            speak("For you always Sir...!")

        elif 'who am i' in query:
            print("You are NEEKUNJ Sir !")
            speak("You are NEEKU Sir !")

        elif 'think of me' in query:
            print(
                "I really like talking to you sir, I think you're an intelligent, funny, friendly, creative, helpful person sir. \n")
            speak(
                "I really like talking to you sir, I think you're an intelligent, funny, friendly, creative, helpful person sir.")

        elif 'thanks' in query:
            print("Your Welcome Sir !")
            speak("Your Welcome Sir !")

        elif 'open whatsapp' in query:
            speak("Opening Web Whatsapp Sir !")
            webbrowser.open("https://web.whatsapp.com/")
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'open c drive' in query:
            c = "C:\\"
            speak("Opening C Drive Sir !")
            os.startfile(c)
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'open d drive' in query:
            e = "D:\\"
            speak("Opening D Drive Sir !")
            os.startfile(e)
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        # elif 'open android studio' in query:
        #     stu = "D:\\Android Studio\\bin\\studio64.exe"
        #     speak("Opening Android Studio Sir !")
        #     os.startfile(stu)
        #     print("Sir, now what should I do for you?")
        #     speak("Sir, now what should I do for you?")

        # elif 'open win rar' in query:
        #     speak("Opening Win Rar Sir !")
        #     winrar = "C:\\Program Files\\WinRAR\\WinRAR.exe"
        #     os.startfile(winrar)
        #     print("Sir, now what should I do for you?")
        #     speak("Sir, now what should I do for you?")

        elif 'open notepad' in query:
            speak("Opening Note Pad Sir !")
            note = "C:\\Windows\\notepad.exe"
            os.startfile(note)
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'type' in query:
            Notepad()

        elif 'typing' in query:
            Notepad()

        # elif 'team viewer' in query:
        #     speak("Opening Team Viewer Sir !")
        #     team = "C:\\Program Files\\TeamViewer\\TeamViewer.exe"
        #     os.startfile(team)
        #     print("Sir, now what should I do for you?")
        #     speak("Sir, now what should I do for you?")
        #
        #
        # elif 'virtual box' in query:
        #     speak("Opening Virtual Box Sir !")
        #     vb = "C:\\Program Files\\Oracle\\VirtualBox\\VirtualBox.exe"
        #     os.startfile(vb)
        #     print("Sir, now what should I do for you?")
        #     speak("Sir, now what should I do for you?")
        #
        #
        # elif 'open node js' in query:
        #     speak("Opening Node JS Sir !")
        #     node = "C:\\Program Files\\nodejs\\node.exe"
        #     os.startfile(node)
        #     print("Sir, now what should I do for you?")
        #     speak("Sir, now what should I do for you?")


        elif 'open microsoft edge' in query:
            speak("Opening Microsoft Edge Sir !")
            me = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
            os.startfile(me)
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")


        elif 'open excel sheet' in query:
            speak("Opening Microsoft Excel Sheet Sir !")
            ex = "C:\\Program Files (x86)\\Microsoft Office\\Office16\\EXCEL.exe"
            os.startfile(ex)
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")


        elif 'open word' in query:
            speak("Opening Microsoft Office Word Sir !")
            word = "C:\\Program Files (x86)\\Microsoft Office\\Office16\\WINWORD.exe"
            os.startfile(word)
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")


        elif 'open powerpoint' in query:
            speak("Opening Microsoft Office Power Point Sir !")
            powerpoint = "C:\\Program Files (x86)\\Microsoft Office\\Office16\\POWERPNT.exe"
            os.startfile(powerpoint)
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")


        elif 'open outlook' in query:
            speak("Opening Microsoft Outlook Sir !")
            outlook = "C:\\Program Files (x86)\\Microsoft Office\\Office16\\OUTLOOK.exe"
            os.startfile(outlook)
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")


        elif 'open pycharm' in query:
            speak("Opening PyCharm Sir !")
            pyc = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2023.1.2\\bin\\pycharm64.exe"
            os.startfile(pyc)
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")


        elif 'do you want to sleep' in query:
            speak("No Sir ! But Thank You for Asking...! \n")
            print("No Sir ! But Thank You for Asking...!")

        elif 'open internet explorer' in query:
            speak("Opening Internet Explorer Sir !")
            internet = "C:\\Program Files (x86)\\Internet Explorer\\iexplore.exe"
            os.startfile(internet)
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")


        elif 'hello' in query:
            print("Hello Sir, How may I help you Sir? \n")
            speak("Hello Sir, How may I help You Sir?")

        elif 'wake up' in query:
            print("Sure Sir, tell me how may I help you? \n")
            speak("Sure Sir, tell me how may I help you?")

        elif 'jenni' in query:
            print("Yes Sir, tell me how may I help you ? \n")
            speak("Yes Sir, tell me how may I help you ?")

        elif 'do you have any boyfriend' in query:
            print("No Sir ! I am Happy to be Single. \n")
            speak("No Sir ! I am Happy to be Single.")


        # elif 'open vlc media player' in query:
        #     speak("Opening VLC Media Player Sir !")
        #     vlc = "C:\\Program Files\\VideoLAN\VLC\\vlc.exe"
        #     os.startfile(vlc)
        #     print("Sir, now what should I do for you?")
        #     speak("Sir, now what should I do for you?")


        elif 'command prompt' in query:
            speak("Opening Command Prompt Sir !")
            cmd = "C:\\Windows\\System32\\cmd.exe"
            os.startfile(cmd)
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'sorry' in query:
            print("No Problem Sir. \n")
            speak("No Problem Sir.")

        elif 'alright' in query:
            print("Yes Sir, Now what should I do for You? \n")
            speak("Yes Sir, Now what should I do for You?")

        elif 'what can you do' in query:
            print("I can do anything Sir! \n")
            speak("I can do anything for you Sir !")

        elif 'ip address' in query:
            ip = get("https://api.ipify.org").text
            print(f"Sir Your IP Address is: {ip} \n")
            speak(f"Sir your IP Address is : {ip}")
            print("Sir, now what should I do for you? \n")
            speak("Sir, now what should I do for you?")

        elif 'open facebook' in query:
            speak("Opening Face Book Sir !")
            webbrowser.open("http://www.facebook.com/")
            print("Sir, now what should I do for you? \n")
            speak("Sir, now what should I do for you?")

        elif 'search' in query:
            speak("Sir what should I search ?")
            cm = takeCommand().lower()
            print("Alright Sir, Let me Search...")
            speak("Alright Sir, Let me Search...")

            for search_data in search(cm, num_results=1, lang="en"):
                webbrowser.open(search_data)
            print("Sir, Result is been displayed on your screen. \n")
            speak("Sir, Result is been displayed on your screen.")
            print("Sir, now what should I do for you? \n")
            speak("Sir, now what should I do for you?")

        elif 'play a song' in query:
            speak("Sir, which song should I play for you?")
            so = takeCommand().lower()
            kit.playonyt(f"{so}")
            print(f"Playing Song {so} \n")
            speak(f"Sir Playing Song {so}")
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'send message' in query:
            print("Alright Sir !")
            speak("Alright Sir !")
            sendMessage()

        elif 'location' in query:
            location()


        elif 'quit' in query:
            hour = int(datetime.datetime.now().hour)

            if hour >= 22:
                print("Alright Sir, I am Quiting, Good Night, Sweet Dreams & Sleep well !\n")
                speak("Alright Sir, I am Quiting, Good Night, Sweet Dreams & Sleep well !")
                pygame.mixer.init()
                pygame.mixer.music.load("D:\\PYTHON Programming\\A.I Desktop Virtual Voice Assistance\\SOUNDS\\googlebeep.mp3")
                pygame.mixer.music.play()
                time.sleep(5)
                pygame.mixer.music.stop()
                sys.exit()

            else:
                print("Alright Sir, I am Quiting and Have a Good Day Sir...! \n")
                speak("Alright Sir, I am Quiting and Have a Good Day...!")
                pygame.mixer.init()
                pygame.mixer.music.load("D:\\PYTHON Programming\\A.I Desktop Virtual Voice Assistance\\SOUNDS\\googlebeep.mp3")
                pygame.mixer.music.play()
                time.sleep(5)
                pygame.mixer.music.stop()
                sys.exit()


        elif 'mail' in query:
            print("Alright Sir ! Opening G-Mail Account.")
            speak("Alright Sir ! Opening G-Mail Account.")
            webbrowser.open("https://mail.google.com/mail/u/0/#inbox")
            print("Sir, now what I should do for you ?")
            speak("Sir, now what I should do for you ?")


        elif 'stock market' in query:
            stockMarket()

        elif 'event' in query:
            print("Alright Sir !")
            speak("Alright Sir !")
            Event()

        elif 'news' in query:
            News()

        elif 'meet' in query:
            print("Alright Sir, Opening Google Meet")
            speak("Alright Sir, Opening Google Meet")
            webbrowser.open("https://meet.google.com/")
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'drive' in query:
            print("Alright Sir, Opening Google Drive.")
            speak("Alright Sir, Opening Google Drive.")
            webbrowser.open("https://drive.google.com/drive/my-drive")
            print("Sir, now what should I do for you?")
            speak("Sir, now what should I do for you?")

        elif 'battery' in query:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = str(battery.percent)
            plugged = "Plugged In" if plugged else "Not Plugged In"

            if percent <= '20':
                print(f"Sir your Battery Power is running slow, may I suggest you to charge it soon.")
                speak(f"Sir your Battery Power is running slow, may I suggest you to charge it soon.")
            else:
                print(f"Sir, your Battery Percent is {percent + '%'} And, You have {plugged} the charger.")
                speak(f"Sir, your Battery Percent is {percent + '%'} And, You have {plugged} the charger.")

        elif 'weather' in query:
            speak("Ok Sir !")
            CheckWeather()

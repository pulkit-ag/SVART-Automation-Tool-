import pyttsx3
import os
import speech_recognition as sr

pyttsx3.speak("Welcome to this application ! I'm your Personal Computer Assistant. I can perform following tasks at the moment.")
print("\t\t\t\t\tWelcome to PC Automation ")
print("\t\t\t------------------------------------")
print()

print("\t\t\t1.Opening notepad")
print("\t\t\t2.Opening camera ")
print("\t\t\t3.Opening calculator ")
print("\t\t\t4.Opening settings")
print("\t\t\t5.Opening Excel")
print("\t\t\t6.Opening Powerpoint")
print("\t\t\t7.Opening Applications")
print("\t\t\t8.Opening Paint")
print("\t\t\t9.Opening Word")
print("\t\t\t10.Opening Files Explorer")
print("\t\t\t11.Opening Microsoft Edge")
print("\t\t\t12.Opening Command Prompt")
print("\t\t\t13.Opening Control Panel")
print("\t\t\t14.Opening Calender")
print("\t\t\t15.Opening chrome ")
print("\t\t\t16.Opening VLC ")
print("\t\t\t17.Closing notepad")

print()
while True:
    pyttsx3.speak("What do you want me to do? ")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        print("Recognising...")
        data = r.recognize_google(audio).lower()
    if (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("write" in data)) and (
            ("notepad" in data) or ("editor" in data) or ("document" in data) or ("file" in data) or (
            "Notepad" in data)):
        print("Processing Input..")
        pyttsx3.speak("Opening Notepad")
        print("Opening notepad...")
        os.system("start Notepad")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("click" in data)) and (
            ("cam" in data) or ("camera" in data) or ("webcam" in data) or ("photo" in data)):
        print("Processing Input..")
        pyttsx3.speak("Opening Camera..")
        print("Opening camera...")
        os.system("start microsoft.windows.camera:")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("solve" in data)) and (
                     ("calculator" in data) or ("calc" in data) or ("operation" in data) or ("calculation" in data)):
        print("Processing Input..")
        pyttsx3.speak("Opening Calculator")
        print("Opening calculator...")
        os.system("start calc")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("change" in data)) and (
            ("settings" in data) or ("setting" in data)):
        print("Processing Input..")
        pyttsx3.speak("Opening Settings...")
        print("Opening settings...")
        os.system("start ms-settings:")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data)) and (
            ("excel" in data) or ("ms excel" in data) or ("msexcel" in data) or ("microsoft excel" in data) or (
            "spreadsheet" in data) or ("database" in data)):
        pyttsx3.speak("Opening M S Excel")
        os.system("start excel")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("make" in data)) and (
            ("powerpoint" in data) or ("ms powerpoint" in data) or ("mspowerpoint" in data) or ("microsoft powerpoint" in data) or (
            "presentation" in data)):
        pyttsx3.speak("Opening M S Powerpoint")
        os.system("start powerpnt")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("see" in data)) and (
            ("applications" in data) or ("apps" in data)):
        pyttsx3.speak("Opening Applications")
        os.system("start shell:appsfolder")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("draw" in data)) and (
            ("diagram" in data) or ("paint" in data) or ("ms paint" in data) or ("mspaint" in data)):
        pyttsx3.speak("Opening M S Paint")
        os.system("start mspaint")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("write" in data)) and (
            ("Word" in data) or ("word" in data) or ("msword" in data) or ("ms word" in data)):
        pyttsx3.speak("Opening M S Word")
        os.system("start winword")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data)) and (
            ("file explorer" in data) or ("explorer" in data)):
        pyttsx3.speak("Opening File Explorer")
        os.system("start explorer")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data)) and (
            ("controlpanel" in data) or ("control panel" in data) or ("cpanel" in data) or ("control" in data)):
        pyttsx3.speak("Opening Control Panel")
        os.system("start control")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data)) and (
            ("cmd" in data) or ("commandprompt" in data) or ("command prompt" in data)):
        pyttsx3.speak("Opening Command Prompt")
        os.system("start cmd")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data)) and ("calendar" in data):
        pyttsx3.speak("Opening Calendar")
        os.system("start outlookcal:")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("launch" in data)) and (
            ("msedge" in data) or ("microsoft edge" in data)):
        pyttsx3.speak("Opening Microsoft Edge")
        os.system("start microsoft-edge:")
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data)) and (
            ("chrome" in data) or ("browser" in data) or ("Chrome" in data)):
        print("Processing Input..")
        pyttsx3.speak("Opening Chrome")
        print("Opening chrome...")
        os.system("start chrome")
    
    elif (("run" in data) or ("execute" in data) or ("open" in data) or ("start" in data) or ("play" in data)) and (
            ("vlc" in data) or ("player" in data) or ("music" in data) or ("song" in data)):
        print("Processing Input..")
        pyttsx3.speak("Opening Music Player...")
        print("Opening music player...")
        os.system("start vlc")
    elif (("close" in data) or ("exit" in data) or ("stop" in data)) and (
            ("notepad" in data) or ("editor" in data) or ("document" in data) or ("file" in data) or (
            "Notepad" in data)):
        print("Processing Input..")
        pyttsx3.speak("Closing Notepad")
        print("Closing notepad...")
        os.system("tskill notepad")
    elif ("exit" in data) or ("quit" in data) or ("thank you" in data) or ("leave" in data):
        break
    else:
        pyttsx3.speak("This application is not supported yet!")
        print("Not supported till now")
pyttsx3.speak("Thank you for using me ! Have a nice day.")
print("Thank you ! ")

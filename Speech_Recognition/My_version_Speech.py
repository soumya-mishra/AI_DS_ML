from gtts import gTTS
import speech_recognition as sr
import os
import re
import webbrowser
import smtplib
import requests   

def talkToMe(audio):
    "speaks audio passed as argument"

    print(audio)
    for line in audio.splitlines():
        os.system("say " + audio)
        
def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Ready...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        print('You said: ' + command + '\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        print('Your last command couldn\'t be heard')
        command = myCommand();

    return command

def assistant(command):
    "if statements for executing commands"

    if 'open google' in command:
        reg_ex = re.search('open google (.*)', command)
        url = 'https://www.google.com/'
        if reg_ex:
            subreddit = reg_ex.group(1)
            url = url + 'r/' + subreddit
        webbrowser.open(url)
        print('Done!')
        
    elif 'what\'s up' in command:
        talkToMe('Just doing my thing')
    
    elif 'open outllok' in command:
        os.startfile('C:/ProgramData/Microsoft/Windows/Start Menu/Programs/Outlook 2016')
              
    
    elif 'email' in command:
        talkToMe('Who is the recipient?')
        recipient = myCommand()

        if 'Soumya' in recipient:
            talkToMe('What should I say?')
            content = myCommand()

            #init gmail SMTP
            mail = smtplib.SMTP('smtp.gmail.com', 587)

            #identify to server
            mail.ehlo()

            #encrypt session
            mail.starttls()

            #login
            mail.login('username', 'password')

            #send message
            mail.sendmail('Soumya', 'soumyaiter@gmail.com', content)

            #end mail connection
            mail.close()

            talkToMe('Email sent.')
        else:
            talkToMe('I don\'t know what you mean!')

talkToMe('I am ready for your command')

#loop to continue executing multiple commands
while True:
    assistant(myCommand())            

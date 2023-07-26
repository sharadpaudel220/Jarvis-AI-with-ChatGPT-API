import speech_recognition as sr
import subprocess
import os
import webbrowser
import openai
import datetime
from config import apikey
import random

chatStr= ""
def chat(query):
    global chatStr
    openai.api_key = apikey
    chatStr += f"Sharad: {query}\n Jarvis: "
    message = [
        {"role": "system", "content": query}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    if "choices" in response and len(response["choices"]) > 0 and "message" in response["choices"][0]:
        generated_text = response["choices"][0]["message"]["content"]
        chatStr += f"User: {query}\nJarvis: {generated_text}\n"
        say(generated_text)
        return generated_text
    else:
        print("Error: Failed to get a valid response from the AI.")
        chatStr += "Jarvis: Error: Failed to get a valid response from the AI.\n"
        return "Error: Failed to get a valid response from the AI."

# For voice command
def ai(prompt):
    openai.api_key = apikey
    text = f" open AI response for prompt: {prompt} \n ********************** \n \n"
    message = [
        {"role": "system", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=message,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    if "choices" in response and len(response["choices"]) > 0 and "message" in response["choices"][0]:
        generated_text = response["choices"][0]["message"]["content"]
        print(generated_text)
        text += generated_text+ "\n"
        return generated_text
    else:
        print("Error: Failed to get a valid response from the AI.")
        # text += "Error: Failed to get a valid response from the AI."

    if not os.path.exists("openAI"):
        os.mkdir("openAI")

    with open(f"openAI/{prompt[0:25]}.txt", "w") as f:
        f.write(text)


def say(text):
    subprocess.run(["say", text])
    # subprocess.run(["say", "-v", text])

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Processing command...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            print("Some error detected boss. I apologize.")
            exit()


if __name__ == '__main__':
    say("At your service Boss")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
                 ["google", "https://www.google.com"], ["whatsapp", "https://www.whatsapp.com"] ]
        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"opening {site[0]} Boss")
                webbrowser.open(site[1])
        if "open music" in query:
            musicPath= "/Users/sharadpaudel/Downloads/1.mp3"
            os.system(f"open {musicPath}")
            # print(query)

        elif "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Boss the time now is {strfTime}")

        elif "open facetime".lower() in query.lower():
            os.system(f"open /System/Applications/FaceTime.app")
            say("Opening facetime now...")

        elif "shutdown".lower() in query.lower():
            os.system("shutdown /r")
            say("Shutting your macbook now. Bye Bye.")

        elif "jarvis".lower() in query.lower():
            ai(prompt=query)

        elif "Quit now".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print('chatting...')
            chat(query)




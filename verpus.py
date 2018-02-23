import speech_recognition as sr
import time
import json
from bullshit import Bullshit
from retaliator import Retaliator


bullshit = Bullshit();
with open("houndify_auth.json") as file:
    houndifyAuth = json.load(file)

retaliator = Retaliator()

def process_stream(recogniser, audio):
    words = recogniser.recognize_houndify(
        audio,
        houndifyAuth["client_id"],
        houndifyAuth["client_key"]
    )
    if len(words) and bullshit.detect(words):
        print("Bullshit detected")
        if (bullshit.canRetaliate()):
            retaliator.retaliate()


sourceMic = sr.Microphone(device_index=1)
recogniser = sr.Recognizer();
listenThread = recogniser.listen_in_background(sourceMic, process_stream)

while True: time.sleep(0.1)

import json

class Bullshit:
    def __init__(self):
        self.bullshitWords = lines = open("bullshit.txt").read().lower().splitlines()
        self.detectedBullshit = 0

        with open("config.json") as file:
            config = json.load(file)

        self.bullshitLimit = config["bullshit_limit"]

    def detect(self, words):
        words = words.split(" ");
        if isinstance(words, str):
            words = [words]

        detected = False
        for word in words:
            if word in self.bullshitWords:
                self.detectedBullshit += 1
                detected = True
        return detected

    def canRetaliate(self):
        return self.detectedBullshit >= self.bullshitLimit
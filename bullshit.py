class Bullshit:
    def __init__(self):
        self.bullshitWords = lines = open("bullshit.txt").read().lower().splitlines()
        self.detectedBullshit = 0
        self.bullshitLimit = 2

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
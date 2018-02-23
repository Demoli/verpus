import winsound


class Retaliator:
    def __init__(self) -> None:
        pass

    def retaliate(self):
        winsound.PlaySound('resources/alarm.wav', winsound.SND_FILENAME)

MAX_INVENTORY = 8
LIVES = [2, 4, 4]

#SHOTGUN STATS
MAX_SHELLS = 8
MAG  = [None for i in range(MAX_SHELLS)]

class player:
    def __init__(self, name):
        self.name = name
        self.inventory = [None for i in range(MAX_INVENTORY)]
        self.lives = 1

def load(mag, ShellNum, LivesNum):
    BlanksNum = ShellNum - LivesNum
    for i in range(LivesNum):
        mag[i] = "LIVE"
        mag[i+BlanksNum] = "BLANK"

if __name__ == "__main__":
    load(MAG, 8, 4)
    print(MAG)

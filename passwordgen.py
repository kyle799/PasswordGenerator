import random as r
from random import shuffle
from sys import argv
numbs = "1234567890"
lower = "qwertyuiopasdfghjklzxcvbnm"
special = ",.!@#$%^&*()<>"
uppers = "QWERTYUIOPASDFGHJKLZXCVBNM"
chars = numbs + lower + special + uppers
if argv[2] = 0:
a = argv[2]
print(a)
a = int(a)

def main():
    global new_password
    new_password = ""
    incrementer = 0
    def get_char(characters):
        global new_password
        index = r.randint(0, len(characters))
        new_password = new_password + characters[index - 1]
    while a > incrementer:
        if incrementer < 2:
            incrementer += 1
            get_char(numbs)
        elif incrementer < 4:
            incrementer += 1
            get_char(special)
        elif incrementer < 6:
            incrementer += 1
            get_char(uppers)
        elif incrementer < 8:
            incrementer += 1
            get_char(lower)
        elif incrementer < a:
            incrementer += 1
            get_char(chars)
    def shuffle_password(new_password):
        new_password = list(new_password)
        shuffle(new_password)
        return ''.join(new_password)
    for i in range(10):
        new_password = shuffle_password(new_password)
    print(new_password)

if __name__ == "__main__":
    main()
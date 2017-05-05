# Python program to illustrate a loop with condition at the bottom
# Roll a dice untill user chooses to exit

# import random module
import random

turn = 0
diceKeys = []
dices = {}

def startGame():
    global turn
    global diceKeys
    global dices

    turn = 1
    diceKeys = ['1', '2', '3', '4', '5']
    dices = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

def createScoreText(score):
    if score[0][1] == 5:
        text = "PYTZEE"
    elif score[0][1] == 4:
        text = "Carré"
    elif score[0][1] == 3:
        if score[1][1] == 2:
            text = "Full house"
        else:
            text = "Three of a kind"
    elif score[0][1] == 2:
        if score[1][1] == 2:
            text = "Two pairs"
        else:
            text = "One pair"

    return text

def createScore(dices):
    score = {1:0,2:0,3:0,4:0,5:0,6:0}
    k = 1
    while k <= 5:
        score[dices[k]] = score[dices[k]] + 1
        k = k + 1

    score = [(l, score[l]) for l in sorted(score, key=score.get, reverse=True)]

    text = createScoreText(score)

    return text


startGame()

print("*******************************")
print("*      Welcome to PYTZEE     *")
print("*******************************")
print("  2017 Created by Tom Vermost")
while True:
   print("Turn",turn)
   input("Press enter to roll the dices")
   i = 1
   num = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
   while i <= 5:
       if dices[i] == 0:
           # get a number between 1 to 6
           num[i] = random.randint(1,6)
           print("Dice", i, ":", num[i])
       else:
           print("[kept]Dice", i, ":", dices[i])

       i = i + 1

   if turn < 3:
       showUI = True
       option = ''
       while option != '0':
           if option in diceKeys:
               if option != '':
                   option = int(option)
                   if dices[option] == 0:
                       dices[option] = num[option]
           kept = []
           m = 1
           while m <= 5:
               if dices[m] != 0:
                   kept.append(dices[m])
                   diceKeys[m - 1] = ''
               m = m + 1
           if len(kept) > 0:
               print("Dices kept:", kept)
           if showUI == True:
               print("Which dices do you want to keep?")
               print(diceKeys)
               print("or 0 to end turn")
               showUI = False
           option = input(">>")
       turn = turn + 1
   else:
       j = 1
       while j <= 5:
           if dices[j] == 0:
               dices[j] = num[j]
           j = j + 1

       score = createScore(dices)

       print('Your score:', score)

       again = input("Play again? y/n")
       if again == 'n':
           break
       else:
           startGame()
__author__ = 'Quasi-Boden'

import requests
import random
from bs4 import BeautifulSoup
import itertools

totalPrizePot = 0
playerCount = 20
numGames = 8

def compare(userNumbers, winningNumbers):
    prizePot = 0
    result = []
    for element in userNumbers:
        if element in winningNumbers:
            result.append(element)

    if len(result) == 0:
        print("No matches were found!")
        print("Current Prize Pot is: $" + str(prizePot))
    elif len(result) == 1:
        prizePot += 2
        print("One number matched! $2 added to Group Winnings!")
        print("Current Prize Pot is: $" + str(prizePot))
    elif len(result) == 2:
        prizePot += 5
        print("Two numbers matched! $5 added to Group Winnings!")
        print("Current Prize Pot is: $" + str(prizePot))
    elif len(result) == 3:
        prizePot += 50
        print("Three numbers matched! $50 added to Group Winnings!")
        print("Current Prize Pot is: $" + str(prizePot))
    elif len(result) == 4:
        prizePot += 5000
        print("Four numbers matched! $5000 added to Group Winnings!")
        print("Current Prize Pot is: $" + str(prizePot))
    elif len(result) == 5:
        prizePot += 200000000
        print("Five numbers matched! $20000000 added to Group Winnings!")
        print("Current Prize Pot is: $" + str(prizePot))

    return prizePot


url = 'http://www.megamillions.com/'
megaMillionsHomePage = requests.get(url)

soup = BeautifulSoup(megaMillionsHomePage.content)
groupA = []

totalNum = 0

for i in range(0, playerCount):
    firstPick = random.randint(1, 75)
    secondPick = random.randint(1, 75)
    thirdPick = random.randint(1, 75)
    fourthPick = random.randint(1, 75)
    fifthPick = random.randint(1, 75)
    matchPick = random.randint(1, 15)
    userPick = [firstPick, secondPick, thirdPick, fourthPick, fifthPick, matchPick]
    groupA.append(userPick)
   # print(groupA)

megaMillionsWinningNumbers = [7, 22, 27, 41, 49, 10]

for game in range(0, numGames):
    for player in groupA:
        totalPrizePot += compare(player, megaMillionsWinningNumbers)

print(str(playerCount) + " Players won $" + str(totalPrizePot) + " over the course of " + str(numGames) + " games!")
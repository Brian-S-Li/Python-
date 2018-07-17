import random

def main():
    done = False
    while not done:
        choice = str(input("What would you like to do? "+
                           "Type name (coin, dice, rearrange, "+
                           "pickSome, or randomRange): "))

        if choice == "coin":
            print(coinFlip())
        elif choice == "dice":
            num = dieRoll()
            print(num)
        elif choice == "rearrange":
            myList = rearrange()
            print(myList)
        elif choice == "pickSome":
            myList = pickSome()
            print(myList)
        elif choice == "randomRange":
            num = randRange()
            print(num)
        else:
            print("I didn't quite get that. Try again")
        done = tryAgain()


def coinFlip():
    coin = random.randint(0, 1)
    if coin == 1:
        return "Heads"
    elif coin == 0:
        return "Tails"


def dieRoll():
    die = random.randint(1, 6)
    return str(die)


def pickSome():
    elementList = []
    numToReturn = int(input("How many items would you like returned?"))
    done = False
    while not done:
        item = str(input("Add something to the list or q to exit"))
        if item == "q":
            done = True
        else:
            elementList.append(item)
    random.shuffle(elementList)
    newList = []
    for i in range(numToReturn):
        newList.append(elementList[i])
    return newList


def rearrange():
    elementList = []
    done = False
    while not done:
        item = str(input("Add something to the list or quit to exit"))
        if item == "q":
            done = True
        else:
            elementList.append(item)
    random.shuffle(elementList)
    return elementList


def randRange():
    elementList = []
    numToReturn = int(input("How many items would you like returned?"))
    upRange = int(input("Give me an upper range inclusive"))
    lowRange = int(input("Give me a lower range inclusive"))
    for i in range(lowRange, upRange + 1):
        elementList.append(i)
    random.shuffle(elementList)
    newList = []
    for i in range(numToReturn):
        newList.append(elementList[i])
    return newList


def tryAgain():
    done = False
    while not done:
        inp = input("Do you want to try again? Y/N")
        if inp.lower() == "n":
            print("Thanks")
            return True
        elif inp.lower() == "y":
            return False
        else:
            print("Sorry I didn't get that, please try again.")

main()

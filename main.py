from functions import *
from logging import *
from scenarios import *

while True:
    returnedcharacterselection = first_user_input()
    if returnedcharacterselection == False:
        getLogger("MAIN").error("Your character selection was invalid. Please double check your input.")
        print("Your character selection was invalid. Please double check your input.")
        continue

    returnedcharacterdata = character_modification(returnedcharacterselection)
    print (f" Your stats are as follows... {returnedcharacterdata}")
    break

while True:
    scenariodetermined = randint(0, 6)
    if scenariodetermined == 0:
        resultofbandit = bandit_encounter(returnedcharacterdata)
        if resultofbandit == "InputInvalid":
            getLogger("MAIN").error("Your choice was invalid. Please double check your input.")
            print("Your choice was invalid. Please double check your input.")
            continue
        if resultofbandit == False:
            print ("Game over...")
    if scenariodetermined == 1:
        resultoftrader = orion_encounter(returnedcharacterdata)
        if resultoftrader == "InputInvalid":
            getLogger("MAIN").error("Your choice was invalid. Please double check your input.")
            print("Your choice was invalid. Please double check your input.")
            continue
        if resultoftrader == False:
            print ("Game over...")


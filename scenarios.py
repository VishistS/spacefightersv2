from random import *

def bandit_encounter(cattributes):
    print("You have encountered a group of Nebula bandits... They seek your fortunes...")
    offer_input = input("They offer to let you go in exchange for 50 Wealth... Do you accept? \n")
    banditpower = randint(25,100)
    try:
        if offer_input == "Y":
            if cattributes["Wealth"] >= 100:
                cattributes["Wealth"] = cattributes["Wealth"] - 100
                print ("You have been spared...")
                return True
        if offer_input == "N":
            if cattributes["Power"] > banditpower:
                print ("You were forced into combat with the bandits... However, your superior fleet defeated theirs...")
                return True
            if cattributes["Power"] < banditpower:
                print ("You were forced into combat with the bandits... However, your fleet was crushed by theirs...")
                return False
    except:
        return "InputInvalid"


def orion_encounter(cattributes):
    orionpower = randint(0,50)
    orionwealth = randint(50,100)
    oriontech = randint(75,100)
    print("You have encountered a group of Orion Collective trader ships... They wish to to trade with you...")
    attacktrade_input = input("Do you want to trade...Or attack...")
    try:
        if attacktrade_input == "Attack":
            if cattributes["Power"] > orionpower:
                cattributes["Power"] = cattributes["Power"] + (orionpower/2)
                cattributes["Wealth"] = cattributes["Wealth"] + (orionwealth/2)
                cattributes["Technology"] = cattributes["Technology"] + (oriontech/2)
                print("Your attack was unsuspected... The trader's riches are now yours...")
                return True
            else:
                print("Your attack was unsuspected... However the traders fleet was underestimated...")
                return False
        if attacktrade_input == "Trade":
            secondtradeinput = input("Would you like to acquire new technology(Technology) or bolster your fleet?(Power)\n")
            if secondtradeinput == "Technology":
               techtradeinput = input("The traders are willing to trade you 50 Technology in exchange for 50 Wealth. Do you accept?\n")
               if techtradeinput == "Y":
                   cattributes["Wealth"] = cattributes["Wealth"] - 50
                   cattributes["Technology"] = cattributes["Technology"] + 50
                   print("The traders are pleased with the deal...")
                   return True
               if techtradeinput == "N":
                   print ("The traders are unamused with you wasting their time...")
                   return True
            if secondtradeinput == "Power":
                   powertradeinput = input("The traders are willing to trade you 50 Power in exchange for 50 Wealth. Do you accept?\n")
                   if powertradeinput == "Y":
                       cattributes["Wealth"] = cattributes["Wealth"] - 50
                       cattributes["Power"] = cattributes["Power"] + 50
                       print("The traders are pleased with the deal...")
                       return True
                   if powertradeinput == "N":
                       print("The traders are unamused with you wasting their time...")
                       return True
    except:
            return "InputInvalid"

def abandoned_planet(cattributes):
    planettech = randint(50, 75)
    success_chance = randint(1,3)
    print("Your fleet admiral reports that there is an abandoned planet near your current location...")
    planet_explore_input = input("It is estimated it would cost 25 Technology to explore the planet - given it's extreme climate... Do you wish to explore?")
    if planet_explore_input == "Y":
        if success_chance == 3:






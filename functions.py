introductionbackgroundlore = "The Galaxy of Netubus is vast and expansive... It is up to you to determine your fate in this lonely place."
firstuserinputprompt = "Hello user. Welcome, before starting you must select a faction and difficulty. OPTIONS : Brigand, Fortunekeeper, Phrenic. OPTIONS : Easy, Medium, Hard\n"
formattingprompt = "Please make sure your input is case sensitive. Seperate it with a :"
acceptedfactions = ["Brigand", "Fortunekeeper", "Phrenic"]
accepteddifficulties = ["Easy", "Medium", "Hard"]

def first_user_input():
    print(introductionbackgroundlore)
    print(formattingprompt)
    faction_input = input(firstuserinputprompt)
    fac_input_for_dic = faction_input.split(":")
    try:
        fac_input_dictionary = {"Faction": fac_input_for_dic[0], "Difficulty": fac_input_for_dic[1]}
        if fac_input_dictionary["Faction"] in acceptedfactions:
            return fac_input_dictionary
        if fac_input_dictionary["Faction"] not in acceptedfactions:
            return False
    except:
        return False

def character_modification(givencharacterdict):
    Wealth = 0
    Power = 0
    Technology = 0
    if givencharacterdict["Faction"] == "Brigand":
            Wealth = 100
            Power = 150
            Technology = 50
            return {"Wealth": Wealth, "Power": Power, "Technology": Technology}
    if givencharacterdict["Faction"] == "Fortunekeeper":
            Wealth = 200
            Power = 50
            Technology = 50
            return {"Wealth": Wealth, "Power": Power, "Technology": Technology}
    if givencharacterdict["Faction"] == "Phrenic":
            Wealth = 100
            Power = 50
            Technology = 150
            return {"Wealth": Wealth, "Power": Power, "Technology": Technology}

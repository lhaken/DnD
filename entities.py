def hasNumber(string):
    for character in string:
        if character.isdigit():
            return True
        else:
            pass
    return False

def isNumber(integer):
    try:
        integer = int(integer)
        return True
    except ValueError:
        return False

dmgTypes = ["NONE", "PHYSICAL", "MAGIC", "FIRE", "WATER", "PIERCING"]

class entity:     
    def createEntity(self):
        self.name = input("Jméno bytosti > ")
        while hasNumber(self.name):
            print("ERROR - Jméno bytosti nesmí obsahovat číslo. Prosím zkuste to znovu.")
            self.name = input("Jméno bytosti > ")

        self.level = input("Úroveň bytosti > ")
        while not isNumber(self.level):
            print("ERROR - Úroveň bytosti musí být reprezentována celým číslem. Prosím zkuste to znovu.")
            self.level = input("Úroveň bytosti > ")

        self.hp = input("Životy bytosti > ")
        while not isNumber(self.hp):
            print("ERROR - Životy bytosti musí být reprezentována celým číslem. Prosím zkuste to znovu.")
            self.hp = input("Životy bytosti > ")

        self.speed = input("Rychlost bytosti > ")
        while not isNumber(self.speed):
            print("ERROR - Rychlost bytosti musí být reprezentována celým číslem. Prosím zkuste to znovu.")
            self.speed = input("Rychlost bytosti > ")

        self.armorClass = input("Brnění bytosti > ")
        while not isNumber(self.armorClass):
            print("ERROR - Brnění bytosti musí být reprezentována celým číslem. Prosím zkuste to znovu.")
            self.armorClass = input("Brnění bytosti > ")

        self.dmg = input("Poškození bytosti > ")
        while not isNumber(self.dmg):
            print("ERROR - Poškození bytosti musí být reprezentována celým číslem. Prosím zkuste to znovu.")
            self.dmg = input("Poškození bytosti > ")

        print(dmgTypes)
        self.dmgResist= input("Jakému typu poškození je bytost odolná? > ")
        while self.dmgResist.upper() not in dmgTypes:
            print("ERROR - Typ poškození není v nabídce. Prosím zkuste to znovu.")
            self.dmgResist= input("Jaký je typ poškození bytosti? > ")

        #finish abilities and weakness

    def saveEntity(self):
        entitiesFile = open("entities.txt", "a+")
        entitiesFile.write("${}\nlevel:{}\nHP:{}\nDMG:{}\nspeed:{}\narmor class:{}\nresist:{}\n\n".format(self.name, self.level, self.hp, self.dmg, self.speed, self.armorClass, self.dmgResist))

        entitiesFile.close()

addEntity = entity()
addEntity.createEntity()
addEntity.saveEntity()
        

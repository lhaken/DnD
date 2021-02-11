import random
import entities
import items

print(" ")
print("  OVLÁDÁNÍ - akce, které můžete provést jsou označeny pomlčkami  ")
print("#############################PŘÍKLAD#############################")
print("Jste v místnosti s postelí a dveřmi. Chcete -spát- nebo -odejít-?")
print("pro přespání napíšeme - 'spát'     pro odchod napíšeme - 'odejít'")
print("#############################PŘÍKLAD#############################")
print(" ")

# inventory will be saved into a txt file - beta inventory not saving -> also will be checked if all the bonuses from weapons are still active -> if you sell a weapon bonus must be cancelled

def initPlayer():
    
    global player
    
    global inventory

    inventory = []
    
    player = entities.activeEnemy()
    player.findEntity("player")
    player.hp = int(player.hp)
    player.dmg = int(player.dmg)
    player.spd = int(player.speed)

def roll():
    global playerRoll
    global enemyRoll
    
    playerRoll = random.randint(0, 10)
    enemyRoll = random.randint(0, 10)

def decision():
    global answer
    
    answer = input(">> ")
    print(" ")
    
def fight(entity):
    
    global player
    
    global keyTaken
    global goblinSlayed
    global doorsUnlocked
    global enemy
    
    roll()
    enemy = entities.activeEnemy()
    enemy.findEntity(entity)
    if playerRoll >= enemyRoll:
        while player.hp > 0 and enemy.hp > 0:
            action = input("-zaútočit-, -krýt- >> ")
            if action == "krýt":
                print("Vykryl jsi útok.")
                print("ŽIVOTY Hráč - " + str(player.hp) + " ♥ Nepřítel - " + str(enemy.hp) + " ♥")
                print(" ")
            elif action == "zaútočit":
                round(player, enemy)
                round(enemy, player)
            else:
                print("Špatný tah. " + enemy.name.capitalize() + " na tebe útočí!")
                player.hp -= enemy.dmg
                print(enemy.name.capitalize() + " ti dává " + str(enemy.dmg) + " poškození.")
                print("ŽIVOTY Hráč - " + str(player.hp) + " ♥ Nepřítel - " + str(enemy.hp) + " ♥")
    elif playerRoll < enemyRoll:
        while player.hp > 0 and enemy.hp > 0:
            action = input("-zaútočit-, -krýt- >> ")
            if action == "krýt":
                print("Vykryl jsi útok.")
                print("ŽIVOTY Hráč - " + str(player.hp) + " ♥ Nepřítel - " + str(enemy.hp) + " ♥")
                print(" ")
            elif action == "zaútočit":
                round(enemy, player)
                round(player, enemy)
            else:
                print("Špatný tah. " + enemy.name.capitalize() + " na tebe útočí!")
                player.hp -= enemy.dmg
                print(enemy.name.capitalize() + " ti dává " + str(enemy.dmg) + " poškození.")
                print("ŽIVOTY Hráč - " + str(player.hp) + " ♥ Nepřítel - " + str(enemy.hp) + " ♥")
                print(" ")
    else:
        print("Unknown error")

def round(attacker, defender):
    global goblinSlayed
    
    dodge1 = random.randint(0, 20)
    dodge2 = random.randint(0, 20)
    if player.hp > 0 and enemy.hp > 0:
        if dodge1 < defender.speed:
            print("Útok minul.")
        else:
            defender.hp -= attacker.dmg
            print(defender.name.capitalize() + " dostává " + str(attacker.dmg) + " poškození.")
            print("ŽIVOTY Hráč - " + str(player.hp) + " ♥ Nepřítel - " + str(enemy.hp) + " ♥")
            print(" ")
            if defender.hp <= 0:
                print(defender.name.capitalize() + " byl zabit!")
                goblinSlayed = True
                return
            else:
                pass
    else:
        pass

def room1():
    global inventory
    global keyTaken
    global goblinSlayed
    global doorsUnlocked
    
    print("Všechny tři dveře jsou vedle sebe a vypadají jedny jako druhé. Do kterých chceš jít? -pravé-, -levé- nebo -prostřední-")
    decision()
    answers = ["pravé", "levé", "prostřední"]
    while answer not in answers:
        print("Vypadá to, že jsi zadal špatnou možnost. Zkus 'pravé', 'levé' nebo 'prostřední'.")
        decision()
    else:
        if answer == "pravé":
            if keyTaken == False:
                print("Dveře jsou odemčené. Když vejdeš do místnosti vidíš pouze klíč. Chceš si klíč -vzít- nebo ho chceš -nechat- jen tak ležet?")
                decision()
                answers = ["vzít", "nechat"]
                while answer not in answers:
                    print("Vypadá to, že jsi zadal špatnou možnost. Zkus 'vzít' nebo 'nechat'.")
                    decision()
                else:
                    if answer == "vzít":
                        inventory.append("klíč")
                        keyTaken = True
                        print("Sebral jsi klíč a vracíš se do místnosti se třemi dveřmi.")
                        room1()
                    else:
                        print("Necháváš klíč klíčem a vracíš se do místnosti se třemi dveřmi.")
                        room1() 
            else:
                print("Ale tady už jsi přeci byl a našel jsi zde klíč. Není tu už vůbec nic a proto se vracíš do místnosti se třemi dveřmi.")
                room1()
        elif answer == "levé":
            if goblinSlayed == False:
                print("Když vkročíš do místnosti setkáváš se s goblinem, který nevypadá moc přátelsky. Chceš -utéct- nebo -zaútočit-?")
                decision()
                answers = ["utéct", "zaútočit"]
                while answer not in answers:
                    print("Vypadá to, že jsi zadal špatnou možnost. Zkus 'utéct' nebo 'zaútočit'.")
                    decision()
                else:
                    if answer == "zaútočit":
                        fight("goblin")
                        print("Epický souboj! Již v místnosti nic není. Vracíš do místnosti se třemi dveřmi.")
                        room1()
                    else:
                        print("Rozhodl jsi se utéct zpět do místnosti se třemi dveřmi.")
                        room1()
            else:
                print("Tuhle místnost si moc dobře pamatuješ. Tady jsi se utkal s tím proradným goblinem. Není tu nic k vidění a proto se vracíš do místnosti se třemi dveřmi.")
                room1()
        else:
            if "klíč" in inventory:
                print("Vsunul jsi klíč do klíčové dírky a otočil s ním. *cvak* Dveře se otevřely a... toto je zatím konec naší hry. Děkujeme na přehrání.")
                restart()
            else:
                print("Dveře jsou zamknuté. Asi budeš potřebovat nějaký klíč.")
                room1()
def story():
    global player
    global keyTaken
    global goblinSlayed
    global doorsUnlocked
    global inventory
    
    print("Právě jsi se probudil v cele. Nemáš nejmenší tušení jak jsi se sem dostal a ani nevíš kde jsi.")
    print("Mřížové dveře jsou rezavé a s trochou síly by určitě povolily. Chceš, zkusit dveře vyrazit a -odejít- nebo chceš radši -zůstat-?")
    decision()
    answers = ["zůstat", "odejít"]
    while answer not in answers:
        print("Vypadá to, že jsi zadal špatnou možnost. Zkus 'odejít' nebo 'zůstat'.")
        decision()
    else:
        while answer == "zůstat":
            print("Na nic si nevzpomínáš a v cele nic zvláštního nevidíš.")
            decision()
        else:
            print("Povedlo se! Dveře povolily a ty teď stojíš v místnosti. Když se rozhlédneš, uvidíš troje dveře a dýku. Chceš -vzít- dýku a poté jít ke dveřím, nebo -jít- ke dveřím rovnou?")
            decision()
            answers = ["vzít", "jít"]
            while answer not in answers:
                print("Vypadá to, že jsi zadal špatnou možnost. Zkus 'jít' nebo 'vzít'.")
                decision()
            else:
                if answer == "vzít":
                    print("Dobrá volba! Určitě se ti bude hodit.")
                    inventory.append("dýka")
                    item = items.pickItem()
                    item.findItem("dýka")
                    if item.ability == "STRENGTH":
                        player.dmg += item.bonus
                    elif item.ability == "HP":
                        player.hp += item.bonus
                    elif item.ability == "SPEED":
                        playerSPD += item.bonus       
                    else:
                        pass
                else:
                    print("Dýku necháváš ležet na zemi a jdeš ke dveřím.")

                keyTaken = False
                goblinSlayed = False
                doorsUnlocked = False
                
                room1()

def restart():
    rstrt = input("Přeješ si hru restartovat? (a/n) >> ")
    if rstrt == "a":
        initPlayer()
        story()
    elif rstrt == "n":
        return
    else:
        print("Špatný input.")
        restart()
                             
initPlayer()
story()

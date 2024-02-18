import random

print("You are in a mideval town and have been sent to explore a dungeon \nfirst you need to be outfitted with gear.")
print()

health = int(20)
weapon = input("The first item that you get to pick is a Weapon. \nYour choices are: SWORD, AXE, MACE, or DAGGERS ")
print()

while not weapon.lower() in ("sword","axe","mace",'daggers'):
    weapon = input("The first item that you get to pick is a Weapon. \nYour choices are: SWORD, AXE, MACE, or DAGGERS ")
    print()
else:
    if weapon.lower == "sword":
        attack = 3
        damage = 5
    elif weapon.lower == "axe":
        attack = 2
        damage = 9
    elif weapon.lower == "mace":
        attack = 1
        damage = 21
    else:
        attack = 4
        damage = 3
attack = int(attack)
damage = int(damage)

print()
armor = input("The next equiptment that you get to pick is your armor:\n your choices are: LEATHER, CHAINMAIL, PLATE ")
print()
print(armor.lower())
while not armor.lower() in ("leather","chainmail","plate"):
    armor = input("The next equiptment that you get to pick is your armor:\n your choices are: LEATHER, CHAINMAIL, PLATE ")
    print()
else:
    if armor.lower() == "leather":
        attack = (attack * 3)
        protection = 2
    elif armor.lower() == "chainmail":
        attack = attack * 2
        protection = 4
    elif armor.lower() == "plate":
        attack = attack * 1
        protection = 6
protection = int(protection)


print(f"the number of attacks you get per turn is your attack stat. your attack stat is: {attack}")
print(f"your damage will roll between 1 and your damage stat your damage is: {damage} ")
print(f"Protection reduces the damage that you take your protection is: {protection}")

dungeon = input("Now it is time to head into a dungeon where would you like to go? \n your choices are: FOREST, CAVE, TOWER ")

wolf_health = int(13)
wolf_damage = int(9)
Twolf_health = int(26)
Twolf_damage = int(15)
# ///////////////////////////////////////#
spider_health = int(15)
spider_damage = int(5)
bats_health = int(10)
bats_damage = int(6)
# ////////////////////////////////////////////
spirit_health = int(25)
spirit_damage = int(2)
princess_health = int(35)
princess_damage = int(20)

turn_damage = random.randint(1, damage)
if dungeon.lower() == "forest":
    print("You head down the pathway into the forest. ")
    print("as you head into the forest you come accross a wolf")
    print("you stop to fight the wolf")
    while wolf_health > 0 and health > 0:
        health = health - (wolf_damage - protection)
        wolf_health = wolf_health - (turn_damage * attack)
        print(f"your health is {health}")
        print(f"the wolfs health is{wolf_health}")
        if health <0:
            print("You have died please try again.")
        elif wolf_health < 0:
            print(" you have won you health is reset to 20 ")
            print("and you continue down the forest path.")
            health = 20
            print("as you continue down the forest path you run into a big Timber Wolf.")
            fight = input("Do you fight the Timber Wolf? Y/N")
            if fight.lower() == "n":
                escape = random.randint(1,2)
                if escape == 1: 
                    print("you escape successfully and live out your life on a farm")
                elif escape == 2:
                    print("you are unable to escape from the wolf and he eats you")
            elif fight.lower() == "y":
                while Twolf_health > 0 and health > 0:
                    health = health - (Twolf_damage - protection)
                    Twolf_health = Twolf_health - (turn_damage * attack)
                    print(f"your health is {health}")
                    print(f"the timberwolfs health is {Twolf_health}")
                    if health < 0:
                        print("you died please try again")
                    elif Twolf_health < 0:
                        print("you have survived the forest and make it home safely")




elif dungeon.lower() == "cave":
    print("You head into the mountains to find a cave.")
    print("as you head into the cave your come across a giant spider")
    print("you stop to fight the giant spider")
    while spider_health > 0 and health > 0:
        health = health - (spider_damage - protection)
        spider_health = spider_health - (turn_damage * attack)
        print(f"your health is {health}")
        print(f"the spiders health is{spider_health}")
        if health <0:
            print("You have died please try again.")
        elif spider_health < 0:
            print(" you have won you health is reset to 20 ")
            print("and you continue deeper into the cave.")
            health = 20
            print("as you continue deeper into the cave you run into a big swarm of bats.")
            fight = input("Do you fight the swarm of bats? Y/N")
            if fight.lower() == "n":
                escape = random.randint(1,2)
                if escape == 1: 
                    print("you escape successfully and live out your life on a farm")
                elif escape == 2:
                    print("you are unable to escape from the bats and you go mad trying to find your way out")
            elif fight.lower() == "y":
                while bats_health > 0 and health > 0:
                    health = health - (bats_damage - protection)
                    bats_health = bats_health - (turn_damage * attack)
                    print(f"your health is {health}")
                    print(f"the bats health is {bats_health}")
                    if health < 0:
                        print("you died please try again")
                    elif bats_health < 0:
                        print("you have survived the foest and make it home safely")

elif dungeon.lower() == "tower":
    print("You head into the nearest tower dungeon.")
    print("as you head up into the tower you come across an angry spirit")
    print("you stop to fight the angry spirit")
    while spirit_health > 0 and health > 0:
        health = health - (spirit_damage - protection)
        spirit_health = spirit_health - (turn_damage * attack)
        print(f"your health is {health}")
        print(f"the wolfs health is{spirit_health}")
        if health <0:
            print("You have died please try again.")
        elif spirit_health < 0:
            print(" you have won you health is reset to 20 ")
            print("and you continue up the tower.")
            health = 20
            print("as you continue up the tower you run into the princess.")
            fight = input("Do you fight the princess? Y/N")
            if fight.lower() == "n":
                escape = random.randint(1,2)
                if escape == 1: 
                    print("you escape successfully and live out your life on a farm")
                elif escape == 2:
                    print("you are unable to escape from the princess and she calls the gaurds on you and are locked up")
            elif fight.lower() == "y":
                while princess_health > 0 and health > 0:
                    health = health - (princess_damage - protection)
                    princess_health = princess_health - (turn_damage * attack)
                    print(f"your health is {health}")
                    print(f"the princesses health is {princess_health}")
                    if health < 0:
                        print("you were defeated and the princess calls the gaurds on you.")
                    elif princess_health < 0:
                        print("you have survived princess and she asks you to marry her.")
                        marry = input("do you marry the princess? Y/N")
                        if marry.lower() == "y":
                            print("you marry the princess and live out your days in luxury")
                        else:
                            print("the princess calls the gaurds on you and locks you up for the rest of your life")

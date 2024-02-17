print("You are in a mideval town and have been sent to explore a dungeon \nfirst you need to be outfitted with gear.")
print()


weapon = input("The first item that you get to pick is a Weapon. \nYour choices are: SWORD, AXE, MACE, or DAGGERS ")
print()
print(weapon.lower())

while not weapon.lower() in ("sword","axe","mace",'daggers'):
    weapon = input("The first item that you get to pick is a Weapon. \nYour choices are: SWORD, AXE, MACE, or DAGGERS ")
    print()
else:
    print("success")

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

if dungeon.lower() == "forest":
    print("You head down the pathway into the forest. ")


elif dungeon.lower() == "cave":
    print("You head into the mountains to find a cave.")


elif dungeon.lower() == "tower":
    print("You head into the nearest tower dungeon.")
    

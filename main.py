from room import Room
from item import Item
from character import Enemy, Character, Friend

# room setup
kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining hall")
dining_hall.set_description("A long room with floor to ceiling windows along both sides and a long table in the middle.")

ballroom = Room("Ballroom")
ballroom.set_description("A vast, springy floor. A Damoclean chandelier dangles above. A revolving glitter ball twinkling stars along the walls.")

# linking the rooms
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(ballroom,"west")
dining_hall.link_room(kitchen,"north")
ballroom.link_room(dining_hall, "east")

# introduce a character, Dave in the Dining Hall
dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("That'll be your brain that I'm after")
dave.set_weakness("elephant")
dave.set_awake(True)
dining_hall.set_character(dave)

# add another enemy, Eben, in the Ballroom
eben = Enemy("Eben", "An angry giant with a deep voice")
eben.set_conversation("I run a large computer company")
eben.set_weakness("artichoke")
eben.set_awake(False)
ballroom.set_character(eben)

# add a friend, kate in the kitchen
greta = Friend("Greta", "An environmental warrior")
greta.set_conversation("Stop flying, it's madness and terrible")
greta.set_awake(False)
kitchen.set_character(greta)

# distribute items
sword = Item("sword", "it's pointy at one end")
kitchen.set_item(sword)

elephant = Item("elephant", "surprisingly small, grey and with a trunk")
dining_hall.set_item(elephant)

artichoke = Item("artichoke", "it's green and spikey")
ballroom.set_item(artichoke)


# main game  initialisation

# item storage system
pocket = []

current_room = kitchen

enemies_to_kill = 2

dead = False

# main game loop
while ((not dead) and (eben.get_enemies_killed() < enemies_to_kill)):
    print("\n")
    print (str(eben.get_enemies_killed()))
    current_room.get_details()
    
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
        
    item_here = current_room.get_item()
    if item_here is not None:
        item_here.describe()
     
    command = input("> ")
    if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
        
    elif command == "talk" and inhabitant is not None:
        # Choosing to talk to the inhabitant
        if inhabitant.awake:
            inhabitant.talk()
        else:
            print(inhabitant.name + " is asleep and not very talkative")

    elif command == "fight" and inhabitant is not None:
        if not isinstance(inhabitant, Friend):
            # fight with the inhabitant, if there is one
            print("Choose your weapon")
            weapon = input()
            
            if weapon in pocket:
            
                if inhabitant.fight(weapon):
                    # What to do if win fight
                    print ("You are the victor, the enemy is dead")
                    current_room.set_character(None)
                  
                else:
                    # What happens if you lose
                    print ("You lose, you are dead dead dead")
                    dead = True
                    
            else:
                print ("You are not carrying " + weapon)
            
        else:
            inhabitant.fight(None)

    elif command == "wake":
        inhabitant.wake()
    
    elif command == "sleep":
        inhabitant.sleep()
    
    elif command == "hug" and isinstance(inhabitant, Friend):
        inhabitant.hug()
        
    elif command =="take" and item_here is not None:
        thingy = current_room.get_item().get_name()
        pocket.append(thingy)
        print ("You have taken " + thingy)
        current_room.set_item(None)
        
    elif command == "i":
        print ("You are carrying: ")
        if pocket is not None:
            print (pocket)
        else:
            print ("nothing")
        
if dead:        
    print("\n"+"Game Over, insert coin to play again")
elif eben.get_enemies_killed() == 2:
    print("It was a wonderful adventure, you have killed all of the enemies and lived happily ever after.")
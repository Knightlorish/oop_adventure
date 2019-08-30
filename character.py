class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.awake = None


    def conscious(self):
        if not self.awake:
            print (self.name + " is asleep")


    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )
        self.conscious()
        
    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
            
    # sleeping or awake state
    def set_awake(self, conscious):
        self.awake = conscious
        
    def get_awake(self):
        return self.awake
    
    def wake(self):
        if self.awake:
            print(self.name + " is already awake")
        else:
            print (self.name + " is now awake and not very happy about it")
            self.awake = True
            
    def sleep(self):
        if not self.awake:
            print (self.name + " is already asleep")
        else:
            print (self.name + " falls instantly asleep, hugging themselves and mumbling")
            self.awake = False



    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True


class Friend(Character):
    
    # create a friend
    
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.gift = None
            
    def set_gift(self, present):
        self.gift = present
        
    def get_gift(self):
        return self.gift
        
    def hug(self):
        if self.wake_state:
            print(self.name + " embraces you, Oxytocin floods your system")
        else:
            print(self.name + " is asleep, leave well alone")
            
    def fight(self, combat_item):
        print(self.name + " says friends don't fight, stop being so silly")
        return None
    

class Enemy(Character):
    
    # Create an enemy
    
    killed = 0
    
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
                
    # add some getters and setters for weakness
    def set_weakness(self, weakness_item):
        self.weakness = weakness_item
        
    def get_weakness(self):
        return self.weakness

    def fight(self,combat_item):
        print("You attack " + self.name + " with the " + combat_item)
        if combat_item == self.weakness:
            print("You defeated " + self.name + " with the " + combat_item)
            Enemy.killed += 1
            print ("Dead enemies = " + str(Enemy.killed))
            return True,
        else:
            print (self.name + " batters your tiny head in")
            return False
        
    def get_enemies_killed(self):
        return Enemy.killed
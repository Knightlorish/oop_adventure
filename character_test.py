# character test
from character import Character, Enemy, Friend

dave = Enemy("Dave", "A smelly zombie")

dave.describe()

dave.set_conversation("Just wait there, I'm going to get you.")

dave.talk()

dave.set_weakness("Spider")

print ("Dave's weakness is " + dave.weakness)

kate = Friend("Kate", "An environmental saviour")

kate.set_gift("chopsticks")

kate.hug()

print (isinstance(kate,Friend))




        
        

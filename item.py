class Item():

    def __init__(self, item_name, item_description):
        self.name = item_name
        self.description = item_description
    
    #def set_name (self, item_name):
    #    self.name = item_name
        
    #def get_name (self):
    #    return self.name
        
    #def describe(self):
    #   print (self.description)

    def get_details (self):
        print ("Stuff here: " + self.name + ", " + self.description)
        
    # Describe the item
    def describe(self):
        self.get_details()
        
    def get_name(self):
        return self.name
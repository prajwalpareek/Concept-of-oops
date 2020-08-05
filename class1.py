class Robot:
    
    def __init__(self,name,color,weight):
        self.name = name
        self.color = color
        self.weight = weight 
        
    def introduce_self(self):
        return "My name is "+self.name
            
r1 = Robot("photon","black",41)
r2 = Robot("alpha","white",34)

print(r1.introduce_self())
print(r2.introduce_self())

class Person:
    
    def __init__(self,name,personality,is_sitting):
        self.name = name
        self.personality = personality
        self.is_sitting = is_sitting
        self.robot_owned = r2
        #define a variable robot_owned

    def sit_down(self):
        if self.is_sitting == True:
            return "sitting"
        
    def stand_up(self):
        if self.is_sitting == False:
            return "not sitting"
        
p1 = Person("mohan","happy",False)
p2 = Person("prajwal","Excited",True)

print(p2.sit_down())
print(p1.stand_up())

print(p1.robot_owned.introduce_self())

#this is a option 1 to access methods of any other class by object of any other class.

#output
'''
My name is photon                                                                                                                
My name is alpha                                                                                                                 
sitting                                                                                                                          
not sitting                                                                                                                      
My name is alpha  '''
class Dog():
    dog_age = 7
    def __init__(self,age=5):
        self.age = age
        
    def estimatehumanlif(self):
        return self.age * self.dog_age
    
mydog = Dog()

print(mydog.estimatehumanlif())
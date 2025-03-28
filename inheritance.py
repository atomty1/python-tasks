# Animals
#     Mammals
#         Primate

# Turkey
# class Animal:
#     def __init__(self, eyes):
#         self.eyes = eyes
#         self.m_gland = True
    

# new_turkey = Animal(2)
# new_whale = Animal(2)

# Humans
#     Man
#     Woman
class Human:
    
    def __init__(self, my_name):
        print("Good evening")
        self.name = my_name
        self.eyes = 2
        self.ears = 2
        self.legs = 2
        self.voice = "broad"
    
    def show_name(self):
        print(f"My name is {self.name}")
    def say_hi(self):
        print("Hi")
        
class Man(Human):
    def __init__(self, name):
        super().__init__(name)
        print(f"{name} is my name")

        # print("Hello")
        # self.beards = True
    # def show_name(self):
    #     print("Heeeyyyy")
        
class Woman(Human):
    pass


person_a = Man("Peter")
person_a.say_hi()
print(person_a.name)
# print(person_a.beards)
# print(person_a.eyes)
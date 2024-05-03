class Dog:
    def __init__(self, breed, age, color):
        self.breed = breed
        self.age = age
        self.color = color

    def say_age(self):
        words_to_say = "I am " + str(self.age) + " years old"
        print(words_to_say)

    def bark(self):
        print('Woof woof')
    
    def sleep(self):
        print('Zzzzzz')
    
    def eat(self):
        print('i am eating')


dog = Dog('bhutanese', 20, 'black')
petdog = Dog('pug', 10, 'white')
my_friend_dog = Dog('german shephard', 15, 'brown')

dog.say_age()
petdog.say_age()
my_friend_dog.say_age()
variable = dog.breed
##TASK 1

##Build on top of the code provided
##Create a new behaviour in the class
#Behavinuir names Introduce

#Expected output:
# ? dog.introduce() --> Run this code. Output show be as below: 
#I am a thutanese dog.
 #I am 20 years ald
#I am black in color

class Dog:
    def __init__(self, breed, age, color):
        self.breed = breed
        self.age = age
        self.color = color

    def introduce(self):
        print('HI')
        print(f"I am a {self.breed} dog.")
        print(f"I am {self.age} years old.")
        print(f"I am {self.color} in color.")

# Example usage
dog = Dog("Bhutanese", 20, "black")
dog.introduce()
dog = Dog("pug", 10, "white")
dog.introduce()
dog = Dog("germanshepard", 15, "brown")
dog.introduce()

#task 2
class Dog:
    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    def introduce(self):
        print("Hi")
        print("I am a " + self.breed + " dog.")
        print("I am " + str(self.age) + " years old")
        print("I am " + self.color + " in color")

    def say_age(self):
        words_to_say = "I am " + str(self.age) + " years old"
        print(words_to_say)

    def bark(self):
        print('Woof woof')
    
    def sleep(self):
        print('Zzzzzz')
    
    def eat(self):
        print('i am eating')
    
    def run(self, speed):
        print('I am', self.name)
        print('Okay, i will run in', str(speed), 'km/hr')
        print()

dog = Dog('dechen', 'bhutanese', 20, 'black')
petdog = Dog('dorji', 'pug', 10, 'white')
my_friend_dog = Dog('tashi', 'german shephard', 15, 'brown')

how_fast_should_dog_run = 1000
dog.run(10)
dog.run(100)
dog.run(how_fast_should_dog_run)
petdog.run(20)

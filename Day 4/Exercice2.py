class Dog:
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
        return f"{self.name} barks"

    def run_speed(self):
        return self.weight / self.age * 10

    def fight(self, other_dog):
        my_score = self.run_speed() * self.weight
        other_score = other_dog.run_speed() * other_dog.weight

        if my_score > other_score:
            return f"{self.name} won the fight"
        elif other_score > my_score:
            return f"{other_dog.name} won the fight"
        else:
            return "It's a tie!"



dog1 = Dog("Rex", 3, 30)
dog2 = Dog("Buddy", 2, 25)
dog3 = Dog("Max", 4, 40)

print(f"{dog1.name}'s running speed: {dog1.run_speed()}")
print(f"{dog2.name}'s running speed: {dog2.run_speed()}")
print(f"{dog3.name}'s running speed: {dog3.run_speed()}")

print(dog1.fight(dog2))
print(dog2.fight(dog3))
print(dog3.fight(dog1))
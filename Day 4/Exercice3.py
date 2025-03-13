import random
from Exercice2 import Dog # Importing the Dog class from the previous exercise


class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True
        return f"{self.name} is now trained"

    def play(self, *args):
        dog_names = self.name
        for dog in args:
            dog_names += f", {dog.name}"
        return f"{dog_names} all play together"

    def do_a_trick(self):
        if self.trained:
            tricks = [
                f"{self.name} does a barrel roll",
                f"{self.name} stands on his back legs",
                f"{self.name} shakes your hand",
                f"{self.name} plays dead"
            ]
            return random.choice(tricks)
        else:
            return f"{self.name} is not trained yet"



pet_dog1 = PetDog("morisse", 3, 25)
pet_dog2 = PetDog("langa", 2, 20)
pet_dog3 = PetDog("leo", 4, 30)


print(pet_dog1.train())
print(pet_dog1.do_a_trick())
print(pet_dog2.do_a_trick())
print(pet_dog1.play(pet_dog2, pet_dog3))
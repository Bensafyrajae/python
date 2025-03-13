from Exercice4 import Family

class TheIncredibles(Family):
    def use_power(self, name):
        for member in self.members:
            if member['name'] == name:
                if member['age'] >= 18:
                    return f"{member['name']} uses power: {member['power']}"
                else:
                    raise Exception(f"{member['name']} is not over 18 years old")
        return f"{name} is not a family member"

    def incredible_presentation(self):
        print(f"**Here is our powerful family, The {self.last_name}**")
        super().family_presentation()


incredibles_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False,
     'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False,
     'power': 'read minds', 'incredible_name': 'SuperWoman'}
]

incredibles_family = TheIncredibles("Incredibles", incredibles_members)

incredibles_family.incredible_presentation()

incredibles_family.born(
    name='Jack', age=1, gender='Male', is_child=True,
    power='Unknown Power', incredible_name='BabyJack'
)

incredibles_family.incredible_presentation()

try:
    print(incredibles_family.use_power('Michael'))
    print(incredibles_family.use_power('Sarah'))
    print(incredibles_family.use_power('Jack'))  # This should raise an exception
except Exception as e:
    print(f"Exception: {e}")
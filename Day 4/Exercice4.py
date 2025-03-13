class Family:
    def __init__(self, last_name, members):
        self.last_name = last_name
        self.members = members

    def born(self, **kwargs):
        self.members.append(kwargs)
        print(f"Congratulations to the {self.last_name} family on their new child!")

    def is_18(self, name):
        for member in self.members:
            if member['name'] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Family Name: {self.last_name}")
        for member in self.members:
            print("Member Details:")
            for key, value in member.items():
                print(f"  {key}: {value}")
            print()


initial_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

smith_family = Family("Smith", initial_members)

smith_family.family_presentation()
print(f"Is Michael over 18? {smith_family.is_18('Michael')}")
print(f"Is Sarah over 18? {smith_family.is_18('Sarah')}")

smith_family.born(name='Eya', age=0, gender='Female', is_child=True)

smith_family.family_presentation()
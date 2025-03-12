class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age

def find_oldest_cat(cat_list):
    oldest_cat = cat_list[0]
    for cat in cat_list:
        if cat.age > oldest_cat.age:
            oldest_cat = cat
    return oldest_cat

cat1 = Cat("Emma", 3)
cat2 = Cat("leo", 5)
cat3 = Cat("Snow", 7)

cats = [cat1, cat2, cat3]

oldest_cat = find_oldest_cat(cats)

print(f"Le chat le plus âgé est {oldest_cat.name}, et a {oldest_cat.age} ans.")



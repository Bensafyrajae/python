brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}
#2
brand["number_stores"] = 2
print(brand)
#3
#4
brand["country_creation"] = "Spain"
print(brand)
#5
if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")
print(brand)
#6
del brand["creation_date"]
#7
print(brand["international_competitors"][-1])